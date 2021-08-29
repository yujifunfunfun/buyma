import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import eel
import time

def main(date):

    option = Options()                         
    option.add_argument('--headless') 
    option.add_argument('--lang=ja-JP')
    option.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--ignore-ssl-errors')
    option.add_argument('--incognito') 


    #ここで、バージョンなどのチェックをする
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)   


    # Webサイトを開く
    driver.get("https://www.buyma.com/login/")
    time.sleep(5)

    # ログインメールアドレス入力
    driver.find_element_by_id("txtLoginId").send_keys('tyuji051605160516@gmail.com')
    # パスワード入力
    driver.find_element_by_id("txtLoginPass").send_keys('tozuka1998')
    # ログインボタンクリック
    driver.find_element_by_id("login_do").click()
    eel.view_log_js('ログインしました')
    time.sleep(5)
    # 出品画面へ遷移
    driver.get("https://www.buyma.com/my/sell/?tab=b/")
    eel.view_log_js('出品管理へ遷移')
    
    time.sleep(3)

    eel.view_log_js('処理が開始されました')
    # 日付変更動作
    edit_buttons = driver.find_elements_by_class_name('_item_edit_yukodate')
    input_lists = driver.find_elements_by_class_name("_item_yukodate_edit")
    edit_buttons_num = len(edit_buttons)
    for count,(edit_button,input_list) in enumerate(zip(edit_buttons,input_lists),1):
        edit_button.click()
        time.sleep(2)
        input_list.clear()
        time.sleep(1)
        input_list.send_keys(date)
        time.sleep(1)
        eel.view_log_js(f"{count}/{edit_buttons_num}完了")

    eel.view_log_js("処理が完了しました")
    
        
        
# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
