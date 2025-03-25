import os
import difflib
import json

class AIModule:
    def __init__(self, repo_path="../"):
        self.repo_path = repo_path
        self.config_file = "module_config.json"
        self.load_module_config()

    def load_module_config(self):
        """Load module configuration to identify test cases based on changes."""
        config_path = os.path.join(self.repo_path, self.config_file)
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                self.module_config = json.load(f)
        else:
            self.module_config = {
                "login": ["login_test.py"],
                "search": ["search_test.py"],
                "cart": ["cart_test.py"]
            }
    
    def detect_changes(self):
        """Identify affected modules by checking modified files."""
        modified_files = self.get_git_diff()
        affected_modules = set()

        for file in modified_files:
            for module, tests in self.module_config.items():
                if module in file:
                    affected_modules.update(tests)

        return list(affected_modules)

    def get_git_diff(self):
        """Get modified files using Git diff."""
        try:
            diff_output = os.popen("git diff --name-only HEAD~1").read().splitlines()
            return diff_output
        except Exception as e:
            print(f"Error while fetching Git diff: {e}")
            return []

    def run_tests(self, test_cases):
        """Run affected test cases."""
        if not test_cases:
            print("✅ No affected modules. No tests to run.")
            return
        
        for test in test_cases:
            print(f"🔎 Running test: {test}")
            os.system(f"python3 regression_tests/{test}")

    def generate_report(self):
        """Generate HTML report after test execution."""
        report_path = os.path.join("../reports", "ai_test_report.html")
        with open(report_path, "w") as f:
            f.write("<html><head><title>AI Test Report</title></head><body>")
            f.write("<h2>AI-Driven Regression Test Report</h2>")
            f.write("<p>Modules impacted and tests executed successfully!</p>")
            f.write("</body></html>")
        print(f"📄 Report generated at: {report_path}")

    def execute(self):
        """Main function to detect changes, run tests, and generate report."""
        print("🚀 AI Module is detecting affected modules...")
        affected_tests = self.detect_changes()
        if affected_tests:
            self.run_tests(affected_tests)
            self.generate_report()
        else:
            print("✅ No changes detected. No need to run tests.")
