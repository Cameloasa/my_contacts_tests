# Mina Vänner Tests

Välkommen to "Mina Vänner Tests" – a project to test the "Mina Vänner" webpage using Playwright and Behave. We use Test-Driven Development (TDD) to keep it simple and fun!

## Prerequisites
- Python 3.13.1 (vi älskar modern Python!)
- Access to the "Mina Vänner" webpage (ex. a URL like `https://forverkliga.se/JavaScript/my-contacts/#/`).

## Installation
1. **Set up virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install playwright
   playwright install
   pip install behave