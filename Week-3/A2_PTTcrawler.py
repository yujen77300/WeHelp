# 抓取ptt網頁(html格式)
import urllib.request as req
targetUrl = []


def getData(url):

    # 建立request物件，然後要有header，看起來像正常使用者的連線
    request = req.Request(url, headers={

        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.50",
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # 解析原始碼取得每篇文章的標題
    # 剛剛得到的資料data，會透過html做解析
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    # bs4尋找網頁標籤的方法 find、find_all
    titles = root.find_all("div", class_="title")

    for title in titles:
        if title.a != None:
            if title.a.string[1:3] == "好雷" or title.a.string[1:3] == "普雷" or title.a.string[1:3] == "負雷":
                targetUrl.append(title.a.string)

    # 抓取上一頁的網址
    nextLink = root.find("a", string="‹ 上頁")
    return (nextLink["href"])

# 製作一個key function，依照好雷、普雷、負雷進行排序


def order(x):
    orderResult = 0
    if x[1:2] == "好":
        orderResult = 0
    if x[1:2] == "普":
        orderResult = 1
    if x[1:2] == "負":
        orderResult = 2
    return orderResult


pageURL = "https://www.ptt.cc/bbs/movie/index.html"
# 抓前十頁的標題
page = 0
while page < 10:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    page += 1

with open("movie.txt", "w", encoding="utf-8") as file:
    for i in sorted(targetUrl, key=order):
        file.write(i+"\n")
