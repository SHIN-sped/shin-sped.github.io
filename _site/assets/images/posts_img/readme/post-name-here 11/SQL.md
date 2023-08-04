## SQL의 JOIN 연산 과정

### SQL의 JOIN은 두 개 이상의 테이블에서 데이터를 검색할 때 사용하는 방법 중 하나입니다. JOIN은 두 개 이상의 테이블에서 데이터를 가져와서 하나의 결과 집합으로 만드는 것을 말합니다. JOIN은 INNER JOIN, OUTER JOIN, CROSS JOIN 등이 있습니다

### INNER JOIN은 두 테이블에서 공통된 값을 가진 열을 기준으로 두 테이블을 연결합니다. OUTER JOIN은 INNER JOIN과 비슷하지만, 한쪽 테이블에만 있는 데이터도 결과에 포함시킵니다. CROSS JOIN은 두 테이블의 모든 조합을 만들어 결과를 반환합니다

#### JOIN 연산은 다음과 같은 과정을 거칩니다

1. FROM 절에서 조인할 테이블을 지정합니다.
2. ON 절에서 조인할 열을 지정합니다.
3. WHERE 절에서 필요한 데이터를 검색합니다.

### 참고 사이트 (https://learn.microsoft.com/ko-kr/sql/relational-databases/performance/joins?view=sql-server-ver16)



## 스터디 노트 

```Mysql
CREATE DATABASE 데이터베이스이름

CREEATE TABLE Test
(
	ID INT,
  	Name VARCHAR(30),
  	ReserveDate DATE,
  	RoomNum INT
)

ALTER DATABASE 데이터베이스이름 CHARACTER SET=문자집합이름
ALTER DATABASE 데이터베이스이름 COLLATE=콜레이션이름

ALTER DATABASE Hotel CHARACTER SET=euckr_bin COLLATE=euckr_korean_ci;

ALTER TABLE Reservation
ADD Phone INT;

ALTER TABLE Reservation
DROP RoomNum;

ALTER TABLE Reservation
MODIFY COLUMN ReserveDate VARCHAR(20);


DROP DATABASE Hotel;
DROP TABLE 테이블이름
TRUNCATE TABLE 테이블이름

INSERT INTO 테이블이름(필드이름1, 필드이름2, 필드이름3, ...)
VALUES (데이터값1, 데이터값2, 데이터값3, ...)

INSERT INTO 테이블이름
VALUES (데이터값1, 데이터값2, 데이터값3, ...)

INSERT INTO Reservation(ID, Name, ReserveDate, RoomNum)
VALUES(5, '이순신', '2016-02-16', 1108);

UPDATE 테이블이름
SET 필드이름1=데이터값1, 필드이름2=데이터값2, ...
WHERE 필드이름=데이터값

UPDATE Reservation
SET RoomNum = 2002
WHERE Name = '홍길동';

DELETE FROM Reservation
WHERE Name = '홍길동'

DELETE FROM 테이블 이름
WHERE 필드이름=데이터값

DELETE FROM Reservation
WHERE Name = '홍길동';

SELECT 필드이름
FROM 테이블이름
[WHERE 조건]

SELECT *
FROM Reservation
WHERE Name = '홍길동';

SELECT *
FROM Reservation
ORDER BY ReserveDate DESC;


SELECT * FROM Reservation
WHERE Name LIKE '장%';


CREATE TABLE Test
(
	ID int NOT NULL,
	Name VARCHAR(30),
	ReserveDate DATE,
	RoomNum INT	
);

CREATE TABLE Test2
(
	ID INT,
  	ParentID INT,
  	FOREIGN KEY (ParentID)
  REFERENCES Test1(ID) ON UPDATE CASCASE
);

CREATE TABLE Test
(
	ID INT,
	Name VARCHAR(30) DEFAULT 'Anonymous',
	ReserveDate DATE,
	RoomNum INT
);

SELECT *
FROM Reservation
INNER JOIN Customer
ON Reservation.Name = Customer.Name;

SELECT *
FROM Reservation
JOIN Customer
ON Reservation.Name = Customer.Name;

SELECT *
FROM Reservation
LEFT JOIN CUSTOMER
ON Reservation.Name = Customer.Name
WHERE ReserveDate > '2016-02-01';

SELECT *
FROM Reservation
RIGHT JOIN Customer
ON Reservation.Name = Customer.Name;
```

