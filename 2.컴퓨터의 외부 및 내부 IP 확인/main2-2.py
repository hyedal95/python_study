import socket
# 컴퓨터가 연결된 접속정보를 받아올 때 사용하는 모듈을 불러옴
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr",443))
# 소켓을 연결하여 www.google.co.kr에 접속한다. https의 기본 접속 포트는 443이다.
print(in_addr)
# 연결된 소켓의 이름을 출력

