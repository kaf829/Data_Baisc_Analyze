CREATE TABLE `userTBL` (
  userID  char(8) NOT NULL PRIMARY KEY,
  name varchar(10) NOT NULL,
  birthYear int NOT NULL,
  addr char(2) NOT NULL,
  mobile1 char(3),
  mobile2 char(3),
  height SMALLINT,
  mDate DATE
);

CREATE TABLE `buyTBL` (
  num  INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  userID char(6) NOT NULL,
  prodName char(4) NOT NULL,
  groupName char(4),
  price int NOT NULL,
  amount smallINT NOT NULL,
  FOREIGN KEY(userID) REFERENCES userTBL(userID)
);

desc buyTBL;
select * from userTBL;

INSERT INTO userTBL VALUES("LSG", "이승기", 1987, '서울', '011', 1111111, 182, '2008-8-8');

alter table userTBL modify mobile2 char(8);

-- INSERT INTO usertbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO usertbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO usertbl VALUES('KHJ', '김현중', 1986, '서울', '019', '3333333', 181, '2007-7-7');
INSERT INTO usertbl VALUES('JYP', '박진영', 1970, '경기', '011', '4444444', 186, '2009-4-4');
INSERT INTO usertbl VALUES('SSK', '성시경', 1979, '서울', NULL, NULL, 186, '2009-9-9');
INSERT INTO usertbl VALUES('LJB', '임재범', 1963, '서울', NULL, NULL, 182, '2005-5-5');
INSERT INTO usertbl VALUES('YJS', '유재석', 1972, '서울', '011', '6666666', 178, '2008-8-8');
INSERT INTO usertbl VALUES('EJW', '은지원', 1978, '경북', '011', '7777777', 174, '2014-3-3');
INSERT INTO usertbl VALUES('JKW', '조관우', 1965, '경기', '016', '8888888', 176, '2013-5-5');
INSERT INTO usertbl VALUES('BBK', '비비코', 1970, '미국', NULL, NULL, 180, '2013-5-5');


INSERT INTO buytbl VALUES(NULL, 'KBS', '운동화', '의류', 30, 2);
INSERT INTO buytbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buytbl VALUES(NULL, 'JYP', '모니터', '전자', 200, 1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '모니터', '전자', 200, 1);
INSERT INTO buytbl VALUES(NULL, 'KBS', '청바지', '의류', 50, 3);
INSERT INTO buytbl VALUES(NULL, 'BBK', '책', '서적', 15, 2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '청바지', '의류', 50, 1);
INSERT INTO buytbl VALUES(NULL, 'EJW', '청바지', '의류', 50, 1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL, 30, 2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책', '서적', 15, 1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL, 30, 2);

select * from buytbl;


SHOW CREATE TABLE buytbl;

SELECT * FROM USERTBL WHERE NAME = '이승기';
SELECT * FROM USERTBL where birthYear >= 1979 AND height >= 182;
SELECT * FROM USERTBL where birthYear >= 1979 OR height >= 182;
SELECT NAME, HEIGHT FROM usertbl WHERE HEIGHT >= 180 AND HEIGHT <=183;
SELECT NAME, HEIGHT FROM usertbl WHERE HEIGHT BETWEEN 180 AND 183;
SELECT NAME, HEIGHT FROM usertbl WHERE ADDR IN("경남", "전남", "경북");
SELECT NAME, HEIGHT FROM USERTBL WHERE NAME LIKE '김%수';
SELECT NAME, HEIGHT FROM USERTBL WHERE NAME LIKE '김%';
SELECT NAME, HEIGHT FROM USERTBL WHERE NAME LIKE '_승기';

SELECT HEIGHT FROM USERTBL WHERE NAME = '이승기';
SELECT * FROM USERTBL WHERE HEIGHT >= (SELECT HEIGHT FROM USERTBL WHERE NAME = '이승기');

SELECT NAME,HEIGHT FROM USERTBL WHERE HEIGHT >= (SELECT MAX(HEIGHT) FROM USERTBL WHERE ADDR = "서울" );


SELECT NAME, HEIGHT FROM USERTBL
	WHERE HEIGHT >= ANY(SELECT HEIGHT FROM USERTBL WHERE ADDR = '서울');
    
SELECT NAME, mdaate from usertbl order by mdate;

select addr, max(name) from userTbl group by addr;

select emp_no, hire_date from employees order by hire_date ASC LIMIT 5
;
Create table buytbl2 (SELECT * FROM buytbl);

desc buytbl2;

select * from buytbl2;

select prodName, sum(amount) from buyTbl group by prodName;


select userID  as "사용자아이디", sum(price*amount) AS "총급액" from buyTbl group by userID;

select avg(amount) from buytbl;

select * from userTBl;

select count(*), count(mobile1), count(mobile2) from userTBl;

select name, max(height), min(height) from usertbl group by name;

select name, height from usertbl
where height >= any(select height from usertbl where addr = '경남')
;
select userID as '사용자' , sum(price* amount) As total
	from buytbl
    group by userID
    having total > 1000
    order by sum(price * amount) desc
;
select * from buytbl;

select num, groupName, sum(price * amount) as charge
	from buytbl
    group by groupName, num
    with rollup
  ;  
select groupName, sum(price * amount) as charge
	from buytbl
    group by groupName
    with rollup
;

 create table testTbl1(
	id int,
    userName char(3),
    age int
 );
 
 insert into testtbl1 values(1,"홍길동",25);
 insert into testtbl1 values(2,"홍길동",35);
 insert into testtbl1 values(4,"하니",29);
 insert into testtbl1(id, userName) values(2,"설현");
 
 select * From testtbl1;
 delete from testtbl1 where userName = '설현' and id = 2;
 
 SET SQL_SAFE_UPDATES = 0;
 UPDATE `sqldb`.`testtbl1`
SET
userName = "민지"
WHERE id = 2;



 create Table testTBl4(
	id int,
    Fname varchar(50),
    Lname varchar(50));
    
insert into testTBl4
	select emp_no,first_name, last_name
    From employees.employees;
    
select * from testTbl4;

update testTbl4 set Lname = '없음' where fname = 'Georgi';


select * from testtbl4;
Delete from testtbl4 where Fname = "Georgi"

