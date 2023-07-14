import os
import shutil

def file_remove(image_name):
    folder_path1 = "/home/ikw/바탕화면/image folder"
    folder_path2 = "/home/ikw/yolov7/runs/detect"

    # image folder 경로에 있는 파일 중 특정 파일 삭제하기
    if os.path.exists(os.path.join(folder_path1, image_name)):
        os.remove(os.path.join(folder_path1, image_name))

    # detect 경로 지우기
    if os.path.exists(folder_path2):
        shutil.rmtree(folder_path2)

    print(f'\n\n\n파일 제거 완료 \n--------------\n{folder_path1}/{image_name}\n{folder_path2}\n--------------\n\n\n')
