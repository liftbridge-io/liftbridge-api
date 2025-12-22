package proto

import (
	"testing"

	"google.golang.org/protobuf/proto"
)

func TestSubscribeRequestReverse(t *testing.T) {
	req := &SubscribeRequest{
		Stream:    "test-stream",
		Partition: 0,
		Reverse:   true,
	}

	if !req.GetReverse() {
		t.Error("expected Reverse to be true")
	}

	// Test proto marshaling
	data, err := proto.Marshal(req)
	if err != nil {
		t.Fatalf("failed to marshal: %v", err)
	}

	req2 := &SubscribeRequest{}
	if err := proto.Unmarshal(data, req2); err != nil {
		t.Fatalf("failed to unmarshal: %v", err)
	}

	if !req2.GetReverse() {
		t.Error("expected unmarshaled Reverse to be true")
	}

	if req2.GetStream() != "test-stream" {
		t.Errorf("expected stream 'test-stream', got %q", req2.GetStream())
	}
}

func TestSubscribeRequestReverseDefault(t *testing.T) {
	req := &SubscribeRequest{
		Stream:    "test-stream",
		Partition: 0,
	}

	if req.GetReverse() {
		t.Error("expected Reverse to be false by default")
	}
}

func TestMessageFields(t *testing.T) {
	msg := &Message{
		Offset:    100,
		Key:       []byte("key"),
		Value:     []byte("value"),
		Stream:    "test-stream",
		Partition: 0,
	}

	if msg.GetOffset() != 100 {
		t.Errorf("expected offset 100, got %d", msg.GetOffset())
	}
}
