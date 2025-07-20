# Cisco SD-WAN Network API Testing (Enhanced)

[![API Tests](https://github.com/yourusername/network-api-testing/actions/workflows/api-tests.yml/badge.svg)](https://github.com/yourusername/network-api-testing/actions)

## 🚀 Features

- ✅ Auth, inventory, interface, event, and template API tests
- 🧪 Pytest + Allure + Code Coverage
- 🐳 Dockerized test execution
- 🔁 GitHub Actions CI/CD with badge support

## 🐳 Run with Docker

```bash
docker build -t sdwan-tests .
docker run --rm sdwan-tests
```

Or with docker-compose:

```bash
docker-compose up --build
```

## 📊 Generate Allure Report (Locally)

```bash
# Inside container or local venv
pytest --alluredir=allure-results
allure generate allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

## 📈 Coverage Report

After running tests:

- Terminal summary
- HTML output at `htmlcov/index.html`
# Cisco-Network-API-Test
