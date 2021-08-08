import os

# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더 파일 목록 가져오기
# print(os.listdir("경로")) # 주어진 폴더의 모든 폴더, 파일 목록

# 하위 폴더 포함 파일 목록 가져오기
# result = os.walk(".") # 주어진 폴더 밑에 있는 모든 폴더, 파일 가져옴
# print(result)

# for root, dirs, files in result:
    # print(root, dirs, files)

# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)

# 폴더 내 특정 패턴을 가진 파일 차기
# *.xlsx, *.txt 등등
import fnmatch
pattern = "*.py"
result = []
for root, dirs, files in os.walk("."):
    for name in files:
        if fnmatch.fnmatch(name, pattern): # 이름과 패턴 일치시
            result.append(os.path.join(root,name))

print(result)

