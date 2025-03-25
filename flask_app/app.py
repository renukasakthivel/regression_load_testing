from flask import Flask, render_template, request, send_file
import subprocess
import os

app = Flask(__name__)

# Path to test scripts and reports
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPORT_DIR = os.path.join(BASE_DIR, 'reports')

# Home Page Route
@app.route('/')
def home():
    return render_template('index.html')

# Run Regression Test Route
@app.route('/run_regression', methods=['POST'])
def run_regression():
    try:
        # Run the regression tests using Selenium
        result = subprocess.run(['python', '../regression_tests/base.py'], capture_output=True, text=True)
        return f"Regression Tests Completed Successfully! <br><br>{result.stdout}"
    except Exception as e:
        return f"Error running regression tests: {str(e)}"

# Run Load Test Route
@app.route('/run_load', methods=['POST'])
def run_load():
    try:
        # Run load tests using Locust
        result = subprocess.run(['locust', '-f', '../locust_tests/locustfile.py', '--headless', '-u', '10', '-r', '1', '--run-time', '1m'], capture_output=True, text=True)
        return f"Load Tests Completed Successfully! <br><br>{result.stdout}"
    except Exception as e:
        return f"Error running load tests: {str(e)}"

# Download Report Route
@app.route('/download_report', methods=['GET'])
def download_report():
    report_path = os.path.join(REPORT_DIR, 'test_report.html')
    if os.path.exists(report_path):
        return send_file(report_path, as_attachment=True)
    else:
        return "No report found! Run tests first."

if __name__ == '__main__':
    app.run(debug=True)
