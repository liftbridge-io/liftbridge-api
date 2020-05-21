# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import api_pb2 as api__pb2


class APIStub(object):
    """API is the main Liftbridge server interface clients interact with.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateStream = channel.unary_unary(
                '/proto.API/CreateStream',
                request_serializer=api__pb2.CreateStreamRequest.SerializeToString,
                response_deserializer=api__pb2.CreateStreamResponse.FromString,
                )
        self.DeleteStream = channel.unary_unary(
                '/proto.API/DeleteStream',
                request_serializer=api__pb2.DeleteStreamRequest.SerializeToString,
                response_deserializer=api__pb2.DeleteStreamResponse.FromString,
                )
        self.PauseStream = channel.unary_unary(
                '/proto.API/PauseStream',
                request_serializer=api__pb2.PauseStreamRequest.SerializeToString,
                response_deserializer=api__pb2.PauseStreamResponse.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/proto.API/Subscribe',
                request_serializer=api__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=api__pb2.Message.FromString,
                )
        self.FetchMetadata = channel.unary_unary(
                '/proto.API/FetchMetadata',
                request_serializer=api__pb2.FetchMetadataRequest.SerializeToString,
                response_deserializer=api__pb2.FetchMetadataResponse.FromString,
                )
        self.Publish = channel.unary_unary(
                '/proto.API/Publish',
                request_serializer=api__pb2.PublishRequest.SerializeToString,
                response_deserializer=api__pb2.PublishResponse.FromString,
                )
        self.PublishAsync = channel.stream_stream(
                '/proto.API/PublishAsync',
                request_serializer=api__pb2.PublishRequest.SerializeToString,
                response_deserializer=api__pb2.PublishResponse.FromString,
                )
        self.PublishToSubject = channel.unary_unary(
                '/proto.API/PublishToSubject',
                request_serializer=api__pb2.PublishToSubjectRequest.SerializeToString,
                response_deserializer=api__pb2.PublishToSubjectResponse.FromString,
                )


class APIServicer(object):
    """API is the main Liftbridge server interface clients interact with.
    """

    def CreateStream(self, request, context):
        """CreateStream creates a new stream attached to a NATS subject. It returns
        an AlreadyExists status code if a stream with the given subject and name
        already exists.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteStream(self, request, context):
        """DeleteStream deletes a stream.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PauseStream(self, request, context):
        """PauseStream pauses a stream's partitions. If no partitions are
        specified, all of the stream's partitions will be paused. Partitions are
        resumed when they are published to via the Liftbridge Publish API.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Subscribe creates an ephemeral subscription for the given stream. It
        begins to receive messages starting at the given offset and waits for
        new messages when it reaches the end of the stream. Use the request
        context to close the subscription.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchMetadata(self, request, context):
        """FetchMetadata retrieves the latest cluster metadata, including stream
        broker information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Publish(self, request, context):
        """Publish a new message to a stream. If the AckPolicy is not NONE and a
        deadline is provided, this will synchronously block until the ack is
        received. If the ack is not received in time, a DeadlineExceeded status
        code is returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PublishAsync(self, request_iterator, context):
        """Asynchronously publish messages to a stream. This returns a stream which
        will yield PublishResponses for messages whose AckPolicy is not NONE.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PublishToSubject(self, request, context):
        """Publish a Liftbridge message to a NATS subject. If the AckPolicy is not NONE and a
        deadline is provided, this will synchronously block until the first ack
        is received. If an ack is not received in time, a DeadlineExceeded
        status code is returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_APIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateStream': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateStream,
                    request_deserializer=api__pb2.CreateStreamRequest.FromString,
                    response_serializer=api__pb2.CreateStreamResponse.SerializeToString,
            ),
            'DeleteStream': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteStream,
                    request_deserializer=api__pb2.DeleteStreamRequest.FromString,
                    response_serializer=api__pb2.DeleteStreamResponse.SerializeToString,
            ),
            'PauseStream': grpc.unary_unary_rpc_method_handler(
                    servicer.PauseStream,
                    request_deserializer=api__pb2.PauseStreamRequest.FromString,
                    response_serializer=api__pb2.PauseStreamResponse.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=api__pb2.SubscribeRequest.FromString,
                    response_serializer=api__pb2.Message.SerializeToString,
            ),
            'FetchMetadata': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchMetadata,
                    request_deserializer=api__pb2.FetchMetadataRequest.FromString,
                    response_serializer=api__pb2.FetchMetadataResponse.SerializeToString,
            ),
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=api__pb2.PublishRequest.FromString,
                    response_serializer=api__pb2.PublishResponse.SerializeToString,
            ),
            'PublishAsync': grpc.stream_stream_rpc_method_handler(
                    servicer.PublishAsync,
                    request_deserializer=api__pb2.PublishRequest.FromString,
                    response_serializer=api__pb2.PublishResponse.SerializeToString,
            ),
            'PublishToSubject': grpc.unary_unary_rpc_method_handler(
                    servicer.PublishToSubject,
                    request_deserializer=api__pb2.PublishToSubjectRequest.FromString,
                    response_serializer=api__pb2.PublishToSubjectResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.API', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class API(object):
    """API is the main Liftbridge server interface clients interact with.
    """

    @staticmethod
    def CreateStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.API/CreateStream',
            api__pb2.CreateStreamRequest.SerializeToString,
            api__pb2.CreateStreamResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.API/DeleteStream',
            api__pb2.DeleteStreamRequest.SerializeToString,
            api__pb2.DeleteStreamResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PauseStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.API/PauseStream',
            api__pb2.PauseStreamRequest.SerializeToString,
            api__pb2.PauseStreamResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/proto.API/Subscribe',
            api__pb2.SubscribeRequest.SerializeToString,
            api__pb2.Message.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchMetadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.API/FetchMetadata',
            api__pb2.FetchMetadataRequest.SerializeToString,
            api__pb2.FetchMetadataResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.API/Publish',
            api__pb2.PublishRequest.SerializeToString,
            api__pb2.PublishResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PublishAsync(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/proto.API/PublishAsync',
            api__pb2.PublishRequest.SerializeToString,
            api__pb2.PublishResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PublishToSubject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.API/PublishToSubject',
            api__pb2.PublishToSubjectRequest.SerializeToString,
            api__pb2.PublishToSubjectResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
