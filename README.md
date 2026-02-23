# INFT-1207 – Software Testing & Quality Assurance

A collection of lab assignments and in-class exercises completed as part of the **INFT-1207 Software Testing** course. Each project progresses from foundational unit testing concepts to full end-to-end browser automation, demonstrating a practical understanding of modern QA techniques in Python.

---

## 🧑‍💻 Skills Demonstrated

| Skill | Tools / Frameworks |
|---|---|
| Unit testing & test-driven development | `unittest` (Python standard library) |
| Test isolation with mocking | `unittest.mock.patch` |
| Data-driven testing | CSV file I/O with the `csv` module |
| Browser automation | Selenium WebDriver (Firefox / GeckoDriver) |
| Modern test runner & fixtures | `pytest` |
| Structured test suites | Custom `TestSuite` runners |
| Input validation & boundary analysis | Manual boundary-value analysis |
| CI-ready project layout | `requirements.txt`, clear folder structure |

---

## 📂 Project Overview

### In-Class Exercises (ICE)

| Folder | Description |
|---|---|
| `ICE/` | Temperature sensor application – validates readings in the range −50 °C to 150 °C and computes min/max/average statistics. |
| `ICE3_Sanyam/` | Enhanced temperature sensor with custom-built `min`/`max` iterators and `unittest` test suite covering valid inputs, boundary values, and overflow errors. |
| `ICE_5/` | Selenium-based exercise targeting a public demo site; demonstrates locating strategies (ID, name, CSS selector, XPath) and `ActionChains` for complex interactions. |

---

### Lab Assignments

#### Lab 0 – Unit Testing Fundamentals (`Lab0/`)
> **Goal:** Get comfortable with Python's `unittest` framework.

- Simple calculator module (`add`, `subtract`)
- Accompanying test file that covers happy paths and edge cases
- Entry point for understanding the test lifecycle (`setUp` / `tearDown`)

**Run:**
```bash
python -m unittest discover Lab0/test
```

---

#### Lab 1 – Secure Password Generator (`Lab1_Group12/`)
> **Goal:** Build a utility with robust input validation and file I/O.

- Generates passwords of configurable length containing letters, digits, and special characters
- Validates all user inputs before generation
- Saves generated passwords to a file

**Run:**
```bash
python Lab1_Group12/src/lab1_sanyam_anchal.py
```

---

#### Lab 2 – Reading List Manager with Mocking (`Lab2_Group4/`)
> **Goal:** Test a CSV-backed CRUD application using mocks to isolate I/O.

- Command-line book manager (add, list, search, delete)
- Persists data to `books.csv`
- Test suite uses `unittest.mock.patch` to capture `stdout` and verify printed output without touching the file system

**Run tests:**
```bash
python -m unittest discover Lab2_Group4/test
```

---

#### Lab 3 – Geometry Calculator with Comprehensive Test Suite (`Lab3_Group1/`)
> **Goal:** Achieve thorough coverage through structured test design.

- Calculates areas of circles, trapeziums, ellipses, and rhombuses
- **40+ unit tests** covering valid inputs, invalid types, negative values, zero, and floating-point precision
- Includes a menu-driven `test_suite.py` runner for selective test execution

**Run all tests:**
```bash
python -m unittest discover Lab3_Group1/test
```

**Run selective suite:**
```bash
python Lab3_Group1/test_suite.py
```

---

#### Lab 4 – E-Commerce Web Automation (`Lab4_Group1/`)
> **Goal:** Automate a real-world e-commerce workflow with Selenium + pytest.

- Target site: [Magento Software Testing Board](https://magento.softwaretestingboard.com)
- **5 end-to-end scenarios:** category navigation, multi-attribute filtering (style, size, price, color, material), add-to-cart, checkout flow, and order confirmation
- Uses `WebDriverWait` + `expected_conditions` for robust synchronisation
- Demonstrates `ActionChains` (hover), JavaScript click override, and CSS/XPath selectors

**Install dependencies:**
```bash
pip install -r Lab4_Group1/requirements.txt
```

**Run tests:**
```bash
pytest Lab4_Group1/test/test_Lab4_Sanyam_Anchal.py -v
```

---

#### Lab 5 – Body Fat Calculator Automation (`Lab5_Group1/`)
> **Goal:** Write a reusable, well-structured Selenium test class with shared fixtures.

- Target site: [calculator.net Body Fat Calculator](https://www.calculator.net/body-fat-calculator.html)
- Tests: clear-button behaviour, valid inputs, invalid inputs, field-specific validation, and female-specific field skipping via `pytest.mark.skipif`
- Shared browser setup/teardown via `setUpClass` / `tearDownClass`
- Helper methods reduce duplication across test cases

**Run tests:**
```bash
pytest Lab5_Group1/src/lab5_sanyam_anchal.py -v
```

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Unit Testing:** `unittest`, `unittest.mock`
- **Web Automation:** Selenium WebDriver 4, GeckoDriver (Firefox)
- **Test Runner:** `pytest`
- **Data Persistence:** CSV (`csv` module)
- **Math / Stats:** `math`, `statistics` (standard library)

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sanyam-bot/LabCode-INFT-1207.git
   cd LabCode-INFT-1207
   ```

2. **Install Selenium dependencies** (required for Lab 4, Lab 5, and ICE_5)
   ```bash
   pip install selenium pytest
   # Firefox + GeckoDriver must also be installed on your machine
   ```

3. **Run any lab's tests** using the commands shown in each section above.

---

## 📝 Course Information

**Course:** INFT-1207 – Introduction to Software Testing  
**Institution:** Durham College  
**Topics Covered:** Unit testing, boundary-value analysis, equivalence partitioning, mocking, integration testing, and browser-based UI automation.

---

*All lab work is original and was completed as part of graded coursework. Group projects were completed in collaboration with a lab partner.*