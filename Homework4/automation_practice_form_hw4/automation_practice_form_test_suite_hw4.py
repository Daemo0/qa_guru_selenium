import os
import automation_practice_form_po_hw4


class AutomationPracticeFormTestSuite:
    def __init__(self):
        self.automation_practice_form = None
        self.tmp_file_name = None

    def setup(self):
        self.automation_practice_form = automation_practice_form_po_hw4.AutomationPracticeFormPO(
            "https://qa-guru.github.io/one-page-form/automation-practice-form.html")
        self.automation_practice_form.setup()
        self.tmp_file_name = self._create_tmp_file()

    def _create_tmp_file(self):
        file_path = os.path.abspath('test_file.jpg')
        with open(file_path, 'w') as file:
            file.write("Test")
        return file_path

    def tear_down(self):
        if os.path.exists(self.tmp_file_name):
            os.remove(self.tmp_file_name)
        self.automation_practice_form.tear_down()

    def test_form_positive01(self):
        self.setup()
        try:
            self.automation_practice_form.fill_in_form(self.tmp_file_name, "Dmitry", "Bugaev", "bugaev@example.com",
                                                       "Male",
                                                       "1234567890", ("1988", "4", "22"), ("Maths", "English"),
                                                       ("Sports", "Music"),
                                                       "г. Санкт-Петербург, ул. Невский проспект, д 101", "NCR",
                                                       "Noida")
            self.automation_practice_form.assert_form(self.tmp_file_name, "Dmitry", "Bugaev", "bugaev@example.com",
                                                      "Male",
                                                      "1234567890", ("1988", "4", "22"), ("Maths", "English"),
                                                      ("Sports", "Music"),
                                                      "г. Санкт-Петербург, ул. Невский проспект, д 101", "NCR", "Noida")
            print('Тест 1: Данные совпали!')
        finally:
            self.tear_down()

    def test_form_positive02(self):
        self.setup()
        try:
            # TODO: придумай другой набор тестовых данных # done
            self.automation_practice_form.fill_in_form(self.tmp_file_name, "Anfisa", "Maximova", "anf@maximov.com",
                                                       "Female", "0987654321", ("2002", "2", "17"), ("Biology", "Arts"),
                                                       ("Sports", "Music"), "443000, г. Самара, ул. Пушкина, д 1",
                                                       "Haryana",
                                                       "Karnal")
            self.automation_practice_form.assert_form(self.tmp_file_name, "Anfisa", "Maximova", "anf@maximov.com",
                                                      "Female",
                                                      "0987654321", ("2002", "2", "17"), ("Biology", "Arts"),
                                                      ("Sports", "Music"),
                                                      "443000, г. Самара, ул. Пушкина, д 1", "Haryana", "Karnal")
            print('Тест 2: Данные совпали!')
        finally:
            self.tear_down()


test_suite = AutomationPracticeFormTestSuite()
test_suite.test_form_positive01()
test_suite.test_form_positive02()
# TODO: в общем виде работать не будет, и в нашем виде работать не будет, так как setup и tear_down должны вызываться перед каждым тестом ... так же в идеале перед каждым тестом создается PO - подумайте как решить малой кровью (в будущем через Test Runner) # done
