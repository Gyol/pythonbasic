print('변환하고 싶은 섭씨 온도를 입력해 주세요: ')
temperature = int(input())
fah = (((9/5)*temperature)+32)
print(temperature)
print('섭씨온도: ', temperature)
print('화씨온도: ', fah)
print('화씨온도 = {:.2f}'.format(fah))

