import logging

def say_Hello(msg):
    return 'Hello ' + msg

# logger 생성
root_logger = logging.getLogger()
# log level 설정
root_logger.setLevel(logging.DEBUG)
# logger file Handler 생성
fileHandler = logging.FileHandler('test.log', 'w', 'utf-8')
# logger console Handler 생성
streamHandler = logging.StreamHandler()
# 그니까 저 logging을 file에 출력할거냐고 console에 출력할거냐고 그냥 그거일뿐이여



formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s')
# lineno 저거 말 그대로 몇번라인에서 찍은거냐고

streamHandler.setFormatter(formatter)
fileHandler.setFormatter(file_formatter)

# logger 객체에 file handler와 stream handler를 등록
root_logger.addHandler(fileHandler)
root_logger.addHandler(streamHandler)

root_logger.debug('Start of the Program')
root_logger.debug(say_Hello('Debug Mode'))
root_logger.info(say_Hello('Info Mode'))
root_logger.debug('End of the Program')
# root_logger.warn(say_Hello('Warn Mode'))
#root_logger.error(say_Hello('Error Mode'))
