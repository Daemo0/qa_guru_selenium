import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TableElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    @property
    def element(self):
        return self.driver.find_element(*self.locator)

    def get_headers(self) -> list[str]:
        header_elements = self.element.find_elements(By.CSS_SELECTOR, "thead th")
        return [header.text for header in header_elements]

    def get_row_data(self, row_index: int) -> list[str]:
        rows = self.element.find_elements(By.CSS_SELECTOR, "tbody tr")
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return [cell.text for cell in cells]

    def get_cell_value(self, row_index: int, column_index: int) -> str:
        rows = self.element.find_elements(By.CSS_SELECTOR, "tbody tr")
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return cells[column_index].text

# Тест 1 - Вывод 1 строки и значения колонки Due 3 строки таблицы 1;
# Вывод 1 строки и значения колонки Action 4 строки
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/tables")

        table1_locator = (By.ID, "table1")
        table2_locator = (By.ID, "table1")
        table_1 = TableElement(driver, table1_locator)
        table_2 = TableElement(driver, table2_locator)

        headers_1 = table_1.get_headers()
        first_row_1 = table_1.get_row_data(0)
        specific_cell_1 = table_1.get_cell_value(row_index=2, column_index=3)

        headers_2 = table_2.get_headers()
        first_row_2 = table_2.get_row_data(0)
        specific_cell_2 = table_2.get_cell_value(row_index=3, column_index=5)

        print("Данные таблицы 1")
        print("Заголовки таблицы:", headers_1)
        print("Первая строка данных:", first_row_1)
        print(f"Значение в строке 1, колонке 'Due': {specific_cell_1}")

        print("Данные таблицы 2")
        print("Заголовки таблицы:", headers_2)
        print("Первая строка данных:", first_row_2)
        print(f"Значение в строке 1, колонке 'Due': {specific_cell_2}")

        assert "Last Name" in headers_1, "Заголовок 'Last Name' в таблице 1 не найден"
        assert "Smith" in first_row_1, "Фамилия 'Smith' в таблице 1 должна быть в первой строке"
        assert specific_cell_1 == "$100.00", f"Ожидалось $100.00, но  в таблице 1 получено {specific_cell_1}"

        assert "First Name" in headers_2, "Заголовок 'Last Name' в таблице 2 не найден"
        assert "John" in first_row_2, "Имя 'John' в таблице 2 должно быть в первой строке"
        assert specific_cell_2 == "edit delete", f"Ожидалось edit delete, но  в таблице 1 получено {specific_cell_2}"

        print("\n✅ Тест №1 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()


# Тест 2 - вывод 2 строки данных и значения колонки Web Site 4 строки
# Вывод 2 строки данных и значения колонки Web Site 3 строки
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/tables")

        table1_locator = (By.ID, "table1")
        table2_locator = (By.ID, "table1")
        table_1 = TableElement(driver, table1_locator)
        table_2 = TableElement(driver, table2_locator)

        headers_1 = table_1.get_headers()
        second_row_1 = table_1.get_row_data(1)
        specific_cell_1 = table_1.get_cell_value(row_index=3, column_index=4)

        headers_2 = table_2.get_headers()
        second_row_2 = table_2.get_row_data(1)
        specific_cell_2 = table_2.get_cell_value(row_index=1, column_index=4)

        print("Данные таблицы 1")
        print("Заголовки таблицы:", headers_1)
        print("Вторая строка данных:", second_row_1)
        print(f"Значение в строке 2, колонке 'Web Site': {specific_cell_1}")

        print("Данные таблицы 2")
        print("Заголовки таблицы:", headers_2)
        print("Вторая строка данных:", second_row_2)
        print(f"Значение в строке 3, колонке 'Web Site': {specific_cell_2}")

        assert "First Name" in headers_1, "Заголовок 'Last Name' в таблице 1 не найден"
        assert "Frank" in second_row_1, "Имя 'Frank' в таблице 1 должно быть во второй строке"
        assert specific_cell_1 == "http://www.timconway.com", f"Ожидалось http://www.timconway.com, но в таблице 1 получено {specific_cell_1}"

        assert "Email" in headers_2, "Заголовок 'Email' в таблице 2 не найден"
        assert "fbach@yahoo.com" in second_row_2, "Email 'fbach@yahoo.com' в таблице 2 должно быть во второй строке"
        assert specific_cell_2 == "http://www.frank.com", f"Ожидалось http://www.frank.com, но в таблице 2 получено {specific_cell_2}"

        print("\n✅ Тест №2 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()


# Тест 3 - вывод 3 строки данных и значения колонки Action 1 строки
# Вывод 3 строки данных и значения колонки Due 2 строки
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/tables")

        table1_locator = (By.ID, "table1")
        table2_locator = (By.ID, "table1")
        table_1 = TableElement(driver, table1_locator)
        table_2 = TableElement(driver, table2_locator)

        headers_1 = table_1.get_headers()
        third_row_1 = table_1.get_row_data(2)
        specific_cell_1 = table_1.get_cell_value(row_index=0, column_index=5)

        headers_2 = table_2.get_headers()
        third_row_2 = table_2.get_row_data(2)
        specific_cell_2 = table_2.get_cell_value(row_index=1, column_index=3)

        print("Данные таблицы 1")
        print("Заголовки таблицы:", headers_1)
        print("Третья строка данных:", third_row_1)
        print(f"Значение в строке 1, колонке 'Action': {specific_cell_1}")

        print("Данные таблицы 2")
        print("Заголовки таблицы:", headers_2)
        print("Третья строка данных:", third_row_2)
        print(f"Значение в строке 2, колонке 'Due': {specific_cell_2}")

        assert "Email" in headers_1, "Заголовок 'Email' в таблице 1 не найден"
        assert "jdoe@hotmail.com" in third_row_1, "Email 'jdoe@hotmail.com' в таблице 1 должен быть в третьей строке"
        assert specific_cell_1 == "edit delete", f"Ожидалось edit delete, но в таблице 1 получено {specific_cell_1}"

        assert "Last Name" in headers_2, "Заголовок 'Last Name' в таблице 2 не найден"
        assert "Doe" in third_row_2, "Email 'Doe' в таблице 2 должен быть в третьей строке"
        assert specific_cell_2 == "$51.00", f"Ожидалось $51.00, но в таблице 2 получено {specific_cell_2}"

        print("\n✅ Тест №3 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()


# Тест 4 - вывод 4 строки данных и значения колонки Last Name 2 строки
# Вывод 4 строки данных и значения колонки Email 1 строки
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/tables")

        table1_locator = (By.ID, "table1")
        table2_locator = (By.ID, "table1")
        table_1 = TableElement(driver, table1_locator)
        table_2 = TableElement(driver, table2_locator)

        headers_1 = table_1.get_headers()
        fourth_row_1 = table_1.get_row_data(3)
        specific_cell_1 = table_1.get_cell_value(row_index=1, column_index=0)

        headers_2 = table_2.get_headers()
        fourth_row_2 = table_2.get_row_data(3)
        specific_cell_2 = table_2.get_cell_value(row_index=0, column_index=2)

        print("Данные таблицы 1")
        print("Заголовки таблицы:", headers_1)
        print("Четвертая строка данных:", fourth_row_1)
        print(f"Значение в строке 2, колонке 'Last Name': {specific_cell_1}")

        print("Данные таблицы 2")
        print("Заголовки таблицы:", headers_2)
        print("Четвертая строка данных:", fourth_row_2)
        print(f"Значение в строке 1, колонке 'Email': {specific_cell_2}")

        assert "Due" in headers_1, "Заголовок 'Due' в таблице 1 не найден"
        assert "$50.00" in fourth_row_1, "Due '$50.00' в таблице 1 должен быть в четвертой строке"
        assert specific_cell_1 == "Bach", f"Ожидалось Bach, но в таблице 1 получено {specific_cell_1}"

        assert "Web Site" in headers_2, "Заголовок 'Email' в таблице 2 не найден"
        assert "http://www.timconway.com" in fourth_row_2, "Due 'http://www.timconway.com' в таблице 2 должен быть в четвертой строке"
        assert specific_cell_2 == "jsmith@gmail.com", f"Ожидалось jsmith@gmail.com, но в таблице 2 получено {specific_cell_2}"

        print("\n✅ Тест №4 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()


# Тест 5 - sql-инъекция
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/tables")

        table1_locator = (By.ID, "table1")
        table2_locator = (By.ID, "table1")
        table_1 = TableElement(driver, table1_locator)
        table_2 = TableElement(driver, table2_locator)

        headers_1 = table_1.get_headers()
        fourth_row_1 = table_1.get_row_data(3)
        specific_cell_1 = '''< script > alert('xss') < / script > ",
                "1' OR '1'='1"'''

        headers_2 = table_2.get_headers()
        fourth_row_2 = table_2.get_row_data(3)
        specific_cell_2 = '''< script > alert('xss') < / script > ",
                "1' OR '1'='1"'''

        print("Данные таблицы 1")
        print("Заголовки таблицы:", headers_1)
        print("Четвертая строка данных:", fourth_row_1)
        print(f"Значение в строке 2, колонке 'Last Name': {specific_cell_1}")

        print("Данные таблицы 2")
        print("Заголовки таблицы:", headers_2)
        print("Четвертая строка данных:", fourth_row_2)
        print(f"Значение в строке 1, колонке 'Email': {specific_cell_2}")

        assert "Due" in headers_1, "Заголовок 'Due' в таблице 1 не найден"
        assert "$50.00" in fourth_row_1, "Due '$50.00' в таблице 1 должен быть в четвертой строке"
        assert specific_cell_1 == '''< script > alert('xss') < / script > ",
                "1' OR '1'='1"''', f"Ожидалось Bach, но в таблице 1 получено {specific_cell_1}"

        assert "Web Site" in headers_2, "Заголовок 'Email' в таблице 2 не найден"
        assert "http://www.timconway.com" in fourth_row_2, "Due 'http://www.timconway.com' в таблице 2 должен быть в четвертой строке"
        assert specific_cell_2 == '''< script > alert('xss') < / script > ",
                "1' OR '1'='1"''', f"Ожидалось jsmith@gmail.com, но в таблице 2 получено {specific_cell_2}"

        print("\n✅ Тест №5 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()


# Тест 6 (negative) - не найден искомый заголовок во 2 таблице
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/tables")

        table1_locator = (By.ID, "table1")
        table2_locator = (By.ID, "table1")
        table_1 = TableElement(driver, table1_locator)
        table_2 = TableElement(driver, table2_locator)

        headers_1 = table_1.get_headers()
        fourth_row_1 = table_1.get_row_data(3)
        specific_cell_1 = table_1.get_cell_value(row_index=1, column_index=0)

        headers_2 = table_2.get_headers()
        fourth_row_2 = table_2.get_row_data(3)
        specific_cell_2 = table_2.get_cell_value(row_index=0, column_index=2)

        print("Данные таблицы 1")
        print("Заголовки таблицы:", headers_1)
        print("Четвертая строка данных:", fourth_row_1)
        print(f"Значение в строке 2, колонке 'Last Name': {specific_cell_1}")

        print("Данные таблицы 2")
        print("Заголовки таблицы:", headers_2)
        print("Четвертая строка данных:", fourth_row_2)
        print(f"Значение в строке 1, колонке 'Email': {specific_cell_2}")

        assert "Due" in headers_1, "Заголовок 'Due' в таблице 1 не найден"
        assert "$50.00" in fourth_row_1, "Due '$50.00' в таблице 1 должен быть в четвертой строке"
        assert specific_cell_1 == "Bach", f"Ожидалось Bach, но в таблице 1 получено {specific_cell_1}"

        assert "Hehe" in headers_2, "Заголовок 'Hehe' в таблице 2 не найден"
        assert "http://www.timconway.com" in fourth_row_2, "Due 'http://www.timconway.com' в таблице 2 должен быть в четвертой строке"
        assert specific_cell_2 == "jsmith@gmail.com", f"Ожидалось jsmith@gmail.com, но в таблице 2 получено {specific_cell_2}"

        print("\n✅ Тест №4 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()
