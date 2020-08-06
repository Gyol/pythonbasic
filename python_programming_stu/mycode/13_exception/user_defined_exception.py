# 사용자 정의 Exception class
# 음수값이 입력되었을 때 강제로 예외 발생시키기
# 일반 class만들때는 괄호에 object넣었는데 exception은 Exception넣어야돼 규칙이여
class NegativePriceException(Exception):
    def __init__(self):
        print('do not input Negative numbers')
        raise AttributeError

def calc_price(value):
    price = value * 52
    if price < 0:
        raise NegativePriceException
    return price

print(calc_price(55))
print(calc_price(-45))