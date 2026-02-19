# Stellar Burgers API tests

## Setup
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

## Run
```bash
pytest -q
```

## Allure
```bash
pytest --alluredir=allure-results
allure serve allure-results
```
