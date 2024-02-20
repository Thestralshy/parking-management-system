import socket

s = socket.socket()

s.bind(("0.0.0.0",8888))

s.listen(5)
# 接收 TCP 数据
# s.recv()
# 发送 TCP 数据
s.send()
