# Cisco SD-WAN Network API Test Automation 🚀

This project automates the testing of Cisco vManage SD-WAN APIs using **Python**, **pytest**, **Allure Reporting**, and **GitHub Actions CI**. It helps validate SD-WAN REST APIs such as token authentication, inventory fetching, and negative test scenarios in a CI/CD-friendly environment.

---

## 📁 Project Structure

```
network-api-testing-enhanced/
├── auth.py               # Handles authentication and token retrieval
├── api_helper.py         # Generic API request handler
├── get_inventory.py      # Script to fetch and print SD-WAN device inventory
├── tests/
│   ├── test_inventory.py # Validates device inventory API
│   ├── test_token.py     # Tests token generation
│   └── test_negative.py  # Negative test cases (invalid auth, bad endpoint)
├── requirements.txt      # Dependencies
├── Dockerfile            # Docker setup for consistent test execution
├── docker-compose.yml    # Docker service config to run tests and generate reports
├── .github/workflows/    # GitHub Actions CI workflow
└── report.html           # HTML test report (generated)
```

---

## ✅ Features

- 🔐 **Token Authentication** using vManage credentials  
- 📦 **API Testing** for SD-WAN device inventory  
- 🚫 **Negative Testing** for invalid endpoints and bad credentials  
- 🧪 **pytest** with HTML and Allure reports  
- 🐳 **Dockerized** test execution  
- ☁️ **GitHub Actions CI** for automated test runs on every push

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/deepanshu2109/Cisco-Network-API-Test.git
cd Cisco-Network-API-Test
```

### 2. Install dependencies (inside virtualenv)

```bash
pip install -r requirements.txt
```

### 3. Run tests with HTML report

```bash
pytest --html=report.html --self-contained-html -s
```

### 4. Run tests with Allure report

```bash
pytest --alluredir=allure-results
allure generate allure-results -o reports/allure-report --clean
```

---

## 🐳 Docker

To run tests inside a Docker container:

```bash
docker-compose up --build
```

---

## ⚙️ CI/CD with GitHub Actions

All tests run automatically using GitHub Actions defined in `.github/workflows/api-tests.yml`. On every push, the workflow installs dependencies, runs tests, and generates a report.

---

## 📋 Sample Output

### CLI:
```
SD-WAN Devices:
vmanage - vmanage - reachable
vsmart - vsmart - reachable
vbond - vbond - reachable
...
```

### HTML Report:
Open `report.html` in a browser after test execution.

---

## 👤 Author

**Deepanshu Durgam**  
GitHub: [@deepanshu2109](https://github.com/deepanshu2109)

---

## 📝 License

MIT License - feel free to use and adapt for your own SD-WAN API testing needs!
