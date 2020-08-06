#태어난 년도를 입력받아 나이를 계산하고, 고딩/대딩 출력 코드

from datetime import datetime as dt
current_Y = dt.today().year

birth_Y = int(input())
age = current_Y - birth_Y +1

if 17 <= age < 20:
    print('Highschool Student')
elif 20 <= age < 27:
    print('Uni Student')
else:
    print('Not Student')
