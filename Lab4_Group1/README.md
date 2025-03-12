# Body Fat Calculator Test Suite

**Authors:**  
Sanyam Singh Sachdeva (100963204)  
Anchalpreet Kaur (100960062)

**Date:** Mar 11, 2025

**Description:**  
This project contains automated test cases for the Body Fat Calculator. The tests are written using Selenium WebDriver and pytest to validate both positive and negative scenarios on the Body Fat Calculator web page.

## Prerequisites

- **Python 3.x**  
- **Selenium:** Install using `pip install selenium`
- **pytest:** Install using `pip install pytest`
- **Firefox Browser:** Installed on your machine.
- **Geckodriver:** Download and ensure it is in your system's PATH (compatible with your Firefox version).

## Test Structure

- **Test Class:**  
  All tests are organized within the `TestDefaultSuite` class.
  
- **Setup & Teardown:**  
  - `setup_class`: Initializes a Firefox WebDriver and opens the Body Fat Calculator webpage before any tests run.
  - `teardown_class`: Quits the WebDriver after all tests have been executed.
  
- **Helper Methods:**  
  - `_fill_common_fields`: Fills in the common fields (age, weight, height, neck, and waist).
  - `_fill_female_specific_fields`: Fills in the additional hip field for female cases.
  
- **Tests:**  
  - **Clear Button Test:** Verifies that all input fields are cleared.
  - **Valid Inputs Test:** Checks if the calculator returns the expected body fat result.
  - **Invalid Inputs Test:** Confirms that appropriate error messages are displayed when non-numeric values are provided.
  - **Field-specific Tests:** Individual tests for missing or empty values in each input field.
  - **Conditional Test:** `test_with_empty_hip` is conditionally skipped for non-female scenarios using `@pytest.mark.skipif`.

## Running the Tests

To run the tests, navigate to the project directory in your terminal and execute:

```bash
 pytest -q test/test_Lab4_Sanyam_Anchal.py

