import os
import shutil
# 파일 복사하기
# 파일을 폴더 안으로 복사하기
# shutil.copy("run_btn.png", "11_T_F") # 원본 파일 경로, 대상 폴더 경로
# 원본 파일 경로, 다른 이름으로 복사
# shutil.copy("run_btn.png", "11_T_F/copied_run_btn.png") 

# 원본 파일 경로, 대상파일 경로
# shutil.copyfile("run_btn.png", "11_T_F/copied_run_btn_2.png")

# 원본 파일 경로, 대상 폴더
# shutil.copy2("run_btn.png", "11_T_F/copied2_run_btn.png")

# copy, copyfile : 메타정보 복사 x
# copy2 : 메타정보 복사 ㅇ

# 폴더 복사
# shutil.copytree("11_T_F", "11_T_F2") # 원본 폴더 경로, 대상 폴더 경로
# shutil.copytree("11_T_F", "11_T_F3")

# 폴더 이동
# shutil.move("11_T_F2", "11_T_F3")
# shutil.move("11_T_F3", "11_T_F")
shutil.move("11_T_F", "11_T_F4") # 폴더명 변경효과

