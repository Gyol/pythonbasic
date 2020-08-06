# readline() 함수 사용
with open('i_have_a_dream.txt', 'r') as my_file:
    # line number
    i = 0
    while True:
        line = my_file.readline()
        if line.strip() != "": # 아무것도 없는 빈 줄 표현 왜냐면 저 파일 줄마다 한줄 비워서
            print(str(i) + ' - ' + line.strip())
        if not line:
            break
        i = i + 1
    print(f'There are {i - 1} lines')