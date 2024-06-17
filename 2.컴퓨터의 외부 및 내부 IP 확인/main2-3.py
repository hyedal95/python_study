import requests
# 사이트에 접속하기 위한 requests 모듈 불러오기
import re
# ip주소 찾기 위한 정규식 사용을 위한 re 모듈 불러오기
req = requests.get("http://ipconfig.kr")
# 사이트 접속
out_addr = re.search(r'IP Address: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
# 정규식 표현을 사용하여 ip 주소를 가져와 out_addr 변수와 바인딩한다.
print(out_addr)
# 외부 ip주소를 출력한다.
