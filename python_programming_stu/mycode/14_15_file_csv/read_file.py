# <연습문제 : 파일 읽어서 전체 글자 수, 전체 단어 수, 전체 라인 수 출력>


# file 읽을 때 모드 미설정시 default 값으로 r(읽어옴)

# 일반적인 방법 -> close 해줘야함 (불편해 - 잘사용안함)
# myfile = open('i_have_a_dream.txt')
# contents = myfile.read()
# print(contents.split())
# myfile.close()

# with 구문 사용
with open('i_have_a_dream.txt', 'r') as my_file:
    contents = my_file.read()
    word_list = contents.split(' ')
    word_num = len(word_list)
    line_list = contents.split('\n')
    line_num = len(line_list)

print('Total number of characters : {}'.format(len(contents)))
print('Total number of words : {}'.format(word_num))
print('Total number of lines : {}'.format(line_num))
