import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def main(date):

    #ここで、バージョンなどのチェックをする
    driver = webdriver.Chrome(ChromeDriverManager().install())   

    # Webサイトを開く
    driver.get("https://www.buyma.com/login/")
    time.sleep(5)

    # ログインメールアドレス入力
    driver.find_element_by_id("txtLoginId").send_keys('tyuji051605160516@gmail.com')
    # パスワード入力
    driver.find_element_by_id("txtLoginPass").send_keys('tozuka1998')
    # 検索ボタンクリック
    driver.find_element_by_id("login_do").click()
    time.sleep(5)
    # 出品画面へ遷移
    driver.find_element_by_xpath('//*[@id="wrapper"]/div[5]/div[2]/div/div[2]/ul/li[6]/a').click()
    time.sleep(3)

    # 日付変更動作
    edit_buttons = driver.find_elements_by_class_name('_item_edit_yukodate')
    input_lists = driver.find_elements_by_class_name("_item_yukodate_edit")

    for edit_button,input_list in zip(edit_buttons,input_lists):
        edit_button.click()
        time.sleep(2)
        input_list.clear()
        time.sleep(1)
        input_list.send_keys(date)
        time.sleep(1)
    
        
        
# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
