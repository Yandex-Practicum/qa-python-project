# 🍔 Stellar Burgers: Unit Testing Framework (Part 1)

![CI/CD Status](https://github.com/AlyaSmirnova/Diplom_1/actions/workflows/unit-tests.yml/badge.svg?branch=main)
[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org)
[![Coverage](https://img.shields.io/badge/Coverage-90%25-brightgreen)](https://github.com)
[![Tests](https://img.shields.io/badge/Tests-Pytest-blue?logo=pytest\&logoColor=white)](https://docs.pytest.org/)
[![Reports](https://img.shields.io/badge/Reports-Allure-orange?logo=allure)](https://github.com)

## ✅ Table of Contents
1. [Description](#-description)
2. [Tech Stack & Tools](#-tech-stack-&-tools)
3. [Project Architecture](#-project-architecture)
4. [Allure Reporting Features](#-allure-reporting-features)
5. [Test Coverage](#-test-coverage)
6. [Execution Guide](#-execution-guide)
7. [CI/CD Workflow](#-cicd-workflow)

## 💫 Description
This is the first part of the graduation project: a comprehensive **Unit Testing** suite for the **Stellar Burgers** application. 
The goal of this framework is to ensure the reliability of core business logic, including burger assembly, ingredient management, and price calculation, achieving **100% code coverage**.

## Tech Stack & Tools
- **Language:** Python 3.13+
- **Testing Framework:** [Pytest](https://docs.pytest.org/)
- **Isolation:** [Unittest.Mock](https://docs.python.org) (for mocking dependencies)
- **Coverage Tool:** [Pytest-cov](https://pypi.org/project/pytest-cov/)
- **Reporting:** Allure Framework
- **CI/CD:** GitHub Actions

## Project Architecture
```text
Diplom_1/
    ├── .github/workflows/           # CI/CD pipeline configuration 
    ├── allure-results/              # Raw test execution data (generated after run) 
    ├── praktikum                    # Source code (Business logic)
    │   ├── burger.py
    │   ├── database.py
    │   ├── ingredient.py
    │   ├── ingredient_types.py
    │   ├── order_queue_page.py
    │ 
    ├── tests/                       # Unit test scenarios
    │   ├── test_bun.py
    │   ├── test_burger.py
    │   ├── test_database.py
    │   ├── test_ingredient.py
    │   
    ├── conftest.py                  # Fixtures
    ├── pytest.ini                   # Pytest & Allure configuration
    ├── requirements.txt             # Project dependencies
    └── README.md                    # Comprehensive project documentation
```

## 📊 Allure Reporting Features
The project is integrated with the **Allure Framework** to provide high-level visibility into the unit testing process. Key features include:

*   **Class-Based Grouping:** Tests are logically organized by **Features** corresponding to core classes (`Bun`, `Ingredient`, `Burger`, `Database`), making it easy to navigate the test suite.
*   **Dynamic Documentation:** Uses `@allure.title` and `@allure.description` to transform technical test methods into clear, readable business requirements.
*   **Execution Transparency:** Detailed logging for complex assembly logic in the `Burger` class, ensuring that every step of the burger construction is tracked.
*   **Validation Details:** Comprehensive error messages and attribute verification are captured in the report, simplifying the debugging process.
*   **Scalable Reporting:** Ready for integration with CI/CD tools to track test history and stability over time.

## 🧪 Test Coverage
The suite provides **100% code coverage** for the core logic of the **Stellar Burgers** application, ensuring every method and boundary case is validated:

### 1. Bun Class
* **Constructor Validation:** Ensuring the name and price are set correctly and have the proper data types (`str` and `float`).
* **Method Verification:** Testing `get_name()` and `get_price()` for accurate data retrieval.

### 2. Ingredient Class
* **Initialization:** Verifying the correct assignment of ingredient types (Sauce/Filling), names, and prices.
* **Getters Testing:** Confirming that `get_name()`, `get_price()`, and `get_type()` return the expected values.

### 3. Burger Class (Complex Logic & Mocking)
* **Assembly Operations:** 
    * Successful addition and removal of ingredients using **Mock objects** to isolate tests from the `Ingredient` class.
    * Verification of the `move_ingredient()` method to ensure correct reordering within the list.
* **Pricing Engine:** Testing `get_price()` with **Mocking** and **Patching** to verify the calculation formula: `(Bun Price * 2) + Sum of Ingredients`.
* **Receipt Generation:** Validating the output format of the `get_receipt()` method, ensuring all components are displayed correctly in the final string.

### 4. Database Class
* **Data Integrity:** Verification that the database returns the correct pre-defined list of 3 buns and 6 ingredients.
* **List Validation:** Checking that `available_buns()` and `available_ingredients()` return lists of the expected size and content.

## 🚀 Execution Guide

### 1. Environment Setup
Clone the repository and set up a local virtual environment to ensure dependency isolation:

1. **Clone repository**
> ```bash 
> git clone https://github.com/AlyaSmirnova/Diplom_1
> cd Diplom_1
📦 Repository: [Sprint_5](https://github.com/AlyaSmirnova/Diplom_1)

2. **Create a virtual environment**
> ```bash 
> python -m venv venv

3. **Activate the virtual environment**
> ```bash 
> source venv/bin/activate

4. **Install required dependencies**
> `$ pip install -r requirements.txt`

### 2. Running Tests
The framework is pre-configured via `pytest.ini`. You can execute the full test suite with a single command:
> ```bash 
> pytest

### 3. Code Coverage Analysis
To verify that the tests provide 100% code coverage, run the following command:
> ```bash 
> pytest --cov=praktikum --cov-report=term-missing

### 4. Generating Allure Report
To transform the test results into a visual, interactive HTML report:
> ```bash 
> allure serve allure-results

## ⚙️ CI/CD Workflow
The project is fully automated using **GitHub Actions**. Upon every `push` to the **main** branch or any `Pull Request` creation:

1.  **Environment Provisioning:** A clean **Ubuntu** runner is initialized in the cloud environment.
2.  **Dependency Management:** The Python **3.13** environment is set up, and all required libraries (`Pytest`, `Pytest-cov`, `Allure`) are installed from `requirements.txt`.
3.  **Automated Unit Testing:** Execution of the full test suite to ensure that all core business logic functions correctly.
4.  **Coverage Analysis:** Automated check of **Code Coverage** (100% target) to ensure no untested logic reaches the repository.
5.  **Allure Artifact Generation:** Test results and execution logs are collected to prepare a comprehensive **Allure report**.
6.  **Status Badges:** Real-time feedback on build success and coverage percentage is provided via GitHub status badges.

