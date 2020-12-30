
from selenium import webdriver
from getpass import getpass
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

driver = webdriver.Chrome()


def logging_in(base_url):
    driver.get(base_url)

    fb_id = driver.find_element_by_id("m_login_email")
    fb_password = driver.find_element_by_id("m_login_password")
    login_btn = driver.find_element_by_css_selector('._2pie div')
    email = "moizkhan.42301@gmail.com"

    password = ""
    fb_id.send_keys(email)
    fb_password.send_keys(password)
    login_btn.click()

    while (True):
        try:
            ok_btn = driver.find_element_by_css_selector('._2pis')
            ok_btn.click()
            break
        except:
            continue


def share_post(cap):
    share_post_btn = driver.find_element_by_css_selector("._15kr")
    share_post_btn.click()

    sec_share_post_btn = driver.find_element_by_id("share-with-message-button")
    sec_share_post_btn.click()

    while (True):
        try:
            txt_area = driver.find_element_by_id("share_msg_input")
            txt_area.send_keys(cap)
            break

        except:
            continue

    print("post has been shared \n")
    driver.find_element_by_id("share_submit").click()


def get_post():
    global driver
    post_url = "https://m.facebook.com/groups/380137593049071/permalink/389411455455018/"
    driver.get(post_url)


def get_post_like():
    liked_btn = driver.find_element_by_css_selector(
        "div[data-sigil='ufi-inline-actions'] div")
    liked_btn.click()


def comment_post(txt):
    while(True):
        try:
            cmt_box = driver.find_element_by_css_selector(
                "div[data-sigil='m-composer'] textarea#composerInput")
            cmt_box.send_keys(txt)
            break
        except:
            continue

    post_btn = driver.find_element_by_css_selector(
        "div[data-sigil='m-composer'] button[data-sigil='touchable composer-submit']")

    for i in range(15):
        post_btn.click()


def main():
    base_url = "https://m.facebook.com/"
    logging_in(base_url)

    get_post()
    get_post_like()
    share_post("Post is shared by a fb bot #DSCDSU #python #selenium")
    get_to_post()

    for i in range(50):
        comment_post("Bot challenge accepted. Love this bootcamp. Pythoneers. A great course by a proficient instructors. A well organized course. Have learned many things about python, web automation, web scraping, web-apps.")


if __name__ == '__main__':
    main()
