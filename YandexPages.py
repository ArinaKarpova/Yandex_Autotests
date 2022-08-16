import time
from selenium.webdriver import Keys
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class Elements:

    # INPUTS
    SEARCH_INPUT = (By.XPATH, '//input[contains(@class,"input__control")]')
    SEARCH_FIELD = (By.ID, "text")

    # LINKS
    URL_TENSOR_LINK = (By.XPATH,
                       '(//a[contains(@class,"Link")])[1]//ancestor::div[contains(@class,"Organic")]/descendant::b[text() = '
                       '"tensor.ru"]')
    LINK = (By.XPATH, '(//a[contains(@class,"Link")])[1]')
    LINK_TO_IMAGES = (By.XPATH, '//div[contains(@class,"services-new__item-title")][text() = "Картинки"]')

    # IMAGES
    FIRST_IMAGE = (
        By.XPATH, '(//div[contains(@class,"serp-controller")]/descendant::div[contains(@class,"serp-item")])[1]')
    BIG_IMAGE = (By.XPATH, '//img[contains(@class,"MMImage-Origin")]')
    BIG_IMAGE_OPENED = (By.XPATH, '//div[not(contains(@style,"display:none"))]//img[contains(@class,"MMImage-Origi")]')
    CATEGORY = (By.XPATH,
                '//div[contains(@class,"page-layout")]/descendant::div[contains(@class,"PopularRequestList-Item PopularRequestList-Item_pos_0")]')

    # BUTTONS
    BUTTON_NEXT = (
        By.XPATH, '//div[contains(@class,"CircleButton CircleButton_type_next")]/descendant::i[contains(@class,' \
                  '"CircleButton-Icon")] ')
    BUTTON_PREV = (
        By.XPATH, '//div[contains(@class,"CircleButton CircleButton_type_prev")]/descendant::i[contains(@class,' \
                  '"CircleButton-Icon")] ')

    # OBJECTS
    POPUP_CONTENT = (By.XPATH, '//ul[contains(@class,"mini-suggest__popup-content")]')
    SEARCH_RESULT = (By.XPATH, '//div[contains(@class,"main__content")]')


class Actions(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(Elements.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def enter_words(self, word):
        search_field = self.find_element(Elements.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def submit(self):
        elem = self.find_element(Elements.SEARCH_FIELD)
        elem.click()
        elem.send_keys(Keys.ENTER)

    def click_on_the_images_button(self):
        return self.find_element(Elements.LINK_TO_IMAGES, time=2).click()

    def click_on_the_first_category(self):
        time.sleep(2)
        return self.find_element(Elements.CATEGORY, time=3).click()

    def click_on_the_first_image(self):
        time.sleep(2)
        return self.find_element(Elements.FIRST_IMAGE, time=2).click()

    def click_on_the_button_next(self):
        time.sleep(2)
        return self.find_element(Elements.BUTTON_NEXT, time=2).click()

    def click_on_the_button_prev(self):
        time.sleep(2)
        return self.find_element(Elements.BUTTON_PREV, time=2).click()

    def is_search_field_present(self):
        time.sleep(1)
        if self.find_element(Elements.SEARCH_FIELD, time=2):
            return True and print('link to images exist')
        else:
            return False and print('link not exist')

    def is_suggest_present(self):
        time.sleep(1)
        if self.find_element(Elements.POPUP_CONTENT, time=2):
            return True and print('popup is present')
        else:
            return False and print('popup  not exist')

    def is_search_results_present(self):
        time.sleep(1)
        if self.find_element(Elements.SEARCH_RESULT, time=2):
            return True and print('search results is present')
        else:
            return False and print('search results not present')

    def is_first_link_tensor_ru(self):
        time.sleep(1)
        if self.find_element(Elements.URL_TENSOR_LINK, time=2):
            return True and print('The first link is "tensor.ru"')
        else:
            return False and print('The first link is not "tensor.ru"')

    def is_link_to_images_exist(self):
        time.sleep(1)
        if self.find_element(Elements.LINK_TO_IMAGES, time=2):
            return True and print('link to images exist')
        else:
            return False and print('link not exist')

    def is_image_open(self):
        time.sleep(1)
        if self.find_element(Elements.BIG_IMAGE_OPENED, time=2):
            return True and print('The image is open')
        else:
            return False and print('The image not open')

