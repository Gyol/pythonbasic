# 1. log 디렉토리가 없으면 log 디렉토리를 생성한다.
# 2. log 디렉토리가 있지만, log/count_log.txt 파일이 없으면 파일을 생성합니다.
# 3. log/count_log.txt 을 append mode 로 파일을 open 한다.
# 4. random 과 datetime 모듈을 import 한다.
# 5. range(1,11) 함수를 사용하여 for loop 돌면서
#     현재시간(timestamp)을 string으로 변환하여 stamp 에 저장한다.
#     랜덤한 값에 100000 곱해서 value에 저장한다.
#     stamp와 value를 파일에 wirte() 한다.

import os
if not os.path.isdir('log'):
    os.mkdir('log')

if not os.path.isfile('log/count_log.txt'):
    open('count_log.txt', 'w', encoding='utf8')

time = open('count_log.txt', 'a', encoding='utf8')
import random
from datetime import datetime
r = random.randint()
for i in range(1, 11):
    datetime.now()
    stamp = f'{i}년 {i}월 {i}일 {i}분 {i}초 입니다.'
    value = r * 100000
