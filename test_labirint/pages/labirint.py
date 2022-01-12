import os

from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='search-field')

    # Search button
    search_run_button = WebElement(class_name = "b-header-b-search-e-btntxt")

    # search results
    search_results = WebElement(link_text = "Симмонс Дэн")

    # Main header buttons
    search_postponed = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[1]/div[2]/div/ul/li[5]/a/span[1]/span[1]/span[1]")
    search_basket = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[1]/div[2]/div/ul/li[6]/a/span[2]")

    # Main menu buttons
    search_books = WebElement(link_text = "Книги")
    search_great_books = WebElement(link_text = "Главное 2022")
    search_school = WebElement(link_text = "Школа")
    search_toys = WebElement(link_text = "Игрушки")
    search_stationery = WebElement(link_text = "Канцтовары")
    search_club = WebElement(link_text = "Клуб")
    search_region = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[1]/div[4]/div/div[1]/ul/li[12]/span[1]/span/span[3]/span")
    search_delivery = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[1]/div[4]/div/div[1]/ul/li[12]/span[2]/span[2]/a")
    search_rec = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[1]/div[1]/div/a[2]/span[2]/span/span")

    # Sub menu books buttons---------------------------------------------------------------------------------------dead
    search_books_list_1 = WebElement(link_text = "Периодические издания")
    search_all_books = WebElement(link_text = "Все книги")

    search_bilingues = WebElement(link_text = "Билингвы")
    search_literature_english = WebElement(link_text = "Литература на иностранном языке")
    search_literature_english_for_kids = WebElement(link_text = "Литература на иностранном языке для детей")

    search_literature_for_kids = WebElement(link_text = "Детская художественная литература")
    search_kids_time = WebElement(link_text = "Детский досуг")

    search_babyes_first_books_Child_development = WebElement(link_text = "Первые книги малыша.Развитие ребенка")
    search_educational_literature_for_children = WebElement(link_text = "Познавательная литература для детей")

    search_artbooks_Game_worlds_universes = WebElement(link_text = "Артбуки. Игровые миры. Вселенные")
    search_comics = WebElement(link_text = "Комиксы")
    search_comics_for_kids = WebElement(link_text = "Комиксы для детей")
    search_manga = WebElement(link_text = "Манга")
    search_manga_for_kids = WebElement(link_text = "Манга для детей")
    search_novelizations = WebElement(link_text = "Новеллизации")
    search_educational_comics = WebElement(link_text = "Образовательные комиксы")
    search_fan_souvenirs = WebElement(link_text = "Фан-сувениры")

    #--------------------------------------------------------------------------------------------------------------dead

    # Sub main menu buttons
    search_shipp_and_payment = WebElement(link_text = "Доставка и оплата")
    search_certificates = WebElement(link_text = "Сертификаты")
    search_ratings = WebElement(link_text = "Рейтинги")
    search_new = WebElement(link_text = "Новинки")
    search_discounts = WebElement(link_text = "Скидки")
    search_contacts = WebElement(link_text = "Контакты")
    search_support = WebElement(link_text = "Поддержка")
    search_pickup = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[2]/div/ul/li[11]/a")

    # block of shares today
    search_we_give_cards_and_stickers = WebElement(xpath = "//*[@id='left']/div[2]/a[1]/div/div[2]/div[1]")
    search_we_present_a_calendar_of_happiness = WebElement(xpath = "//*[@id='left']/div[2]/a[2]/div/div[2]/div[1]")
    search_best_discounts_of_the_week = WebElement(xpath = "//*[@id='left']/div[2]/a[3]/div/div[2]/div[1]")
    search_surprises_from_publishers = WebElement(xpath = "//*[@id='left']/div[2]/a[4]/div/div[2]/div[1]")
    search_additional_promotions = WebElement(xpath = "//*[@id='left']/div[2]/div/a")

    # Social networks
    search_soc_net = WebElement(link_text = "в соцсетях")
    search_VK1 = WebElement(class_name = "b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-vk")
    search_VK2 = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[2]/div/div/div/div/div[2]/a[8]/span/span")
    search_inst1 = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[2]/div/div/div/div/div[2]/a[2]/span/span")
    search_inst2 = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[2]/div/div/div/div/div[2]/a[7]/span/span")
    search_FB = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[2]/div/div/div/div/div[2]/a[4]/span/span")
    search_YT = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[2]/div/div/div/div/div[2]/a[3]/span/span")
    search_twitter = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[2]/div/div/div/div/div[2]/a[6]/span")
    search_telegram = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[2]/div/div/div/div/div[2]/a[10]/span/span")
    search_tik_tok = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[2]/div/div/div/div/div[2]/a[11]/span/span[2]")
    search_ya_zen = WebElement(xpath = "//*[@id='minwidth']/div[4]/div[1]/div[2]/div/div/div/div/div[2]/a[9]/span/span")

    # Other fields
    search_whats_read = WebElement(link_text = "Что почитать: выбор редакции")
    search_rules = WebElement(link_text = "Правила")

    # down information field

    search_down_information_field_app_store = WebElement(link_text = "App Store")
    search_down_information_field_google_play = WebElement(class_name = "b-rfooter-e-logo b-rfooter-e-logo-googleplay analytics-click-js")
    search_down_information_field_app_gallery = WebElement(class_name = "b-rfooter-e-logo b-rfooter-e-logo-appgallery analytics-click-js")

    # down information field -> katalog
    search_down_information_field_all_books = WebElement(link_text = "Все книги")
    search_down_information_field_school = WebElement(link_text = "Школа")
    search_down_information_field_journals = WebElement(link_text = "Журналы")
    search_down_information_field_toys = WebElement(link_text = "Игрушки")
    search_down_information_field_stationery = WebElement(link_text = "Канцтовары")
    search_down_information_field_CD_DVD = WebElement(link_text = "CD/DVD")
    search_down_information_field_souvenirs = WebElement(link_text = "Сувениры")
    search_down_information_field_household_products = WebElement(link_text = "Товары для дома")

    # down information field -> interesting
    search_down_information_field_labirint_now = WebElement(link_text = "Лабиринт. Сейчас")
    search_down_information_field_kids_navigation = WebElement(link_text = "Детский навигатор")
    search_down_information_field_reader_reviews = WebElement(link_text = "Рецензии читателей")
    search_down_information_field_book_reviews = WebElement(link_text = "Книжные обзоры")
    search_down_information_field_reader_collections = WebElement(link_text = "Подборки читателей")
    search_down_information_field_tests = WebElement(link_text = "Тесты")
    search_down_information_field_news = WebElement(link_text = "Новости Л.")
    search_down_information_field_contests = WebElement(link_text = "Конкурсы")
    search_down_information_field_special_projects = WebElement(link_text = "Спецпроекты")

    # down information field -> help

    search_down_information_field_how_to_make_an_order = WebElement(link_text = "Как сделать заказ")
    search_down_information_field_payment = WebElement(link_text = "Оплата")
    search_down_information_field_express_delivery = WebElement(link_text = "Курьерская доставка")
    search_down_information_field_support = WebElement(link_text = "Поддержка")
    search_down_information_field_write_to_us = WebElement(link_text = "Напишите нам")
    search_down_information_field_all_help = WebElement(link_text = "Вся помощь")
    search_down_information_field_terms_of_use = WebElement(link_text = "Пользовательское соглашение")

    # down information field -> We is social networks

    search_down_information_field_VK = WebElement(link_text="ВКонтакте")
    search_down_information_field_VK_kids = WebElement(link_text="ВКонтакте. Дети")
    search_down_information_field_youtube = WebElement(link_text="Ютьюб")
    search_down_information_field_unstagram = WebElement(link_text="Инстаграм")
    search_down_information_field_unstagram_kids = WebElement(link_text="Инстаграм. Дети")
    search_down_information_field_facebook = WebElement(link_text="Фейсбук")
    search_down_information_field_classmates = WebElement(link_text="Одноклассники")
    search_down_information_field_twitter = WebElement(link_text="Твиттер")
    search_down_information_field_zen = WebElement(link_text="Дзен")
    search_down_information_field_telegram = WebElement(link_text="Телеграм")
    search_down_information_field_tiktok = WebElement(link_text="ТикТок")
