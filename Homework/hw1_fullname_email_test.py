import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test01():
    print("Позитивная проверка Name")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("Иван Иванов")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "Иван Иванов" in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test02():
    print("Позитивная проверка Email")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "ivan@example.com" in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test03():
    print("Негативная проверка Email - отсутствует '@'")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivanexample.com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "ivanexample.com" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test04():
    print("Негативная проверка Email - отсутствует логин")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("@example.com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "@example.com" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test05():
    print("Негативная проверка Email - отсутствует домен")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@.com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "ivan@.com" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test06():
    print("Негативная проверка Email - отсутствует домен верхнего уровня")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "ivan@example" in result_box.text
        print("Валидация пропускает отсутствие домена верхнего уровня")

    finally:
        driver.quit()


def test07():
    print("Негативная проверка Email - '' в начале логина")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys(" ivan@example.com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "ivan@example.com" in result_box.text
        print("Валидация пропускает пробел в начале логина")

    finally:
        driver.quit()


def test08():
    print("Негативная проверка Email - '' в середине логина")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("iv an@example.com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "iv an@example.com" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test09():
    print("Негативная проверка Email - '' в конце логина")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan @example.com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "ivan @example.com" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test10():
    print("Негативная проверка Email - '' в начале домена")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@ example.com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "ivan@ example.com" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test11():
    print("Негативная проверка Email - '' в середине домена")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@exa mple.com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "ivan@exa mple.com" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test12():
    print("Негативная проверка Email - '' в конце домена")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example .com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "ivan@example .com" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test13():
    print("Негативная проверка Email - '' в начале домена верхнего уровня")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example. com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "ivan@example. com" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test14():
    print("Негативная проверка Email - '' в середине домена верхнего уровня")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.co m")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "ivan@example.co m" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test15():
    print("Негативная проверка Email - '' в конце домена верхнего уровня")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com ")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "ivan@example.com" in result_box.text
        print("Валидация пропускает пробел в конце домена верхнего уровня")

    finally:
        driver.quit()


def test16():
    print("Негативная проверка Email - слишком большой Email")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@aaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaa")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@aaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaa" in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test17():
    print("Негативная проверка Email - запрещенные спецсимволы")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("!v4№@$it3.c0m")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "!v4№@$it3.c0m" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test18():
    print("Негативная проверка Email - SQL-инъекция")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("' OR '1'='1")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert " OR '1'='1'" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


test01()
test02()
test03()
test04()
test05()
test06()
test07()
test08()
test09()
test10()
test11()
test12()
test13()
test14()
test15()
test16()
test17()
test18()
