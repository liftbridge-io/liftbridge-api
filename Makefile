PROJECT := liftbridge-api

BUF_VERSION := 1.47.2

UNAME_OS := $(shell uname -s)
UNAME_ARCH := $(shell uname -m)
CACHE_BASE := $(HOME)/.cache/$(PROJECT)
CACHE := $(CACHE_BASE)/$(UNAME_OS)/$(UNAME_ARCH)
CACHE_BIN := $(CACHE)/bin
CACHE_VERSIONS := $(CACHE)/versions

export PATH := $(abspath $(CACHE_BIN)):$(PATH)

BUF := $(CACHE_VERSIONS)/buf/$(BUF_VERSION)
$(BUF):
	@rm -f $(CACHE_BIN)/buf
	@mkdir -p $(CACHE_BIN)
	curl -sSL \
		"https://github.com/bufbuild/buf/releases/download/v$(BUF_VERSION)/buf-$(UNAME_OS)-$(UNAME_ARCH)" \
		-o "$(CACHE_BIN)/buf"
	chmod +x "$(CACHE_BIN)/buf"
	@rm -rf $(dir $(BUF))
	@mkdir -p $(dir $(BUF))
	@touch $(BUF)

.PHONY: all
all: go py

.PHONY: go
go:
	protoc --go_out=go --go_opt=paths=source_relative \
	       --go-grpc_out=go --go-grpc_opt=paths=source_relative \
	       api.proto

.PHONY: py
py:
	python -m grpc_tools.protoc -I. --python_out=py --grpc_python_out=py api.proto

.PHONY: check
check: $(BUF)
	buf lint
	buf breaking --against '.git#branch=master'

.PHONY: install-tools
install-tools:
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
