'''
yesterday.txt 파일을 읽어서
'YESTERDAY', 'yesterday', 'Yesterday'가 몇 번 나오는지 count
'''

#file open
#mode : r(read), w(write), a(append), rb, wb (binary file)
file = open('yesterday.txt', 'r')

#file의 내용을 읽은 값을 저장한 변수
yesterday_lyric = ''

#while 1은 1이 true니까, 저 파일이 열려있는 동안 일을 계속 수행하겠다는 뜻이여
#readline은 한 줄씩 읽겠다는거고
while 1:
    line = file.readline()
    if not line:
        break
    #yesterday_lyric = yesterday_lyric + line.strip() + '\n' 밑에꺼 이렇게 해도 되고
    yesterday_lyric += line
print(yesterday_lyric)

#file읽기 종료
file.close()

print(len(yesterday_lyric))

n_of_YE = yesterday_lyric.upper().count('YESTERDAY')
print('YESTERDAY: ', n_of_YE)
n_of_Ye = yesterday_lyric.count('Yesterday')
print('Yesterday: ', n_of_Ye)
n_of_ye = yesterday_lyric.lower().count('yesterday')
print('yesterday: ', n_of_ye)