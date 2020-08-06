import logging # built-in mode logging 소환!

def say_hello(msg):
    return 'Hi ' + msg


#logging 설정
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Start of the Program")
logging.debug(say_hello('Debug Mode'))
logging.info(say_hello('Info Mode'))
logging.debug("End of the Program")
# 2020-07-17 16:05:49,803 - DEBUG - Start of the Program
# 2020-07-17 16:05:49,804 - DEBUG - Hi Debug Mode
# 2020-07-17 16:05:49,804 - INFO - Hi Info Mode
# 2020-07-17 16:05:49,804 - DEBUG - End of the Program
# 이유는 맨위에 level=logging이기때문에.. INFO가 더 상위레벨이라서
# DEBUG로 레벨 설정해도 INFO가 나와. level=logging.INFO 하면 DEBUG 레벨들은 뜨지않어