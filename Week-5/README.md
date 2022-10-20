# 第五周作業

## 要求三
+ 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
```
INSERT INTO member(id,name,username,password,follower_count) VALUES(1,"curry","test","test",1000);
INSERT INTO member(name,username,password,follower_count) VALUES("Iguodala","test","qwer",650);
INSERT INTO member(name,username,password,follower_count) VALUES("Poole","pool","asdf",700);
INSERT INTO member(name,username,password,follower_count) VALUES("Wiggins","publicservant","zxcv",800);
INSERT INTO member(name,username,password,follower_count) VALUES("Thompson","test","5tgb",900);
INSERT INTO member(name,username,password,follower_count) VALUES("Jerome","new","7ujm",200);
INSERT INTO member(name,username,password,follower_count) VALUES("Lamb","new2","8ik,",100);
INSERT INTO member(name,username,password,follower_count) VALUES("PBJ","rookie","9ol.",200);
INSERT INTO member(name,username,password,follower_count) VALUES("Moody","rookie2","poiu",300);
```
![image](https://user-images.githubusercontent.com/54500773/196822600-175b9db3-8dfe-4843-81bc-08cc872c64ec.png)

+ 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
```
 SELECT * FROM member;
```
![image](https://user-images.githubusercontent.com/54500773/196822749-dad92dd2-cd4a-4fd5-b955-69a03fca8327.png)

+ 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
```
SELECT * FROM member ORDER BY TIME DESC;
```
![image](https://user-images.githubusercontent.com/54500773/196822943-dc7f3e79-c1d6-4ef0-a625-72dd76009595.png)

+ 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
```
SELECT * FROM member ORDER BY TIME DESC LIMIT 1,3;
```
![image](https://user-images.githubusercontent.com/54500773/196823118-1553bfb8-0e16-4bfd-9388-d49a0a9d5372.png)

+ 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
```
SELECT * FROM member WHERE username="TEST”;
```
![image](https://user-images.githubusercontent.com/54500773/196823264-8b948e7c-4f9d-4e91-8710-87a7127520da.png)

+ 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```
SELECT * FROM MEMBER WHERE username="TEST" AND password="TEST”;
```
![image](https://user-images.githubusercontent.com/54500773/196823319-e5493fd7-2afd-4693-9a26-ccbd236a51b7.png)

+ 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
```
SET SQL_SAFE_UPDATES=0;
UPDATE MEMBER SET name = "test2" WHERE username="test";
```
![image](https://user-images.githubusercontent.com/54500773/196823761-993b5dcf-4db1-4eeb-ac36-40f9f73a0e7b.png)


## 要求四
+ 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```
SELECT COUNT(*) AS TOTAL_MEMBER FROM member;
```
![image](https://user-images.githubusercontent.com/54500773/196825000-3a0911db-fee8-4cd8-90d7-eaad775dc82f.png)

+ 取得 member 資料表中，所有會員 follower_count 欄位的總和。
```
SELECT SUM(follower_count ) AS TOTAL_FOLLOWER FROM member;
```
![image](https://user-images.githubusercontent.com/54500773/196825072-53228615-194e-4de7-9eaa-9373610c23d8.png)

+ 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
```
SELECT AVG(follower_count) AS AVG_FOLLOWER FROM member;
```
![image](https://user-images.githubusercontent.com/54500773/196825130-c5c89768-2c94-4054-abc0-c99cb5b56f80.png)



## 要求五
+ 在資料庫中，建立新資料表紀錄留⾔資訊，取名字為 message。資料表中必須包含以下欄位設定：
```
CREATE TABLE message(
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id BIGINT NOT NULL,
    content VARCHAR(255) NOT NULL,
    like_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE message ADD FOREIGN KEY(member_id) REFERENCES member(id);
INSERT INTO message(member_id,content,like_count) VALUES(1,"The chef",9999);
INSERT INTO message(member_id,content,like_count) VALUES(3,"You got it",7777);
INSERT INTO message(member_id,content,like_count) VALUES(8,"Dubnation",1111);
INSERT INTO message(member_id,content,like_count) VALUES(9,"warriors",2222);
```
![image](https://user-images.githubusercontent.com/54500773/196826786-e2c4ff4f-66f2-4ae2-a5cb-83b1bd51d2fb.png)

+ 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。
```
SELECT member.name,message.content from member INNER JOIN message ON member.id = message.member_id;
```
![image](https://user-images.githubusercontent.com/54500773/196826954-166ded75-8e10-410c-9389-cc80de1c38d9.png)


+ 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。
```

```

+ 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
```

```
