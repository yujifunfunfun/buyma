import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import eel
import time
from logger import *
import csv
import re
import datetime


logger = set_logger(__name__)

def start_chrome():
    global option
    option = Options()                         
    # option.add_argument('--headless') 
    option.add_argument('--lang=ja-JP')
    # option.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # option.add_argument('--ignore-certificate-errors')
    # option.add_argument('--ignore-ssl-errors')
    # option.add_argument('--incognito') 
    option.add_argument("window-size=1500,1000")
    #ここで、バージョンなどのチェックをする
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)   

def login():
    try:
        # Webサイトを開く
        driver.get("https://www.buyma.com/login/")
        time.sleep(5)

        # CSVからID、パスワードの取得
        csv_file = open("id_pass.csv", "r", encoding="ms932")
        f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        l = [row for row in f]
        id = l[1][0]
        passwd = l[1][1]

        # ログインメールアドレス入力
        driver.find_element_by_id("txtLoginId").send_keys(id)
        # パスワード入力
        driver.find_element_by_id("txtLoginPass").send_keys(passwd)
        # ログインボタンクリック
        driver.find_element_by_id("login_do").click()
        logger.info('ログインしました')
        eel.view_log_js('ログインしました')
        time.sleep(3)
    except Exception as e:
        logger.info(e)
        eel.view_log_js('エラーが発生しました')
        driver.quit()

def cal_click_count(input_month):

    date = str(datetime.date.today())
    p = r'-(.*)-'
    this_month = re.search(p, date).group(1)
    this_month = this_month.lstrip('0')
    click_count = int(input_month) - int(this_month)
    return click_count


def edit_date(input_month,input_day):
    try:
        # カレンダーの「次」ボタンを押す回数を計算
        click_count = cal_click_count(input_month)
        # 出品画面へ遷移
        driver.get("https://www.buyma.com/my/sell/?tab=b/")
        logger.info('出品管理へ遷移しました')
        eel.view_log_js('出品管理へ遷移しました')
        time.sleep(3)
        # 表示件数の変更
        driver.find_element_by_class_name("js-row-count-options").click()
        driver.find_element_by_xpath('//*[@id="row-count-options"]/option[3]').click()
        time.sleep(2)
        # 日付変更動作
        logger.info('日付変更処理が開始されました')
        eel.view_log_js('日付変更処理が開始されました')
        edit_date_buttons = driver.find_elements_by_class_name('_item_edit_yukodate')
        edit_date_buttons_num = len(edit_date_buttons)

        for count,edit_date_button in enumerate(edit_date_buttons,1):
            edit_date_button.click()
            time.sleep(1)
            for i in range(0,int(click_count)):
                driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/a[2]/span').click()
                time.sleep(1)
            
            driver.find_element_by_xpath(f'//a[contains(@href,"#") and text()={input_day}]').click()
            time.sleep(1)
            logger.info(f"{count}/{edit_date_buttons_num}完了")
            eel.view_log_js(f"{count}/{edit_date_buttons_num}完了")

        while len(driver.find_elements_by_xpath('//a[@rel="next" and text()="次へ"]')) > 0:
            driver.find_element_by_xpath('//a[@rel="next" and text()="次へ"]').click()
            logger.info('次のページに遷移しました')
            eel.view_log_js("次のページに遷移しました")

            edit_date_buttons = driver.find_elements_by_class_name('_item_edit_yukodate')
            edit_date_buttons_num = len(edit_date_buttons)

            for count,edit_date_button in enumerate(edit_date_buttons,1):
                edit_date_button.click()
                for i in range(0,int(click_count)):
                    driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/a[2]/span').click()
                    time.sleep(1)
                
                driver.find_element_by_xpath(f'//a[text()={input_day}]').click()
                time.sleep(1)

                logger.info(f"{count}/{edit_date_buttons_num}完了")
                eel.view_log_js(f"{count}/{edit_date_buttons_num}完了")

        logger.info('処理が完了しました')
        eel.view_log_js("処理が完了しました")
        driver.quit()
    except Exception as e:
        logger.info(e)
        eel.view_log_js('エラーが発生しました')
        # driver.quit()



def main(input_month,input_day):
    start_chrome()
    login()
    edit_date(input_month,input_day)
        
        
# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
