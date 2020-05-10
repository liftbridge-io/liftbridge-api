.PHONY: all
all: go py

.PHONY: go
go:
	protoc -I. \
		--gofast_out=\
Mgoogle/protobuf/duration.proto=github.com/gogo/protobuf/types,\
plugins=grpc:go api.proto

.PHONY: py
py:
	python -m grpc_tools.protoc -I. --python_out=py --grpc_python_out=py api.proto
