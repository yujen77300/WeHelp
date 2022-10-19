# 第五周作業

## 要求三
+ 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
```
insert into member(id,name,username,password,follower_count) values(1,"curry","test","test",1000);
insert into member(name,username,password,follower_count) values("Iguodala","test","qwer",650);
insert into member(name,username,password,follower_count) values("Poole","pool","asdf",700);
insert into member(name,username,password,follower_count) values("Wiggins","publicservant","zxcv",800);
insert into member(name,username,password,follower_count) values("Thompson","test","5tgb",900);
insert into member(name,username,password,follower_count) values("Jerome","new","7ujm",200);
insert into member(name,username,password,follower_count) values("Lamb","new2","8ik,",100);
insert into member(name,username,password,follower_count) values("PBJ","rookie","9ol.",200);
insert into member(name,username,password,follower_count) values("Moody","rookie2","poiu",300);
```
![image](https://user-images.githubusercontent.com/54500773/196822432-2db00ff7-eedb-4da5-ae51-801ebe0528e9.png)

+ 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
+ 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
+ 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
+ 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
+ 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
+ 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。



## 要求四
+ 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
+ 取得 member 資料表中，所有會員 follower_count 欄位的總和。
+ 取得 member 資料表中，所有會員 follower_count 欄位的平均數。






## 要求五
+ 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。
+ 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。
+ 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
