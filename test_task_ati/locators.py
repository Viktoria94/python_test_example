from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for Main Page locators. All locators should come here."""
    TRUCKS = (By.XPATH, "//span[normalize-space()='Поиск машин']")


class TrucksPageLocators(object):
    """A class for Trucks Page locators. All locators should come here."""
    INPUT_FROM = (By.XPATH, "(//*[@autocomplete or contains(@class,'autocomplete')])[1]")
    DROPDOWN_MENU_FROM = (By.ID, "react-autowhatever-from--item-0")
    INPUT_TO = (By.XPATH, "(//*[@autocomplete or contains(@class,'autocomplete')])[2]")
    DROPDOWN_MENU_TO = (By.ID, "react-autowhatever-to--item-0")
    BUTTON_SEARCH_TRUCKS = (By.XPATH, "//button[normalize-space()='найти транспорт']")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-qa='total-trucks-count']")
    SHOW_CONTACTS = (By.XPATH, "(//button[normalize-space()='Показать контакты'])[10]")
    POP_UP_FAST_REG = (By.XPATH, "//div[@class='ati-id-login']")
    POPUP_FAST_REG_TITLE = (By.XPATH, "//h1[normalize-space()='Вход на ATI.SU']")
