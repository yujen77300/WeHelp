#網路連線
import urllib.request as request
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
  # data=response.read().decode("utf-8")
  # 利用json模組讀取json資料
  data=json.load(response)

#將景點名稱列表出來
attractionList = data["result"]["results"]


# 打開檔案
with open("data.csv","w",encoding="utf-8") as file:
  for attraction in attractionList:
    touristSpot = attraction["stitle"]
    area = attraction["address"].split(' ')[2][0:3]
    firstPic ="https://" + attraction["file"].split('https://')[1]
    if int(attraction["xpostDate"][0:4]) >= 2015:
      # 寫入檔案
      file.write(touristSpot+","+area+","+attraction["longitude"]+","+attraction["latitude"]+","+firstPic+"\n")  

