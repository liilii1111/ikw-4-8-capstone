# 경운대학교 4학년 8조 캡스톤 소스코드

<div align="center">
    <a href="./">
        <img src="./ikw.png" width="40%"/>
    </a>
</div>

## [main]recognition_file.py
- 메인소스 코드로서 코드 실행시 while 문으로 계속해서 실행되면서 "image folder"라는 폴더에 파일이 들어오면 인식해서 객체인식을 진행하게 해주는 코드입니다.

## firebase_get_file.py
- 앱에서 찍은 사진들이 모두 firebase 안에 들어오게 되는데, python 에서 firebase를 연동하여 안의 사진들이 들어오게 되면 while문으로 계속 확인을 하면서 파일을 가져올수있게 하는 코드입니다.

## file_remove.py
- "image folder" 안의 사진이 들어오면 메인 코드에서 객체 인식을 진행하고 fire_remove를 진행하여서 관련된 파일들을 모두 지우게 돼서, 객체 인식 PC의 용량 관리를 용이하게 해줍니다. 그리고 메인에서 파일 인식을 위한 로직이 현재 폴더 안 파일의 개수로 판단을 하므로 파일들을 지워줘야 프로그램이 잘 작동하게 됩니다.

## recog_to_list.py
- 메인에서 객체 인식을 진행한 뒤 0,1,2 같은 인덱스로 인식된 객체를 판별하는데 이를 한글로 DB에 저장하기 위해 class를 지정해 두었던 "data.yaml" 안의 파일에 "names" 리스트를 추출하고 인덱스를 대조하여 어떤 객체 인식 판별하게 됩니다. 그러면 양파면 양파 감자면 감자와 같이 어떤 객체가 인식되었는지 알 수 있습니다.

## Add_DB.py
- "recog_to_list.py" 에서 추출한 class 이름들을 Add_DB.py 를 이용해 DB에 저장하게 됩니다. 이는 미리 만들어 두었던 API를 사용하여 추가하게 됩니다.

## Object_Detection.py
- 메인에서 "image folder" 안의 파일이 들어오면 객체 인식을 실행할 수 있게 하는 코드입니다.



## 학습
``` shell
!python train.py --device 0 --epochs 140 --batch-size 4 --data /home/ikw/dataset/data.yaml --img 640 --cfg cfg/training/yolov7.yaml --weights /home/ikw/yolov7/yolov7.pt --name [real]train[1] --hyp data/hyp.scratch.p5.yaml
```

## 테스트
``` shell
!python detect.py --weights best.pt --img 640 --source '/home/ikw/바탕화면/123.png' --save-txt 
```
