import requests
from bs4 import BeautifulSoup
import time

amazonURL ="https://www.amazon.co.jp/Python%E3%81%A7%E3%81%AF%E3%81%98%E3%82%81%E3%82%8B%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92-%E2%80%95scikit-learn%E3%81%A7%E5%AD%A6%E3%81%B6%E7%89%B9%E5%BE%B4%E9%87%8F%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%A8%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AE%E5%9F%BA%E7%A4%8E-Andreas-C-Muller/dp/4873117984/ref=sr_1_10?dib=eyJ2IjoiMSJ9.aZnjMISH59r91Jtp6ccoYJo3mujh5IWrDTcg8ULrVtGTY23CIsaDf4zN3DxMs6UbrWy6V7w19XfbgUbpUGjMLkL4Z3uSCdjs5xrYo7Xle0NBjJcJY_9QAbxiK_HdP_e9rrAq6gFIyEQprVxrsLb8J5eHqPdzLaYwdOlEnIQFA1RxrAEXEYUitTOSw3u1QiZbqsCbMje7IpxBwqmYoBx_qFMnVWADXWzPuX7cD-1mR8S_r3vdaAoYw-wsxe_Xx4fDZKQ4OebEpex32qMhUWgIy41svHJVYSh7-dKcGqtpMfs.x3vv32oHRUr0O81iBfwEXevZuS1fg4MePAtJmeFXECk&dib_tag=se&keywords=python+%E3%82%AA%E3%83%A9%E3%82%A4%E3%83%AA%E3%83%BC&qid=1729132730&sr=8-10"

def amazonTrackingPrice():
    amazonPage =requests.get(amazonURL)
    soup = BeautifulSoup(amazonPage.content,"html.parser")
   # print(soup)

    title = soup.find(id="productTitle").get_text()
    price = soup.find("span",class_="a-size-base").get_text()
    convertedPrice = price[2:7].replace(",","")
    intPrice=int(convertedPrice)
    print(title)
    print(price)
    print(convertedPrice)

    if (intPrice < 3000):
        sendLineNotify()
def sendLineNotify():
    print("lineに通知しました")
    lineNotifyToken ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    lineNotifyApi = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {lineNotifyToken}"}
    data = {"message": "今がお買い時です！https://www.amazon.co.jp/Python%E3%81%A7%E3%81%AF%E3%81%98%E3%82%81%E3%82%8B%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92-%E2%80%95scikit-learn%E3%81%A7%E5%AD%A6%E3%81%B6%E7%89%B9%E5%BE%B4%E9%87%8F%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%A8%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AE%E5%9F%BA%E7%A4%8E-Andreas-C-Muller/dp/4873117984/ref=sr_1_10?dib=eyJ2IjoiMSJ9.aZnjMISH59r91Jtp6ccoYJo3mujh5IWrDTcg8ULrVtGTY23CIsaDf4zN3DxMs6UbrWy6V7w19XfbgUbpUGjMLkL4Z3uSCdjs5xrYo7Xle0NBjJcJY_9QAbxiK_HdP_e9rrAq6gFIyEQprVxrsLb8J5eHqPdzLaYwdOlEnIQFA1RxrAEXEYUitTOSw3u1QiZbqsCbMje7IpxBwqmYoBx_qFMnVWADXWzPuX7cD-1mR8S_r3vdaAoYw-wsxe_Xx4fDZKQ4OebEpex32qMhUWgIy41svHJVYSh7-dKcGqtpMfs.x3vv32oHRUr0O81iBfwEXevZuS1fg4MePAtJmeFXECk&dib_tag=se&keywords=python+%E3%82%AA%E3%83%A9%E3%82%A4%E3%83%AA%E3%83%BC&qid=1729132730&sr=8-10"}
    requests.post(lineNotifyApi, headers=headers, data=data)

while(True):
        print("トラッキングしました")
        time.sleep(60 * 60)
        amazonTrackingPrice()
 #テスト　こちらは写経になります  
 #      lineNotifyTokenは個人情報になりますのでXで埋めさせていただきました