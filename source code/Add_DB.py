import requests
import json

def add_db(item):
    url = "http://52.79.146.120:8080/fridge-items/post"
    headers = {'Content-Type': 'application/json'}

    # item을 JSON 형태로 변환합니다.
    data = json.dumps({"name": item})
    
    #json형태와 main 에서 받은 item을 data형식으로 바꿔서 url로 post 방식으로 전송합니다.
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        print(f'재료 추가 성공: {item}')
    else:
        print(f'재료 추가 실패: {item}. Response: {response.text}')
