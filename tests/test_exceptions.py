import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.exceptions_page import ExceptionsPage


class TestExceptions:

    @pytest.mark.exceptions
    def no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row 2 should be displayed"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        exceptions_page.add_text_second_row("Water")
        assert exceptions_page.get_confirmation_message() == "Row 2 was saved", "Save Message didn't appear"

    @pytest.mark.exceptions
    def test_invalid_elements_state_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.edit_first_row("Pizza")
        assert exceptions_page.get_confirmation_message() == "Row 1 was saved", "Save Message didn't appear"

    @pytest.mark.exceptions
    def stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert not exceptions_page.instruction_is_not_displayed(
        ), "Instruction shouldn't be displayed"

    @pytest.mark.exceptions
    def timeout_exception(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert exception_page.is_row2_displayed(), "Row 2 should be displayed"


"""
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(
            By.XPATH, "//*[@id='add_btn']")
        add_button_locator.click()

        # wait for 7 seconds
        # driver.implicitly_wait(7)
        wait = WebDriverWait(driver, 7)
        row_2_element = wait.until(ec.presence_of_element_located((
            By.XPATH, "//div[@id='row2']/input")))

        # Verify Row 2 input field is displayed
        assert row_2_element.is_displayed(), "Row 2 should be displayed."



    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_interactable_exception(self, driver):

        # Open the page
        driver.get(
            "https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(
                By.XPATH, "//*[@id='add_btn']")
        add_button_locator.click()

        # wait for 7 seconds
        # driver.implicitly_wait(7)
        wait = WebDriverWait(driver, 7)
        row_2_element = wait.until(ec.presence_of_element_located((
                By.XPATH, "//div[@id='row2']/input")))

        # Verify Row 2 input field is displayed
        assert row_2_element.is_displayed(), "Row 2 is displayed."

        # Type text into the second input field
        row_2_element.send_keys("water")

        # Click 'Save' button by using locator By.name('Save')
        driver.find_element(
            By.XPATH, "//div[@id='row2']/button[@name='Save']").click()

        # Verify text saved
        save_confirmation = wait.until(ec.visibility_of_element_located((
                By.ID, "confirmation")))

        # Verify the confirmation
        save_message = save_confirmation.text
        assert save_message == "Row 2 was saved", "Save Message is verified"

 @pytest.mark.exceptions
  @pytest.mark.debug
   def test_invalid_elements_state_exception(self, driver):
        # Open page
        driver.get(
            "https://practicetestautomation.com/practice-test-exceptions/")

        # Clear input field
        row_1_edit_button = driver.find_element(
            By.XPATH, "//div[@id='row1']/button[@name='Edit']")
        row_1_edit_button.click()
        row_1_element = driver.find_element(
                By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 5)
        wait.until(ec.element_to_be_clickable(
            (By.XPATH, "//div[@id='row1']/input")))
        row_1_element.clear()

        # Type text into the input field
        row_1_element.send_keys("A")
        driver.find_element(
            By.XPATH, "//div[@id='row1']/button[@name='Save']").click()

        save_confirmation = wait.until(ec.visibility_of_element_located((
                By.ID, "confirmation")))

        # Verify the confirmation
        save_message = save_confirmation.text
        assert save_message == "Row 1 was saved", "Save Message is verified"

 @pytest.mark.exceptions
  @pytest.mark.debug
   def test_stale_element_reference_exception(self, driver):

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Find the instructions text element
        instruction_element = driver.find_element(
            By.XPATH, "//p[@id='instructions']")

        # Click 'add' add_button
        add_button_locator = driver.find_element(
            By.XPATH, "//*[@id='add_btn']")
        add_button_locator.click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 7)
        assert wait.until(ec.invisibility_of_element_located(
            (By.XPATH, "//p[@id='instructions']"))), "Instruction text element should not be displayed."

    @pytest.mark.exceptions
    @pytest.mark.debug1
    def test_timeout_exception(self, driver):

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click 'Add' add_button
        add_button_locator = driver.find_element(
            By.XPATH, "//*[@id='add_btn']")
        add_button_locator.click()

        # Wait for 3 seconds for the second input field to be is_displayed
        wait = WebDriverWait(driver, 5)
        row_2_element = wait.until(ec.visibility_of_element_located(
            (By.XPATH, "//div[@id='row2']/input")))

        # Verify the second input is displayed
        assert row_2_element.is_displayed()
"""
