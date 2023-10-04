# SQL

## 기본사항
* 주석은 `-- `로 표시
* 커서 단위로 실행된다!
* 예약어는 대문자, 사용자 작성은 소문자
* 문법 종료시 `;` 넣기

## 언어
* `SHOW DATABASES;` : DB 목록 보여주기 
* `CREATE DATABASE <이름>;` : DB(세계관) 만들기
* `DROP DATABASE test;` : DB 지우기

### 테이블
* `DROP TABLE cats;` : 테이블 삭제
* `CREATE TABLE cats (
    name VARCHAR(50),
    age INT
);` : 테이블 만들기
* `SHOW TABLES;` : 테이블 리스트 보기
* `DESC <테이블명>;` : 테이블 내용 보기
