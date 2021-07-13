BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text,phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'KIM','Kim@naver.com','010-0000-0000','Kim.com','2021-07-01 16:42:42');
INSERT INTO "users" VALUES(2,'Park','Park@gmail.com','010-1111-1111','Park.com','2021-07-01 16:42:42');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-2222','Lee.com','2021-07-01 16:42:42');
INSERT INTO "users" VALUES(4,'Cho','Cho@Daum.net','010-3333-3333','Cho.com','2021-07-01 16:42:42');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@gmail.com','010-1212-2323','Yoo.com','2021-07-01 16:42:42');
COMMIT;
