TEXT = open('count_log.txt', 'w', encoding='utf8')
for i in range(1, 11):
    data = '%d번째 줄 입니다. \n' %i
    TEXT.write(data)
TEXT.close()

with open('count_log.txt', 'a', encoding= 'utf8') as f:
    for i in range(100, 111):
        data = '%d 번째 줄입니다. \n' %i
        f.write(data)

# with open('count_log.txt', 'w', encoding= 'utf8') as f:
#     for i in range(100, 111):
#         data = '%d 번째 줄입니다. \n' %i
#         f.write(data)
# 이렇게 하면 위에 write한 count_log.txt 위에 덮어씌워져
# a를 써서 내용이 추가된거임


import os
# log 디렉토리가 없으면 생성하자구
if not os.path.isdir('log'):
    os.mkdir('log')

with open('count_log.txt', 'a', encoding= 'utf8') as f:
    for i in range(200, 210):
        data = '%d번째 줄입니다. \n' %i
        f.write(data)

# import datetime
# datetime.datetime.now()
# datetime.datetime(2020, 7, 17, 17, 43, 8, 140819)
# 이거는 datetime이라는 클래스를 먼저 불러오고
# datetime이라는 모듈 부르고 함수 호출하고...

# 위랑 밑이랑 결과는 같아 근데 그냥 머 이렇게 쓸수있다고 편하니까 더 많이쓰지
# from datetime import datetime <- 이게 함수여
# datetime.now()
# datetime.datetime(2020, 7, 17, 17, 43, 34, 179815)