import time
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# python -m unittest simple_test_student_registration_form.py

class TestAutomationForm(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)  # Явное ожидание до 5 секунд
        self.url = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"

    def test_fill_entire_form(self):
        driver = self.driver
        wait = self.wait
        driver.get(self.url)

        form_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/section/h1")))
        self.assertEqual(form_title.text, "Practice Form")

        time.sleep(3)

        form_sub_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/section/div/p")))
        self.assertEqual(form_sub_title.text, "Student Registration Form")

        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Level up your automation')]")))
        close_banner_btn = wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="fixedban"]/div/div/button""")))
        close_banner_btn.click()

        wait.until(EC.invisibility_of_element(close_banner_btn))

        first_name = self.wait.until(EC.element_to_be_clickable((By.ID, "firstName")))
        first_name.send_keys("Денис")

        last_name = driver.find_element(By.ID, "lastName")
        last_name.send_keys("Максимов")

        email = driver.find_element(By.ID, "userEmail")
        email.send_keys("den.maximov@example.com")

        gender_male_label = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='gender-radio-1']")))
        gender_male_label.click()

        mobile_number = driver.find_element(By.ID, "userNumber")
        mobile_number.send_keys("9279987897")

        date_input = driver.find_element(By.ID, "dateOfBirthInput")
        date_input.click()

        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__month-container")))

        month_select = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))
        month_select.click()
        month_select.find_element(By.XPATH, "//option[@value='1']").click()

        year_select = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
        year_select.click()
        year_select.find_element(By.XPATH, "//option[@value='2000']").click()

        day_element = driver.find_element(By.CSS_SELECTOR,
                                          ".react-datepicker__day--017:not(.react-datepicker__day--outside-month)")
        day_element.click()

        subjects_input = self.wait.until(EC.element_to_be_clickable((By.ID, "subjectsInput")))
        subjects_input.send_keys("Economics")
        subjects_input.send_keys(Keys.ENTER)

        hobby_sports = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']"))
        )
        hobby_sports.click()

        hobby_music = driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
        hobby_music.click()

        temp_file_path = os.path.abspath("test_image.jpg")
        with open(temp_file_path, "w") as f:
            f.write("fake image data")

        upload_input = driver.find_element(By.ID, "uploadPicture")
        upload_input.send_keys(temp_file_path)

        current_address = driver.find_element(By.ID, "currentAddress")
        current_address.send_keys("443096, г. Самара, ул. Ленинская, д. 1")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("document.getElementsByTagName('footer')[0].style.display='none';")

        state_dropdown = self.wait.until(EC.element_to_be_clickable((By.ID, "state")))
        state_dropdown.click()
        state_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, """//*[@id="stateCity-wrapper"]/div[2]""")))
        state_option.click()

        city_dropdown = self.wait.until(EC.element_to_be_clickable((By.ID, "city")))
        city_dropdown.click()
        city_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="stateCity-wrapper"]/div[3]""")))
        city_option.click()

        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].click();", submit_button)

        modal_title = self.wait.until(
            EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
        )
        self.assertEqual(modal_title.text, "Thanks for submitting the form")

        time.sleep(3)

        result_table = driver.find_element(By.CLASS_NAME, "table-responsive")
        self.assertIn("Денис Максимов", result_table.text)
        self.assertIn("den.maximov@example.com", result_table.text)
        self.assertIn("Male", result_table.text)
        self.assertIn("9279987897", result_table.text)
        self.assertIn("17 Feb 2000", result_table.text)
        self.assertIn("Economics", result_table.text)
        self.assertIn("Sports, Music", result_table.text)
        self.assertIn("test_image.jpg", result_table.text)
        self.assertIn("443096, г. Самара, ул. Ленинская, д. 1", result_table.text)
        self.assertIn("Uttar Pradesh Merrut", result_table.text)

    def tearDown(self):
        if os.path.exists("test_image.jpg"):
            os.remove("test_image.jpg")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
