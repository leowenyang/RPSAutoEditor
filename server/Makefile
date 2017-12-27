stubs:
	python -m grpc.tools.protoc -I/usr/local/include -I. --python_out=./ --grpc_python_out=./ wxrpcauth.proto

client:
	python client.py

server:
	python server.py

gen_key:
	openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt

python -m grpc.tools.protoc -I/usr/local/include -IE:\work\创业之路\音视频技术\并行计算\自动化剪辑\server --python_out=E:\work\创业之路\音视频技术\并行计算\自动化剪辑\server\ --grpc_python_out=E:\work\创业之路\音视频技术\并行计算\自动化剪辑\server\ wxrpcauth.proto