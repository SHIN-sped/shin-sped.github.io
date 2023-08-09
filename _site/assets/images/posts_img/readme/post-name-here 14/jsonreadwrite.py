import json

# JSON 파일을 읽는 방법
with open("class.json", "r") as f:
    data = json.load(f)
print(data)
# JSON 파일을 쓰는 방법
# with open("class_1.json", "w") as f:
#     json.dump(data, f)
# 추가적인 공부 필요