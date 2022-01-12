import pytest
from pages.labirint import MainPage
import time



# Invalid/valid search tests

def test_1_check_main_search(web_browser):
    """ Make sure main search works fine. """
    page = MainPage(web_browser)
    page.search = 'гиперион'
    page.search_run_button.click()
    page.wait_page_loaded()
    page.scroll_down(200)
    page.search_results.click()


def test_2_check_wrong_input_in_search(web_browser):
    """ Make sure that wrong keyboard layout input works fine. """
    page = MainPage(web_browser)

    # Try to enter "Гиперион" with English keyboard:
    page.search = 'ubgthbjy'
    page.search_run_button.click()
    page.wait_page_loaded()
    page.scroll_down(500)
    page.search_results.click()


def test_3_check_main_search(web_browser):
    """ Make sure main search works fine. """
    page = MainPage(web_browser)
    page.search = 'Дары волхвов'
    page.search_run_button.click()
    page.wait_page_loaded()
    page.scroll_down(500)
    page.search_results.click()

# Check clickable header menu tests-----------------------------------------------------------------------alive(2)

def test_3_check_postponed(web_browser):
    page = MainPage(web_browser)
    page.search_postponed.click()
    page.wait_page_loaded()

def test_check_basket(web_browser):
    page = MainPage(web_browser)
    page.search_basket.click()
    page.wait_page_loaded()

# Check clickable main menu tests-------------------------------------------------------------------------alive(9)

def test_check_books(web_browser):
    page = MainPage(web_browser)
    page.search_books.click()
    page.wait_page_loaded()

def test_check_great_books(web_browser):
    page = MainPage(web_browser)
    page.search_great_books.click()
    page.wait_page_loaded()

def test_check_school(web_browser):
    page = MainPage(web_browser)
    page.search_school.click()
    page.wait_page_loaded()

def test_check_toys(web_browser):
    page = MainPage(web_browser)
    page.search_toys.click()
    page.wait_page_loaded()

def test_check_stationery(web_browser):
    page = MainPage(web_browser)
    page.search_stationery.click()
    page.wait_page_loaded()

def test_check_club(web_browser):
    page = MainPage(web_browser)
    page.search_club.click()
    page.wait_page_loaded()

def test_check_region(web_browser):
    page = MainPage(web_browser)
    page.search_region.click()
    page.wait_page_loaded()

def test_check_delivery(web_browser):
    page = MainPage(web_browser)
    page.search_delivery.click()
    page.wait_page_loaded()

def test_check_rec(web_browser):
    page = MainPage(web_browser)
    page.search_rec.click()
    page.wait_page_loaded()

#  Sub menu books buttons tests-------------------------------------------------------------------------------alive(5)

def test_13_check_books(web_browser):
    page = MainPage(web_browser)
    page.search_books_list_1.click()
    page.wait_page_loaded()

def test_check_all_books(web_browser):
    page = MainPage(web_browser)
    page.search_all_books.click()
    page.wait_page_loaded()

def test_check_bilingues(web_browser):
    page = MainPage(web_browser)
    page.search_bilingues.click()
    page.wait_page_loaded()

def test_check_literature_english(web_browser):
    page = MainPage(web_browser)
    page.search_literature_english.click()
    page.wait_page_loaded()

def test_check_literature_english_for_kids(web_browser):
    page = MainPage(web_browser)
    page.search_literature_english_for_kids.click()
    page.wait_page_loaded()

# Sub main menu buttons tests---------------------------------------------------------------------------------alive(8)

def test_check_shipp_and_payment(web_browser):
    page = MainPage(web_browser)
    page.search_shipp_and_payment.click()
    page.wait_page_loaded()

def test_check_certificates(web_browser):
    page = MainPage(web_browser)
    page.search_certificates.click()
    page.wait_page_loaded()


def test_check_ratings(web_browser):
    page = MainPage(web_browser)
    page.search_ratings.click()
    page.wait_page_loaded()

def test_check_new(web_browser):
    page = MainPage(web_browser)
    page.search_new.click()
    page.wait_page_loaded()

def test_check_discounts(web_browser):
    page = MainPage(web_browser)
    page.search_discounts.click()
    page.wait_page_loaded()

def test_check_contacts(web_browser):
    page = MainPage(web_browser)
    page.search_contacts.click()
    page.wait_page_loaded()

def test_check_support(web_browser):
    page = MainPage(web_browser)
    page.search_support.click()
    page.wait_page_loaded()

def test_check_pickup(web_browser):
    page = MainPage(web_browser)
    page.search_pickup.click()
    page.wait_page_loaded()

# block of shares today tests---------------------------------------------------------------------------------alive(5)

def test_check_we_give_cards_and_stickers(web_browser):
    page = MainPage(web_browser)
    page.search_we_give_cards_and_stickers.scroll_to_element()
    page.search_we_give_cards_and_stickers.click()
    page.wait_page_loaded()

def test_check_we_present_a_calendar_of_Happiness(web_browser):
    page = MainPage(web_browser)
    page.search_we_present_a_calendar_of_happiness.scroll_to_element()
    page.search_we_present_a_calendar_of_happiness.click()
    page.wait_page_loaded()

def test_check_best_discounts_of_the_week(web_browser):
    page = MainPage(web_browser)
    page.search_best_discounts_of_the_week.scroll_to_element()
    page.search_best_discounts_of_the_week.click()
    page.wait_page_loaded()

def test_check_surprises_from_publishers(web_browser):
    page = MainPage(web_browser)
    page.search_surprises_from_publishers.scroll_to_element()
    page.search_surprises_from_publishers.click()
    page.wait_page_loaded()

def test_check_additional_promotions(web_browser):
    page = MainPage(web_browser)
    page.search_additional_promotions.scroll_to_element()
    page.search_additional_promotions.click()
    page.wait_page_loaded()


# other field tests----------------------------------------------------------------------------------------alive(2)

def test_check_whats_read(web_browser):
    page = MainPage(web_browser)
    page.search_whats_read.click()
    page.wait_page_loaded()

def test_check_rules(web_browser):
    page = MainPage(web_browser)
    page.search_rules.click()
    page.wait_page_loaded()

# down information field -> katalog----------------------------------------------------------------------------alive(8)

def test_check_search_down_information_field_all_books(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_all_books.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_school(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_school.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_journals(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_journals.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_toys(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_toys.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_stationery(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_stationery.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_CD_DVD(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_CD_DVD.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_souvenirs(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_souvenirs.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_household_products(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_household_products.click()
    page.wait_page_loaded()

# down information field -> interesting------------------------------------------------------------------------alive(9)

def test_check_search_down_information_field_labirint_now(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_labirint_now.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_kids_navigation(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_kids_navigation.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_reader_reviews(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_reader_reviews.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_book_reviews(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_book_reviews.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_reader_collections(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_reader_collections.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_tests(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_tests.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_news(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_news.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_contests(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_contests.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_special_projects(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_special_projects.click()
    page.wait_page_loaded()

# down information field -> help--------------------------------------------------------------------------------alive(7)

def test_check_search_down_information_field_how_to_make_an_order(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_how_to_make_an_order.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_payment(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_payment.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_express_delivery(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_express_delivery.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_support(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_support.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_write_to_us(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_write_to_us.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_all_help(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_all_help.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_terms_of_use(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_terms_of_use.click()
    page.wait_page_loaded()

# down information field -> We is social networks------------------------------------------------------------alive(11)

def test_check_search_down_information_field_VK(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_VK.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_VK_kids(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_VK_kids.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_youtube(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_youtube.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_unstagram(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_unstagram.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_unstagram_kids(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_unstagram_kids.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_facebook(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_facebook.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_classmates(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_classmates.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_twitter(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_twitter.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_zen(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_zen.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_telegram(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_telegram.click()
    page.wait_page_loaded()

def test_check_search_down_information_field_tiktok(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.search_down_information_field_tiktok.click()
    page.wait_page_loaded()
