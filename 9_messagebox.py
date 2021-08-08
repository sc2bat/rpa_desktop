import pyautogui
# print("I'll be done")
# pyautogui.countdown(3)
# print("start")

# pyautogui.alert("fail", "warning") # 확인 버튼만 있는 팝업
# result = pyautogui.confirm("continue?", "confirm") # 확인 취소
# print(result)

# result = pyautogui.prompt("file_name confirm", "input") # 사용자 입력
# print(result)

result = pyautogui.password("password")
print(result)