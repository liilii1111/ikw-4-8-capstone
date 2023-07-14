import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import Object_Detection#객체인식
from recog_to_list import to_list#인식 -> 리스트
from file_remove import file_remove#image folder안에, detect파일 지우기
import pymysql
from Add_DB import add_db#db추가 api

#파일 
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print("\n===========================================")
            # 새로운 파일이 생성되었을 때 실행할 코드
            print(f"새로운 파일이 생성되었습니다: {event.src_path}")
            image_path = event.src_path
            image_name = image_path.split("/")[5]
            print("file name : ",image_name)
            print("\n===========================================")
            
            #객체인식
            Object_Detection.detect(image_name)
            
            #인식된거 리스트 형식으로
            result_list=to_list()
            for item in result_list:
                #db추가 
                add_db(item)

            #image folder안에, detect파일 지우기
            file_remove(image_name)

            
if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='/home/ikw/바탕화면/image folder', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
