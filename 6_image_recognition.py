# 화면내에서 특정 이미지 
# 화면 해상도 약간만 틀어져도 안될 경우 존재
# from PIL.ImageOps import grayscale
import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 1. GrayScale 흑백화 시켜 속도개선
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위를 지정해 속도개선
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1188,837,1912-1188,943-837))
# pyautogui.moveTo(trash_icon)
# pyautogui.mouseInfo()
# 1188,837 30,30,30 #1E1E1E
# 1912,943 30,30,30 #1E1E1E

# 3. 정확도 조절
# pip install opencv-python
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9)
# pyautogui.moveTo(run_btn)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=1)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# 1. 자동화 대상이 바로 보여지지 않는 경우
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
# #     print("False")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("False")

# pyautogui.click(file_menu_notepad)

# 2. 일정시간만 대기 TimeOut
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정

# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초 초과시
#         print("TimeOut") 
        # sys.exit()
def find_target(img_file, timeout=30):
    start = time.time() 
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s ] Target not found ({img_file}).Terminate program.")
        sys.exit()

# pyautogui.click(file_menu_notepad)

my_click("file_menu_notepad.png", 10)