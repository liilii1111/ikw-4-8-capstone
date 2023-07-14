import firebase_admin
from firebase_admin import credentials, storage
import time
#파일 다운로드 현황을 위한 loggin 라이브러리
import logging

#logging config
logging.basicConfig(level=logging.INFO)

#인증서 초기화
def initialize_firebase():
    #firebase 인증서불러오기
    cred = credentials.Certificate('/home/ikw/chat-chef-1144a-firebase-adminsdk-b1gkh-7e46169d71.json')
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'chat-chef-1144a.appspot.com' 
        })
        
#다운로드와 삭제 현황을 콘솔에 알려주는 기능
def download_and_delete_blob(bucket, blob):
    try:
        blob.download_to_filename(f"/home/ikw/바탕화면/image folder/{blob.name}")  # blob을 다운로드
        logging.info(f"Downloaded blob {blob.name}")
        blob.delete()  # blob을 삭제
        logging.info(f"Deleted blob {blob.name}")
    except Exception as e:
        logging.error(f"Failed to process blob {blob.name}: {e}")

def main():
    initialize_firebase()
    bucket = storage.bucket()

    while True:#반복하면서 firebase안의 파일 인식
        blobs = bucket.list_blobs()
        blob_list = [blob for blob in blobs]  # blob 리스트 생성

        if len(blob_list) > 0:  # firebase 안의 파일이 하나라도 들어오면 다운로드 하고 삭제하기.
            download_and_delete_blob(bucket, blob_list[0])

if __name__ == "__main__":
    main()
