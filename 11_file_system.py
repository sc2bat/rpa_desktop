# 파일 기본
import os
# print(os.getcwd()) # current working directory 현재 작업 공간
# # os.chdir("RPA")
# # print(os.getcwd())
# os.chdir("..") # 부모폴더
# print(os.getcwd())
# os.chdir("../..") # 조부모폴더
# print(os.getcwd())

# os.chdir("c:/") # 주어진 경로로 이동
# print(os.getcwd())

# 파일 경로
# open("파일경로") as f ....
# file_path = os.path.join(os.getcwd(), "t_file11.txt")
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"C:\Users\Dero\Desktop\p\RPA\2_desktop\t_file11.txt"))

# 파일 정보 가져오기
import time
import datetime

file_path = "run_btn.png"
# 파일의 생성 날짜
ctime = os.path.getctime(file_path)
print(ctime)
# 날짜 정보를  strftime 년월일 시분초 형태로 출력
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# 파일 수정 날짜
mtime = os.path.getmtime(file_path)
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 마지막 접근 날짜
atime = os.path.getatime(file_path)
print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 파일 크기
size = os.path.getsize(file_path)
print(size) # byte 단위로 가져옴