import pytest
from YandexPages import Actions, Elements


@pytest.mark.search
def test_yandex_search(browser):
    yandex = Actions(browser)
    yandex.go_to_site()
    yandex.is_search_field_present()
    yandex.enter_words("Тензор")
    yandex.is_suggest_present()
    yandex.submit()
    yandex.is_search_results_present()
    yandex.is_first_link_tensor_ru()


# В данном случае я разделила тест с Яндекс картинками на две части, так как не смогла корректно настроить переход между вкладками в браузере.
# Пробовала делать его разными способами: через горячие клавиши send_keys(Keys.CONTROL + '2'), через driver.switch_to.window(2)

@pytest.mark.images
def test_images_first_part(browser):
    yandex = Actions(browser)
    yandex.go_to_site()
    yandex.is_link_to_images_exist()
    yandex.click_on_the_images_button()


@pytest.mark.images
def test_images_second_part(browser):
    yandex = Actions(browser)
    yandex.go_to_site_2()
    # Проверка, что перешли на https://yandex.ru/images/, реализована в получении текущего url, что, наверное, не совсем корректно:
    yandex.get_url()
    yandex.click_on_the_first_category()
    # Проверить, что название категории отображается в поле поиска, не получилось. Мне не удалось найти необходимого атрибута у поля поиска в devtools.
    yandex.click_on_the_first_image()
    yandex.find_element(Elements.BIG_IMAGE, time=2)
    yandex.is_image_open()
    k = yandex.find_element_and_get_src(Elements.BIG_IMAGE, time=2)
    print(k)
    yandex.click_on_the_button_next()
    t = yandex.find_element_and_get_src(Elements.BIG_IMAGE, time=2)
    print(t)
    assert k != t
    if k != t:
        print('The image has changed')
    yandex.click_on_the_button_prev()
    m = yandex.find_element_and_get_src(Elements.BIG_IMAGE, time=2)
    print(m)
    assert k == m
    if k == m:
        print('This image from step 8')
