import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup: Initialize WebDriver
@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()  # Ensure the correct path to chromedriver
    driver.get("https://www.entrata.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
 
# Test 1: Check if 'Watch Demo' and 'Sign In' buttons are present
def test_check_demo_and_sign_in_buttons(setup):
    driver = setup
    watch_demo_button = driver.find_element(By.LINK_TEXT, "Watch Demo")
    sign_in_button = driver.find_element(By.LINK_TEXT, "Sign In")
    
    assert watch_demo_button.is_displayed(), "'Watch Demo' button is not visible."
    assert sign_in_button.is_displayed(), "'Sign In' button is not visible."
 
# Test 2: Test the 'Schedule Your Demo' button (without submission)
def test_schedule_your_demo_button(setup):
    driver = setup
    schedule_demo_button = driver.find_element(By.LINK_TEXT, "Schedule Your Demo")
    
    assert schedule_demo_button.is_displayed(), "'Schedule Your Demo' button is not visible."
    
    schedule_demo_button.click()
    
    # Validate that the click triggers an action (without submitting the form)
    form_header = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Schedule Your Demo')]"))
    )
    assert form_header.is_displayed(), "The demo form did not load as expected."
 
# Test 3: Navigate through the 'Products' dropdown and check visibility
def test_navigate_products_dropdown(setup):
    driver = setup
    products_dropdown = driver.find_element(By.LINK_TEXT, "Products")
    
    # Hovering over the 'Products' dropdown (if there's no click behavior)
    products_dropdown.click()
    
    # Wait for a dropdown option to become visible
    first_product_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Platform Overview"))  # Adjust based on actual options
    )
    
    assert first_product_link.is_displayed(), "Products dropdown did not show the expected links."
 
# Test 4: Verify the homepage title
def test_homepage_title(setup):
    driver = setup
    expected_title = "Entrata - Property Management Software"
    
    # Verify the title
    assert driver.title == expected_title, f"Page title mismatch. Expected '{expected_title}', but got '{driver.title}'."