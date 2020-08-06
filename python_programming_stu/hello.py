import sys # 왜 얘가 필요한가?
import logging

def say_hello(msg):
    return 'Hello and ' + msg

def main():
    print(sys.argv[0])
    msg = sys.argv[1]
    print(msg)
    if msg is None:
        print('enter msg')
    else:
        print(say_hello(msg))

# def main():
#     print(say_hello('fuck off'))

# keyword중에 언더바가 두개 붙으면 뭔가 예약된 거라고 했따..
if __name__ == '__main__':
    print('직접 실행')
    main()
else:
    print('import 되어 실행')
# (venv) D:\Python_MC\mypython\python_programming_stu>python hello.py
# 직접 실행
# Hello and fuck off
#
# (venv) D:\Python_MC\mypython\python_programming_stu>python
# Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from hello import say_hello
# import 되어 실행
# >>> say_hello('aaa')
# 'Hello and aaa'

# import os
# os.getcwd
# os.chdir('c:') 그 cmd에서 cd c 하는것처럼 이 파이썬 여기서도 할 수 있다규용
# os.chdir('c:\\windows\\system32')

# path = 'c:\\windows\\system32\\calc.exe'
# os.getcwd()
# 'c:\\windows\\system32'
# os.path.basename(path)
# 'calc.exe'
# os.path.dirname(path)
# 'c:\\windows\\system32'

# logging module 알아두셔야..합니다

# terminal - pip install pandas.. 하면 numpy도 설치되고 pip show ~ 하면 설치유무
# c에 python37에 lib는 라이브러리인데 머 json도 있고.. 모듈들 있어 scripts보면 깔린것들
# C:\\python37\lib\logging 보면 __init__있는디 얘는 파이썬안에서 제공되는 built-in module이라
# 암튼 저 경로에는 built-in모듈들 있다는거야
# lib\site-packages 는 써드파티? 우리가 따로 설치한 pandas numpy flake8 등 써드파티