import requests
import socket
import uuid
requests_log=[]


def local_host():
    localIP = socket.gethostbyname(socket.gethostname())  # 得到本地ip
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    print(localIP,mac)


def requests_index():
    url = 'http://www.eqxiu.com/'
    print(requests.get(url))


local_host()