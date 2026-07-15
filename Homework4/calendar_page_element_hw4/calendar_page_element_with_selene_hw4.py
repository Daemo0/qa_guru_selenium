from selene import browser, by, be, have


# https://github.com/yashaka/selene

# TODO: переписать используя "голый" Selenium #done
class Calendar:
    def __init__(self, base_element):
        self.input_field = base_element

    def select_date(self, day: str, month: str, year: str):
        # TODO: Как исправить - убрать всплывающее окно что мешает, используя Selene # done
        browser.element(by.text('Level up your automation')).should(be.visible)
        close_banner_btn = browser.element('#fixedban > div > div > button')
        close_banner_btn.click()
        self.input_field.click()
        browser.element(".react-datepicker__month-select").click().element(by.text(month)).click()
        browser.element(".react-datepicker__year-select").click().element(by.text(year)).click()
        browser.element(f'.react-datepicker__day[data-day="{day}"]').click()


class AutomationPracticeFormPage:
    def __init__(self):
        browser.open("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
        self.birthday_calendar = Calendar(browser.element("#dateOfBirthInput"))


class TestSuite:
    def test_select_birthday_date(self):
        page = AutomationPracticeFormPage()
        page.birthday_calendar.select_date(day="15", month="July", year="2000")
        page.birthday_calendar.input_field.should(have.value("15 Jul 2000"))


ts = TestSuite()
ts.test_select_birthday_date()
