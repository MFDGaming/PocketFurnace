from abc import ABCMeta


class PyRakLib:
    __metaclass__ = ABCMeta

    SYSTEM_ADDRESS_COUNT = 20
    LIBRARY_VERSION = "1.0.16beta1"
    VERSION = "0.12.0"
    DEFAULT_PROTOCOL_VERSION = 6
    MAGIC = bytearray.fromhex("00 ff ff 00 fe fe fe fe fd fd fd fd 12 34 56 78")

    PRIORITY_NORMAL = 0
    PRIORITY_IMMEDIATE = 1

    FLAG_NEED_ACK = 0b00001000

    """
     * ENCAPSULATED payload:
     * byte (identifier length)
     * byte[] (identifier)
     * byte (flags, last 3 bits, priority)
     * payload (binary internal EncapsulatedPacket)
     """
    PACKET_ENCAPSULATED = 0x01
    """
     * OPEN_SESSION payload:
     * byte (identifier length)
     * byte[] (identifier)
     * byte (address length)
     * byte[] (address)
     * short (port)
     * long (client_id)
     """
    PACKET_OPEN_SESSION = 0x02
    """
     * CLOSE_SESSION payload:
     * byte (identifier length)
     * byte[] (identifier)
     * string (reason)
     """
    PACKET_CLOSE_SESSION = 0x03
    """
     * INVALID_SESSION payload:
     * byte (identifier length)
     * byte[] (identifier)
     """
    PACKET_INVALID_SESSION = 0x04
    """ TODO: implement this
     * SEND_QUEUE payload:
     * byte (identifier length)
     * byte[] (identifier)
     """
    PACKET_SEND_QUEUE = 0x05
    """
     * ACK_NOTIFICATION payload:
     * byte (identifier length)
     * byte[] (identifier)
     * int (identifier_ack)
     """
    PACKET_ACK_NOTIFICATION = 0x06
    """
     * SET_OPTION payload:
     * byte (option name length)
     * byte[] (option name)
     * byte[] (option value)
     """
    PACKET_SET_OPTION = 0x07
    """
     * RAW payload:
     * byte (address length)
     * byte[] (address from/to)
     * short (port)
     * byte[] (payload)
     """
    PACKET_RAW = 0x08
    """
     * RAW payload:
     * byte (address length)
     * byte[] (address)
     * int (timeout)
     """
    PACKET_BLOCK_ADDRESS = 0x09
    """
     * REPORT_PING payload:
     * byte (identifier length)
     * byte[] (identifier)
     * int32 (measured latency in MS)
    """
    PACKET_UNBLOCK_ADDRESS = 0x10
    """
    * REPORT_PING payload:
    * byte (identifier length)
    * byte[] (identifier)
    * int32 (measured latency in MS)
    """
    PACKET_REPORT_PING = 0x11
    """
     * No payload
     *
     * Sends the disconnect message, removes sessions correctly, closes sockets.
     """
    PACKET_SHUTDOWN = 0x7e
    """
     * No payload
     * Leaves everything as-is and halts, other Threads can be in a post-crash condition.
    """
    PACKET_EMERGENCY_SHUTDOWN = 0x7f
