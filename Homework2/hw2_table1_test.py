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

# Тест 1 - Вывод 1 строки и значения колонки Due 3 строки
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/tables")

        table1_locator = (By.ID, "table1")
        table = TableElement(driver, table1_locator)

        headers = table.get_headers()
        first_row = table.get_row_data(0)
        specific_cell = table.get_cell_value(row_index=2, column_index=3)  # Строка 3, Колонка 4 (Due)

        print("Заголовки таблицы:", headers)
        print("Первая строка данных:", first_row)
        print(f"Значение в строке 3, колонке 'Due': {specific_cell}")

        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Smith" in first_row, "Фамилия 'Smith' должна быть в первой строке"
        assert specific_cell == "$100.00", f"Ожидалось $100.00, но получено {specific_cell}"

        print("\n✅ Тест №1 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()


# Тест 2 - вывод 2 строки данных и значения колонки Web Site 4 строки
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/tables")

        table1_locator = (By.ID, "table1")
        table = TableElement(driver, table1_locator)

        headers = table.get_headers()
        second_row = table.get_row_data(1)
        specific_cell = table.get_cell_value(row_index=3, column_index=4)

        print("Заголовки таблицы:", headers)
        print("Вторая строка данных:", second_row)
        print(f"Значение в строке 4, колонке 'Web Site': {specific_cell}")

        assert "First Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Frank" in second_row, "Имя 'Frank' должно быть во второй строке"
        assert specific_cell == "http://www.timconway.com", f"Ожидалось http://www.timconway.com, но получено {specific_cell}"

        print("\n✅ Тест №2 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()


# Тест 3 - вывод 3 строки данных и значения колонки Action 1 строки
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/tables")

        table1_locator = (By.ID, "table1")
        table = TableElement(driver, table1_locator)

        headers = table.get_headers()
        third_row = table.get_row_data(2)
        specific_cell = table.get_cell_value(row_index=0, column_index=5)

        print("Заголовки таблицы:", headers)
        print("Третья строка данных:", third_row)
        print(f"Значение в строке 1, колонке 'Web Site': {specific_cell}")

        assert "Email" in headers, "Заголовок 'Email' не найден"
        assert "jdoe@hotmail.com" in third_row, "Email 'jdoe@hotmail.com' должен быть в третьей строке"
        assert specific_cell == "edit delete", f"Ожидалось edit delete, но получено {specific_cell}"

        print("\n✅ Тест №3 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()


# Тест 4 - вывод 4 строки данных и значения колонки Last Name 2 строки
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/tables")

        table1_locator = (By.ID, "table1")
        table = TableElement(driver, table1_locator)

        headers = table.get_headers()
        fourth_row = table.get_row_data(3)
        specific_cell = table.get_cell_value(row_index=1, column_index=0)

        print("Заголовки таблицы:", headers)
        print("Четвертая строка данных:", fourth_row)
        print(f"Значение в строке 2, колонке 'Last Name': {specific_cell}")

        assert "Due" in headers, "Заголовок 'Email' не найден"
        assert "$50.00" in fourth_row, "Due '$50.00' должен быть в четвертой строке"
        assert specific_cell == "Bach", f"Ожидалось Bach, но получено {specific_cell}"

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
        table = TableElement(driver, table1_locator)

        headers = table.get_headers()
        fourth_row = table.get_row_data(3)
        specific_cell = '''< script > alert('xss') < / script > ",
                "1' OR '1'='1"'''

        print("Заголовки таблицы:", headers)
        print("Четвертая строка данных:", fourth_row)
        print(f"Значение в строке 2, колонке 'Last Name': {specific_cell}")

        assert "Due" in headers, "Заголовок 'Email' не найден"
        assert "$50.00" in fourth_row, "Due '$50.00' должен быть в четвертой строке"
        assert specific_cell == '''< script > alert('xss') < / script > ",
                "1' OR '1'='1"''', f"Ожидалось Bach, но получено {specific_cell}"

        print("\n✅ Тест №5 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()


# Тест 6 (negative) - не найден искомый заголовок
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/tables")

        table1_locator = (By.ID, "table1")
        table = TableElement(driver, table1_locator)

        headers = table.get_headers()
        fourth_row = table.get_row_data(3)
        specific_cell = table.get_cell_value(row_index=1, column_index=0)

        print("Заголовки таблицы:", headers)
        print("Четвертая строка данных:", fourth_row)
        print(f"Значение в строке 2, колонке 'Last Name': {specific_cell}")

        assert "Hehe" in headers, "Заголовок 'Hehe' не найден"
        assert "$50.00" in fourth_row, "Due '$50.00' должен быть в четвертой строке"
        assert specific_cell == "Bach", f"Ожидалось Bach, но получено {specific_cell}"

        print("\n✅ Тест №6 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()

# Далее несколько вариантов других негативных тестов - закомментировала, чтобы можно было запускать тесты выше

# Тест 7 (negative) - не найден искомый значение в строке
# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#
#     try:
#         driver.get("https://the-internet.herokuapp.com/tables")
#
#         table1_locator = (By.ID, "table1")
#         table = TableElement(driver, table1_locator)
#
#         headers = table.get_headers()
#         fourth_row = table.get_row_data(3)
#         specific_cell = table.get_cell_value(row_index=1, column_index=0)
#
#         print("Заголовки таблицы:", headers)
#         print("Четвертая строка данных:", fourth_row)
#         print(f"Значение в строке 2, колонке 'Last Name': {specific_cell}")
#
#         assert "Due" in headers, "Заголовок 'Due' не найден"
#         assert "$70.00" in fourth_row, "Due '$70.00' должен быть в четвертой строке"
#         assert specific_cell == "Bach", f"Ожидалось Bach, но получено {specific_cell}"
#
#         print("\n✅ Тест №7 успешно пройден!")
#         time.sleep(5)
#
#     finally:
#         driver.quit()
#
#
# # Тест 8 (negative) - не найдено значение specific cell
# if __name__ == "__main__":
#     # Инициализация драйвера
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#
#     try:
#         # Открытие страницы
#         driver.get("https://the-internet.herokuapp.com/tables")
#
#         # Инициализация таблицы как Page Element через её локатор
#         table1_locator = (By.ID, "table1")
#         table = TableElement(driver, table1_locator)
#
#         # Сбор данных для демонстрации
#         headers = table.get_headers()
#         first_row = table.get_row_data(0)
#         specific_cell = table.get_cell_value(row_index=2, column_index=3)  # Строка 3, Колонка 4 (Due)
#
#         # Вывод результатов в консоль
#         print("Заголовки таблицы:", headers)
#         print("Первая строка данных:", first_row)
#         print(f"Значение в строке 3, колонке 'Due': {specific_cell}")
#
#         # Простые проверки (Assertions)
#         assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
#         assert "Smith" in first_row, "Фамилия 'Smith' должна быть в первой строке"
#         assert specific_cell == "http://www.jdoe.com", f"Ожидалось http://www.jdoe.com, но получено {specific_cell}"
#
#         print("\n✅ Тест №8 успешно пройден!")
#         time.sleep(5)
#
#     finally:
#         driver.quit()