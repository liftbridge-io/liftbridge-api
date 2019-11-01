Liftbridge API
==============

This repository contains the public API definitions for
[Liftbridge](https://github.com/liftbridge-io/liftbridge). It is primarily intended for
Liftbridge client developers.

## gRPC API

The client-facing gRPC API is defined in [api.fbs](api.fbs).

## Direct NATS API

It is also possible for a client to publish messages to Liftbridge via NATS directly.
Liftbridge accepts plain NATS messages, allowing it to make existing subjects durable
without any publisher changes. However, these messages will not have some features such
as acks.

In order to opt into Liftbridge-specific features, the message must be prefixed with the
following header and be encoded as a `PublishRequest` (defined in
[api.fbs](api.fbs)).

### Liftbridge Envelope Header

```
0               8               16              24              32
├───────────────┴───────────────┴───────────────┴───────────────┤
│                          Magic Number                         │
├───────────────┬───────────────┬───────────────┬───────────────┤
│    Version    │   HeaderLen   │     Flags     │    MsgType    │
├───────────────┴───────────────┴───────────────┴───────────────┤
│                       CRC-32C (optional)                      │
└───────────────────────────────────────────────────────────────┘
```


#### Magic number [4 bytes]

The Liftbridge magic number is `B9 0E 43 B4`. This was chosen by random but deliberately
restricted to invalid UTF-8 to reduce the chance of a collision. This was also verified
to not match known file sigatures.

#### Version [1 byte]

The version byte allows for future protocol upgrades. This should only be bumped if the
envelope format changes or if the message encoding changes in a non-backwards-compatible
way. Adding fields to the messages should not require a version bump.

#### HeaderLen [1 byte]

The header length is the offset of the payload. This is included primarily for safety.

#### Flags [1 byte]

The flag bits are defined as follows:

| Bit | Description     |
| --- | --------------- |
| 0   | CRC-32C enabled |

#### MsgType [1 byte]

This is the Liftbridge-specific message type

| MsgType | Description |
| ------- | ----------- |
| 0       | Publish     |
| 1       | Replication |

#### CRC-32C [4 bytes, optional]

The CRC-32C (Castagnoli) is the checksum of the payload (i.e. from HeaderLen to the
end). This is optional but should significantly reduce the chance that a random NATS
message is interpreted as a Liftbridge message.
