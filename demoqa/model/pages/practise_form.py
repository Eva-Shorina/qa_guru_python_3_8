from selene.support.shared import browser
from selene import have, command
from demoqa.model.controls import dropdown_list
from demoqa.utils import work_with_path
from demoqa.model.controls import option_select


def send_file(locator, file):
    path = work_with_path.get_path(file)
    browser.element(locator).set_value(path)

def validation(*args):
    browser.element('.table').all('td').even.should(have.texts(args))

def open_page():
    browser.open('/automation-practice-form')
    browser.driver.maximize_window()


def add_name_and_surname(name, surname):
    browser.element('#firstName').type(name)
    browser.element('#lastName').type(surname)


def add_contacts(email, mobile, address):
    browser.element('#userEmail').type(email)
    browser.element('#userNumber').type(mobile)
    browser.element('#currentAddress').type(address)


def add_subject(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def choose_hobby(hobby):
    browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).click()


def add_state(value):
    dropdown_list.choose('#state', value)


def add_city(value):
    dropdown_list.choose('#city', value)


def submit():
    browser.element('#submit').press_enter()


def choose_gender(gender):
    browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()


def select_month(month):
    browser.element('.react-datepicker__month-select').click()
    option_select.select_by_text('.react-datepicker__month-select', month)


def select_year(year):
    browser.element('.react-datepicker__year-select').click()
    option_select.select_by_text('.react-datepicker__year-select', year)


def select_day(day):
    browser.element(f'.react-datepicker__day--0{day}').click()


def click(selector):
    browser.element(selector).click()