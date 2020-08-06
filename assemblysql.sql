# alter table members change 생년월일 생년월일 DATE null;

# 1. 나이 순으로 desc id, 이름, 나이, 정당
select 이름, 나이, 정당
from assembly
order by 나이
desc;

# 2. 나이가 68 - 80 id, 이름, 나이, 정당, 취미특기
select 이름, 나이, 정당, 취미특기
from assembly
where 나이 >= 68
    and 나이 <= 80
order by 나이
desc;

# 2-1. 나이가 20 - 40 id, 이름, 나이, 정당, 취미특기
select 이름, 나이, 정당, 취미특기
from assembly
where 나이 >= 20
    and 나이 <= 40
order by 나이
desc;

# 3. 취미특기가 없는 사람
select 이름, 나이, 정당
from assembly
where 취미특기 = ''
order by 나이
desc;


# 3-1. 취미특기가 없는 사람의 취미특기 column값을 '없음'으로 update
update assembly set 취미특기 = '없음' where 취미특기 = '';
select * from assembly;

# 4. 이름 홍길동 -> 홍 substring
select substr(이름, 1, 1) as sung
from assembly
order by 이름
asc;

# 4-1. 성씨별로 count ex) 김 10
select substr(이름, 1, 1), count(substr(이름, 1, 1))
from assembly group by substr(이름, 1, 1)
order by count(substr(이름, 1, 1))
desc;

# 5. 소속위원회 문자열 중 '보건복지' 문자열이 포함된 member 가져오기
select * from assembly
where 소속위원회 like '%보건복지%';

# 5-1. 소속위원회 문자열 중 '보건복지'이거나 '법제사법'문자열이 포함된 sort 소속위원회 asc
select * from assembly
where 소속위원회 like '%보건복지%'
    or 소속위원회 like '%법제사법%';

# 6. 비서가 4명인 사람
# length() 함수 사용
# subquery 사용 - 2개의 query 사용




# 7. 더불어민주당, 초선, 경기 member
select 이름, 나이, 소속위원회 from assembly
where 정당 like '더불어민주당'
    and 당선횟수 like '초선'
    and 선거구 like '경기'
order by 나이
desc;

# 7-1. 미래통합당, 초선, 경기 member
select 이름, 나이, 소속위원회 from assembly
where 정당 like '미래통합당'
    and 당선횟수 like '초선'
    and 선거구 like '경기'
order by 나이
desc;

# 7-2. 정당별 초선, 경기 member
select 이름, 나이, 정당 from assembly
where 당선횟수 like '초선'
    and 선거구 like '경기'
order by 정당
asc;
