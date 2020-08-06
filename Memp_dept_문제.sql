select * from emp;
#emp : 사원번호,이름,업무,관리자번호,입사일자,급여,커미션,부서번호
select * from dept;
#dept : 부서번호,부서명,도시명
select * from salgrade;
#salgrade : 등급,최저급여,최고급여

# 1. EMP TABLE 에서 이름, 급여, 커미션 금액, 총액 (SAL + COMM) 을 구하여
# 총액이 많은 순서로 출력하라. 
# 단 커미션이 NULL인 사람은 제외한다.
select ename, job, hiredate, (sal + comm)
from emp where comm is not null
order by (sal + comm)
desc;


# 2. EMP와 DEPT TABLE 을 JOIN 하여 부서번호, 부서명, 이름, 급여를 출력하라.
select ename, job, e.deptno, dname, sal
from emp as e join dept as d
where e.deptno = d.deptno
order by sal
desc ;

# Ansi SQL(표준 SQL)
# ECMA가 자바스크립트 표준..?


# 3. EMP 테이블에서 사원번호가 7521인 사원과 업무가 같고, 급여가 7934인 사원보다 많은 사원의
# 사원번호, 이름, 담당업무, 입사일자, 급여를 출력하여라.
select empno, ename, job, hiredate, sal
from emp
where job = (select job from emp where empno = 7521)
    and sal > (select sal from emp where empno = 7934)
order by (sal + comm)
desc ;


# 4. EMP 테이블에서 평균급여보다 적은 급여를 받는 사원의
# 사원번호, 이름, 담당업무, 급여, 부서번호를 출력하라.
select empno, ename, job, sal, deptno
from emp
where sal < (select avg(sal) from emp)
order by sal
desc;


# 5. EMP TABLE 에 있는 EMPNO와 MGR을 이용하여 서로의 관계를 다음과 같이 출력하라.
# SMTH의 매니저는 FORD이다.
# || (oracle), concat(mysql)
# 5.1 (self query) 같은 emp 테이블 2개를 조인합니다.

#     1차시기
    # select
    #     concat(employee, '의 매니저는', manager, '이다.')
    # from emp e, (select ename as employee from emp where empno) d
    # where

#     2차시기
    # select concat(employee, '의 매니저는', manager, '이다.')
    # from emp
    # where ename

#     강사님 버전
select * from emp;
select concat(e.ename, '의 매니저는 ', m.ename, '이다.') as 상하관계
    from emp e, emp m
where m.empno = e.mgr;

# 5.2 inline view
select concat(e.ename, '의 매니저는 ', m.ename, '이다.') as 상하관계
    from emp e, (select * from emp) m
where e.mgr = m.empno;

# 6. ALLEN의 직무와 같은 사람의 이름, 부서명, 급여, 직무를 출력하라.
# 단일행, column query?
select job
from emp
where ename = 'ALLEN';

select ename, dname, sal, job
from

#7. EMP 테이블에서 SALES 부서 사원의 이름,업무, 부서번호를 출력하는 SELECT문을 작성하시오.
#7.1 Nested Query
select ename, job, deptno
from emp
where deptno = (select deptno from dept where dname = 'SALES');

#7.2 Inline View
select e.ename, e.job, e.deptno, d.dname
    from emp e, (select deptno, dname from dept where dname = 'SALES')d
where e.deptno = d.deptno;


# 8. EMP 테이블에서 이름에 “T”가 있는 사원이 근무하는 부서에서 근무하는 모든 사원에 대해
# 사원 번호,이름,급여를 출력하는 SELECT문을 작성하시오.
# 단 사원번호 순으로 출력하여라.



# 9. 전체 사원의 평균 임금보다 많은 사원의 사원번호, 이름, 부서명, 입사일, 지역, 급여를 출력하라.
# where 단일행 subquery


# 10. EMP 테이블에서 관리자중에서 부하직원을 2명이상 관리하는 관리자의 이름을 출력하세요.
# 10.1 Nested Query (where 절에 subquery)
# 관리자 사번을 먼저 count로 출력하면 되지 않을까?

# select mgr, count(*) from emp group by mgr;
# 여기서 group by를 안주면 안되는 이유가 mgr은 단일객체라서...? 띠용 모르겠군


# 10.2 Inline View (from 절에 subquery)



# 11.EMP 테이블에서 CHICAGO에서 근무하는 사원과 같은 업무를 하는 사원의 이름,업무를 출력하는 SELECT문을 작성하시오.

select distinct job from emp join dept
where loc != 'CHICAGO';
select distinct job as cjob from emp join dept
where loc = 'CHICAGO'

# 11.1 Nested Query ( where 절에 in 구문에  subquery 대입 )



# 11.2 Inline View




# 12.EMP 테이블에서 업무가 JONES와 같거나 월급이 FORD이상인 사원의 이름,업무,부서번호,급여를 출력하는 SELECT문을 작성하시오.
# 단 업무별, 월급이 많은 순으로 출력하여라.




# 13. EMP 테이블에서 업무별로 최소 급여를 받는 사원의 사원번호, 이름, 업무, 입사일자, 급여, 부서번호를 출력하여라.




# 14. emp와 dept 테이블에서 업무가 manager인 사원의 이름, 업무, 부서명, 근무지를 출력하여라.
# Inline View 를 사용하자





# 15. EMP 테이블에서 30번 부서원 중 최저급여를 받는 사원을 제외한
# 나머지 사원들의 모든 정보를 출력하는 SELECT문을 작성하시오.




# 16. EMP 테이블에서 말단 사원의 사원번호,이름,업무,부서번호를 출력하는 SELECT문을
# 작성하시오.(말단사원: 다른 사원을 관리하지 않는 사원)
# - ORACLE : NVL(VALUE1, VALUE2)
# - MSSQL  : ISNULL(VALUE1, VALUE2)
# - MYSQL  : IFNULL(VALUE1, VALUE2) # NULL이 아니면 1, NULL이면 2값 출력
SELECT DISTINCT(IFNULL(mgr,0)) FROM emp;
# in 구문은 null값을 비교하지 못한다!


# 17. EMP 테이블에서 사원번호, 이름, 업무, 급여, 급여의 등급을 출력하되
# 3등급 이상인 사원의 정보만을 출력하세요.
# (emp와 salgrade 테이블을 이용);



# 18. 부서번호, 부서에 속한 직원수, 부서명, 도시명을 출력하세요.
# 직원수가 5명이상인 부서만 출력하세요. ( inline view )

# select distinct emp.deptno, count(*) as cnt, dname, loc
# from emp join dept
# group by dname
# having cnt >= 5;




# 19. EMP 테이블에서 30번 부서원 중 최저급여를 받는 사원을 제외한
# 나머지 사원들의 모든 정보를 출력하는 SELECT문을 작성하시오.





# 20. EMP 테이블에서 적어도 한 명 이상으로부터 보고를 받을 수 있는 사원의
# 업무,이름,사원번호,부서번호를 출력하시오.
# (즉 다른 사원의 관리자를 출력하세요)


