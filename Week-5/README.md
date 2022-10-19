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
![image](https://user-images.githubusercontent.com/54500773/196822600-175b9db3-8dfe-4843-81bc-08cc872c64ec.png)

+ 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
```
 SELECT * FROM MEMBER;
```
![image](https://user-images.githubusercontent.com/54500773/196822749-dad92dd2-cd4a-4fd5-b955-69a03fca8327.png)

+ 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
```
SELECT * FROM MEMBER ORDER BY TIME DESC;
```
![image](https://user-images.githubusercontent.com/54500773/196822943-dc7f3e79-c1d6-4ef0-a625-72dd76009595.png)

+ 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
```
SELECT * FROM MEMBER ORDER BY TIME DESC LIMIT 1,3;
```
![image](https://user-images.githubusercontent.com/54500773/196823118-1553bfb8-0e16-4bfd-9388-d49a0a9d5372.png)

+ 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
```
SELECT * FROM MEMBER WHERE USERNAME="TEST”;
```
![image](https://user-images.githubusercontent.com/54500773/196823264-8b948e7c-4f9d-4e91-8710-87a7127520da.png)

+ 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```
SELECT * FROM MEMBER WHERE USERNAME="TEST" AND PASSWORD="TEST”;
```
![image](https://user-images.githubusercontent.com/54500773/196823319-e5493fd7-2afd-4693-9a26-ccbd236a51b7.png)

+ 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
```
SET SQL_SAFE_UPDATES=0;
UPDATE MEMBER SET NAME = "test2" WHERE USERNAME="test";
```
![image](https://user-images.githubusercontent.com/54500773/196823761-993b5dcf-4db1-4eeb-ac36-40f9f73a0e7b.png)


## 要求四
+ 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```
SELECT COUNT(*) AS TOTAL_MEMBER FROM MEMBER;
```
![image](https://user-images.githubusercontent.com/54500773/196825000-3a0911db-fee8-4cd8-90d7-eaad775dc82f.png)

+ 取得 member 資料表中，所有會員 follower_count 欄位的總和。
```
SELECT SUM(FOLLOWER_COUNT) AS TOTAL_FOLLOWER FROM MEMBER;
```
![image](https://user-images.githubusercontent.com/54500773/196825072-53228615-194e-4de7-9eaa-9373610c23d8.png)

+ 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
```
SELECT AVG(FOLLOWER_COUNT) AS AVG_FOLLOWER FROM MEMBER;
```
![image](https://user-images.githubusercontent.com/54500773/196825130-c5c89768-2c94-4054-abc0-c99cb5b56f80.png)






## 要求五
+ 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。
+ 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。
+ 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
