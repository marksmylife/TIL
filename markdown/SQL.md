# SQL

## 기본사항
* 주석은 `-- `로 표시
* 커서 단위로 실행된다!
* 예약어는 대문자, 사용자 작성은 소문자
* 문법 종료시 `;` 넣기

## 문법
* `SHOW DATABASES;` : DB 목록 보여주기 
* `CREATE DATABASE <DB_name>;` : DB(세계관) 만들기
* `DROP DATABASE <DB_name>;` : DB 지우기
* `USE <DB_name>` : DB 이동

### 테이블
* `DROP TABLE <table_name>;` : 테이블 삭제
* `CREATE TABLE <table_name> (
    name VARCHAR(50),
    age INT
);` : 테이블 만들기
* `SHOW TABLES;` : DB 내의 테이블 리스트 보기
* `DESC <table_name>;` : 테이블 속성 보기
* `SELECT * FROM <table_name>`; : 테이블 입력된 실제값 보기
* `DROP TABLE <table_name>;` : 테이블 삭제


### 데이터 입력
* INSERT INTO <table_name> (field1, field2, ...)
    VALUES (value1, value2, ...);
