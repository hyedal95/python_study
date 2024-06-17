import socket
# 컴퓨터가 연결된 접속정보를 받아올 때 사용하는 모듈을 불러옴
in_addr = socket.gethostbyname(socket.gethostname())
# 연결된 소켓의 이름을 가져와 in_addr 변수와 바인딩한다.
print(in_addr)
# in_addr을 출력하여 내부 IP를 확인한다.

