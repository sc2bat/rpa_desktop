import os

# 주어진 경로가 파일 or 폴더
# print(os.path.isdir("2_desktop"))
# print(os.path.isfile("7_window.py"))

# 폴더나 파일이 없다면 False
# print(os.path.isfile("dow.py"))

# # 주어진 경로가 존재하는지
# if os.path.exists("2_desktop"):
#     print("True")
# else:
#     print("False")

# 파일 만들기
# open("11_file_test.txt", "a").close() # 빈 파일 생성

# 파일명 변경
# os.rename("11_file_test.txt", "11_renamefile_test.txt")

# 파일 삭제
# os.remove("11_renamefile_test.txt")

# 폴더 만들기
# os.mkdir("11_T_F") # 현재 디렉 기준 
# os.mkdir("절대경로 가능")
# 하위폴더를 가지는 폴더 만들기
# os.makedirs("11_T_F/a/b/c")

# 폴더명 변경
# os.rename("11_T_F", "11_RN_f")

# 폴더 지우기
# os.rmdir("11_RN_f") # 빈폴더일 경우에만 삭제가능

# import shutil # shell utilities
# shutil.rmtree("11_RN_f") # 빈폴더가 아니라도 삭제