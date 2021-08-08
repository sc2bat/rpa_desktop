import pyautogui
# # 스샷
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 985,15 57,167,242 #39A7F2

# 해당하는 픽셀의 RGB값
pixel = pyautogui.pixel(985, 15)
print(pixel)

# print(pyautogui.pixelMatchesColor(985, 15, (57,167,242)))
# print(pyautogui.pixelMatchesColor(985, 15, pixel))
# print(pyautogui.pixelMatchesColor(985, 15, (57,167,243)))
