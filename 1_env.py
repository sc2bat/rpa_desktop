# 환경설정
# pip install pyautogui

import pyautogui

size = pyautogui.size() # 현재 화면의 스크린 사이즈를 가져옴
print(size) # 가로, 세로 크기 확인
# size[0] : width
# size[1] : height
# 이미지기반으로 자동화