import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import eel
import time
from logger import *

logger = set_logger(__name__)


def start_chrome():
    global option
    option = Options()                         
    # option.add_argument('--headless') 
    # option.add_argument('--lang=ja-JP')
    # option.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # option.add_argument('--ignore-certificate-errors')
    # option.add_argument('--ignore-ssl-errors')
    # option.add_argument('--incognito') 
    option.add_argument("window-size=1500,1000")
    #ここで、バージョンなどのチェックをする
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)   

def login():
    # Webサイトを開く
    driver.get("https://www.buyma.com/login/")
    time.sleep(5)
    # ログインメールアドレス入力
    driver.find_element_by_id("txtLoginId").send_keys('tyuji051605160516@gmail.com')
    # パスワード入力
    driver.find_element_by_id("txtLoginPass").send_keys('tozuka1998')
    # ログインボタンクリック
    driver.find_element_by_id("login_do").click()
    logger.info('ログインしました')
    eel.view_log_js('ログインしました')
    time.sleep(3)

def excute_action(date):
    # 出品画面へ遷移
    driver.get("https://www.buyma.com/my/sell/?tab=b/")
    logger.info('出品管理へ遷移しました')
    eel.view_log_js('出品管理へ遷移しました')
    time.sleep(3)
    logger.info('処理が開始されました')
    eel.view_log_js('処理が開始されました')
    
    # 日付変更動作
    edit_date_buttons = driver.find_elements_by_class_name('_item_edit_yukodate')
    edit_tanka_buttons = driver.find_elements_by_class_name('_item_edit_tanka')
    input_lists = driver.find_elements_by_class_name("_item_yukodate_edit")

    edit_date_buttons_num = len(edit_date_buttons)
    for count,(edit_date_button,edit_tanka_button,input_list) in enumerate(zip(edit_date_buttons,edit_tanka_buttons,input_lists),1):
        if count > 1:
            edit_tanka_button.click()
        edit_date_button.click()
        time.sleep(1)
        input_list.clear()
        time.sleep(1)
        input_list.send_keys(date)
        time.sleep(1)
        logger.info(f"{count}/{edit_date_buttons_num}完了")
        eel.view_log_js(f"{count}/{edit_date_buttons_num}完了")

    logger.info('処理が完了しました')
    eel.view_log_js("処理が完了しました")


def main(date):
    start_chrome()
    login()
    excute_action(date)
        
        
# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
