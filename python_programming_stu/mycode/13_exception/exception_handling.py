# try - except - else
# try - except - finally

for i in range(10):
    try:
        result = float(10 / i)
    except ZeroDivisionError as err:
        # 하는데 이거 뭔 에러인지 모르겠으면 걍 zero머시기 말고 Exception으로 퉁쳐
        # built-in exception에도 hierarchy가 있어서... 그냥 Exception이 제일 상위고
        # 저거 해도 결과창에 에러는 똑같이 뜨는데 같이 코딩할 때 가독성이 문제라
        # 편하긴 한데 여럿이 일할때는 아무래도 비추하긴 하는가봄
        print(err)
    else:
        print(result)
    finally:
        print('Fin.')