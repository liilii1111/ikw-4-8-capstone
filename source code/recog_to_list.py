import yaml
import glob

def to_list():
    # coco.yaml 파일을 읽기 모드로 열기
    with open("/home/ikw/dataset/data.yaml", "r") as f:
        data = yaml.safe_load(f)

    # 클래스 이름 리스트 추출
    class_names = data["names"]

    # labels 파일에 있는 .txt 파일 리스트를 생성
    txt_files = glob.glob("/home/ikw/yolov7/runs/detect/exp/labels/*.txt")

    detected_classes = []

    # 각 파일에서 클래스 ID 추출 후 클래스 이름으로 변환하여 detected_classes에 추가
    for txt_file in txt_files:
        with open(txt_file, "r") as f:
            for line in f.readlines():
                class_id = int(line.split()[0])
                class_name = class_names[class_id]
                detected_classes.append(class_name)

    #리스트 반환
    print('\n\n\n')
    return detected_classes
