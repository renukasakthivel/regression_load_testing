 README.md – Full Documentation
markdown
Copy
Edit
# 🚀 Regression and Load Testing using AI

## 📚 Project Overview
This project automates **regression and load testing** in CI/CD pipelines by leveraging AI to detect affected modules and run necessary test cases. It reduces manual efforts and generates detailed reports for stakeholders.

---

## 📂 Project Structure

regression_load_testing/ ├── ai_module/ │ └── ai_model.py # AI Module to detect affected modules ├── flask_app/ │ └── app.py # Flask App to trigger tests ├── locust_tests/ │ └── locustfile.py # Load testing script using Locust ├── regression_tests/ │ ├── base.py # Base Selenium setup │ ├── login_test.py # Test login functionality │ ├── search_test.py # Test search functionality │ └── cart_test.py # Test add-to-cart and checkout ├── reports/ │ └── ai_test_report.html # Auto-generated test report ├── module_config.json # Configuration for module mapping ├── requirements.txt # Required dependencies └── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Prerequisites

- **Python 3.x** installed and added to PATH.
- **Git** installed for version control.
- **VS Code** or any IDE of your choice.
- **Chrome WebDriver** installed for Selenium.

---

## 📥 Installation

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/regression_load_testing.git
cd regression_load_testing
2. Set Up a Virtual Environment
bash
Copy
Edit
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
🧪 Run AI Module for Regression Testing
1. Navigate to AI Module:
bash
Copy
Edit
cd ai_module
2. Run AI Module:
bash
Copy
Edit
python3 ai_model.py
🌐 Run Flask Web App to Trigger Tests
1. Navigate to Flask App:
bash
Copy
Edit
cd flask_app
2. Start Flask Application:
bash
Copy
Edit
python3 app.py
3. Open Flask Application in Browser:
Go to http://127.0.0.1:5000 to trigger regression and load tests.

📊 Run Load Testing using Locust
1. Navigate to Locust Tests:
bash
Copy
Edit
cd locust_tests
2. Run Locust:
bash
Copy
Edit
locust -f locustfile.py
3. Open Locust Web UI:
Go to http://localhost:8089 to configure and run load tests.

📄 Generate AI Test Report
After running the AI module or Flask app, the test reports will be available in:

bash
Copy
Edit
/reports/ai_test_report.html
🤖 How AI Module Works
Detects Affected Modules: Compares code changes using Git diff.

Maps Changes to Test Cases: Identifies relevant test cases using module_config.json.

Runs Only Affected Tests: Reduces regression testing time.

Generates Reports: Automatically generates HTML test reports.

⚡️ How to Add More Test Cases
Add new Selenium test files in the regression_tests/ directory.

Update module_config.json with new module mappings.

AI Module will automatically detect changes and execute relevant tests.

🔥 Future Enhancements
✅ Jenkins & GitHub CI Integration: Automate test execution with CI pipelines.

✅ Advanced AI Model for Code Impact Analysis: Enhanced AI models for deeper impact analysis.

✅ Custom Load Testing Scenarios: Define multiple load scenarios using Locust.

