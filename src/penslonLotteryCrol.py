import requests
from bs4 import BeautifulSoup

source = requests.get("https://www.dhlottery.co.kr/gameResult.do?method=index720").text
soup = BeautifulSoup(source, "html.parser")
selector = soup.select("table.tbl_data.tbl_data_col")

def getWinningNumberReturnArr(order):
    rtns = []
    list = selector[order].select("tbody > tr")
    for n in list:
        num = int(n.select("td")[2].text)
        rtns.append(num)
    return rtns
