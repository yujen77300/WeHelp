# Python 字典與列表
# 完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中
# manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量不定的情況。

def avg(data):
# 請用你的程式補完這個函式的區塊
  # 設總薪資和非經理人數為0
  total_salary = 0
  nonmanager = 0
  # 列表的長度 len()
  for i in range(len(data["employees"])):
    if (data["employees"][i]["manager"] == 0):
      nonmanager += 1
      total_salary += data["employees"][i]["salary"]
  print(total_salary / nonmanager)


avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
}) # 呼叫 avg 函式


