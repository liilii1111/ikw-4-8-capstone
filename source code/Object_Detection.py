import os
import subprocess

#객체인식
def detect(image_name):
    os.chdir('/home/ikw/yolov7/')
    #서브 프로세스 로 객체인식 실행하기.
    subprocess.call(['python', 'detect.py', '--weights', 'best.pt', '--source', f'/home/ikw/바탕화면/image folder/{image_name}', '--save-txt','--conf','0.5'])

if __name__ == "__main__":
    detect()