/*************/
/* select 실습 */
/*************/

-- 1. 고객 테이블에 있는 모든 데이터를 조회하시오 

select * from 고객;
-- 2. 고객 테이블에서 고객번호, 담당자명, 고객회사명, 마일리지, 10% 인상된 마일리지를 조회하시오. 이때 마일리지는 ‘포인트’로, 인상된 마일리지는 ‘10%인상된 마일리지’로 별명을 붙인다.

select 고객번호, 담당자명, 고객회사명, 마일리지 as '포인트' , 마일리지*10 AS "10프로 인상된 마일리지" from 고객; 

--  3. 고객 테이블에서 마일리지가 100,000점 이상인 고객의 고객번호, 담당자명, 마일리지를 조회하시오.

select 고객번호, 담당자명, 마일리지 from 고객 where 마일리지 > 100000;

-- 4. ‘서울특별시’에 사는 고객에 대해 고객번호, 담당자명, 도시, 마일리지를 조회하시오. 이때 마일리지가 많은 고객부터 순서대로 출력한다.

select 고객번호, 담당자명, 도시, 마일리지 from 고객 where 도시 = '서울특별시' order by 마일리지 desc;

-- 5. 마일리지가 많은 고객부터 상위 3명의 고객에 대한 모든 정보를 조회하시오.

select * from 고객 order by 마일리지 desc limit 3;
-- 6. 고객 테이블의 도시 컬럼에 들어있는 값 중 중복되는 도시 데이터를 한 번씩만 보이시오.

select 도시 from 고객 group by 도시;

-- 7. 담당자가 ‘대표 이사’가 아닌 고객의 모든 정보를 보이시오.

select * from 고객 where 담당자명 != '대표이사';

-- 8. 도시가 ‘부산광역시’이면서 마일리지가 1,000점보다 작은 고객의 모든 정보를 보이시오.

select * from 고객 where 도시 = "부산광역시" and 마일리지 > 1000;

-- 9. ‘부산광역시’에 살거나 마일리지가 1,000점보다 작은 고객에 대하여 고객번호, 담당자명, 마일리지, 도시를 보이시오. 이때 결과는 고객번호 순으로 정렬한다.

select 고객번호, 담당자명, 마일리지 ,도시 from 고객  where 도시 = "부산광역시" or 마일리지 > 1000 order by 고객번호;

-- 10. 지역에 값이 들어있지 않는 고객의 정보를 보이시오

select * from 고객 where 지역 = null or 지역 = '';

-- 11. 담당자직위가 ‘영업 과장’이거나 ‘마케팅 과장’인 고객에 대하여 고객번호, 담당자명, 담당자직위를 보이시오.

select 고객번호, 담당자명, 담당자직위 from 고객 where 담당자직위 in("영업 과장", "마케팅 과장");

-- 12. 마일리지가 100,000점 이상 200,000점 이하인 고객에 대해 담당자명, 마일리지를 보이시오.

select 담당자명, 마일리지 from 고객 where 마일리지 between 100000 and 200000;

-- 13. 도시가 ‘광역시’이면서 고객번호 두 번째 글자 또는 세 번째 글자가 ‘C’인 고객의 모든 정보를 보이시오.

select * from 고객 where 도시 like "%광역시"  and 고객번호 like "_C%"  or 고객번호 like "__C%";


/************/
/* 서브쿼리 실습 */
/************/

-- 1. 최고 마일리지를 보유한 고객의 정보를 보이시오.

select * from 고객 where 마일리지 = (select max(마일리지)  from 고객);

-- 2. 주문번호 ‘H0250’을 주문한 고객에 대해 고객회사명과 담당자명을 보이시오.
select * from 주문 where 주문번호 = "H0250";

select 고객회사명, 담당자명 from 고객 where 고객번호 = (select 고객번호 from 주문 where 주문번호 = "H0250");

-- 3. ‘부산광역시’고객의 최소 마일리지보다 더 큰 마일리지를 가진 고객 정보를 보이시오.
select min(마일리지) from 고객 where 도시 = "부산광역시";

select * from 고객 where 마일리지 > (select min(마일리지) from 고객 where 도시 = "부산광역시");
-- 4. ‘부산광역시’ 고객이 주문한 주문건수를 보이시오.


select count(*) as 주문건수 from 주문 where 고객번호 in( select 고객번호 from 고객 where 도시 = "부산광역시");

-- 5. ‘부산광역시’ 전체 고객의 마일리지보다 마일리지가 큰 고객의 정보를 보이시오.

select sum(마일리지) from 고객 where 도시 = "부산광역시";
select * from 고객 where 마일리지 > (select sum(마일리지) from 고객 where 도시 = "부산광역시");
select avg(마일리지) from 고객 group by 지역 ;
-- 6. 각 지역의 어느 평균 마일리지보다도 마일리지가 큰 고객의 정보를 보이시오.
select * from 고객 where 마일리지 > any(select avg(마일리지) from 고객 group by 지역 );
-- 7. 한 번이라도 주문한 적이 있는 고객의 정보를 보이시오.
select distinct 고객번호 from 주문 ;

select * from 고객 where 고객번호 in(select distinct 고객번호 from 주문);
-- 8. 고객 전체의 평균마일리보다 평균마일리지가 큰 도시에 대해 도시명과 도시의 평균마일리지를 보이시오. 
SELECT AVG(마일리지) FROM 고객;
SELECT 도시, AVG(마일리지) AS 평균마일리지 FROM 고객 GROUP BY 도시 HAVING AVG(마일리지) > (SELECT AVG(마일리지) FROM 고객) ;


-- 9. 담당자명, 고객회사명, 마일리지, 도시, 해당 도시의 평균마일리지를 보이시오. 그리고 고객이 위치하는 도시의 평균마일리지와 각 고객의 마일리지 간의 차이도 함께 보이시오.
SELECT 담당자명, 고객회사명, 마일리지, 도시,
  (SELECT AVG(마일리지) FROM 고객 AS sub WHERE sub.도시 = main.도시 ) AS '평균마일리지', 
  (마일리지 - (SELECT AVG(마일리지) FROM 고객 AS sub WHERE sub.도시 = main.도시 ) ) AS '마일리지차이'
FROM 고객 AS main;


-- 10. 고객번호, 담당자명과 고객의 최종 주문일을 보이시오

select 고객번호, max(주문일) from 주문 group by 고객번호;
SELECT
  고객번호,
  담당자명,
  (SELECT MAX(주문일) FROM 주문 wHERE 주문.고객번호 = 고객.고객번호) AS 최종주문일
FROM 고객
WHERE 고객번호 IN (SELECT 고객번호 FROM 주문);


-- 11. 제품 테이블에 있는 제품 중 단가가 가장 높은 제품명은 무엇인가?
select 제품명, max(단가) AS "가장 높은 단가" from 제품 group by 제품명;

-- 12. 제품 테이블에 있는 제품 중 단가가 가장 높은 제품의 주문수량합은 얼마인가?
select sum(주문수량) as '주문수량합' from 주문세부 where 제품번호 = (select 제품번호  from 제품 where 단가 = (select max(단가) from 제품));

-- select 제품번호  from 제품 where 단가 = (select max(단가) from 제품);

SELECT SUM(주문수량) as "단가가 가장 높은 제품의 합" FROM 주문세부 WHERE 제품번호 = (
    SELECT 제품번호
    FROM 제품
    WHERE 단가 = (SELECT MAX(단가) FROM 제품)
);


-- 13. ‘아이스크림’ 제품의 주문수량합은 얼마인가?
select  sum(주문수량) from 주문세부 where 제품번호 in (select 제품번호 from 제품 where 제품명 like  "%아이스크림");
 -- select * from 제품 where 제품명 like  "%아이스크림";

-- 14. ‘서울특별시’ 고객들에 대해 주문년도별 주문건수를 보이시오.

select * from 주문;
SELECT YEAR(주문일) AS 주문년도, COUNT(*) AS 주문건수 FROM 주문
	WHERE 고객번호 IN (SELECT 고객번호 FROM 고객 WHERE 도시 = '서울특별시' )
		GROUP BY 주문년도 ;



