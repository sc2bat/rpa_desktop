# import logging

# logging.basicConfig(level=logging.DEBUG, format= "%(asctime)s [%(levelname)s] %(message)s")
# # 레벨 순서 debug < info < warning < error < critical

# logging.debug("What's wrong with you")
# logging.info("ready to work")
# logging.warning("Do not buy T")
# logging.error("Error")
# logging.critical("Warning! Warning!")

# 터미널과 파일로 로그 남기기
import logging
from datetime import datetime
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
# 시간 로그레벨 메세지 형태로 로그 작성
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("TEST_log")