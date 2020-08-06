# # mode를 설정하지 않으면 디폴트가 r(read)
#
# myfile = open('i_have_a_dream.txt')
# speech = myfile.read()
# print(speech)
# myfile.close()
#
# # 열었으면 반드시 닫아야하기땜시 굳이 open안하는경우가 많지용 close쓰기 귀찮

# with 구문 사용

with open('i_have_a_dream.txt', 'r') as my_file:
    speech = my_file.read()
    word_list = speech.split(' ') # 이렇게 split한걸 전부 list에 파바박 넣어준다 이거야
    line_list = speech.split('\n') # 줄마다 자른걸 (이하 생략)
print('Characters:', len(speech))
print('Words:', len(word_list))
print('Lines:', len(line_list))