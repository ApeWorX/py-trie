BLANK_NODE: bytes = b""
# keccak(b'')
BLANK_HASH: bytes = b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';{\xfa\xd8\x04]\x85\xa4p"  # noqa: E501
# keccak(rlp.encode(b''))
BLANK_NODE_HASH: bytes = b"V\xe8\x1f\x17\x1b\xccU\xa6\xff\x83E\xe6\x92\xc0\xf8n\x5bH\xe0\x1b\x99l\xad\xc0\x01b/\xb5\xe3c\xb4!"  # noqa: E501


NIBBLE_TERMINATOR: int = 16

HP_FLAG_2: int = 2
HP_FLAG_0: int = 0


NODE_TYPE_BLANK: int = 0
NODE_TYPE_LEAF: int = 1
NODE_TYPE_EXTENSION: int = 2
NODE_TYPE_BRANCH: int = 3

# Constants for Binary Trie
EXP: tuple[int, ...] = tuple(reversed(tuple(2**i for i in range(8))))

TWO_BITS: list[bytes] = [
    bytes([0, 0]),
    bytes([0, 1]),
    bytes([1, 0]),
    bytes([1, 1]),
]
PREFIX_00: bytes = bytes([0, 0])
PREFIX_100000: bytes = bytes([1, 0, 0, 0, 0, 0])

KV_TYPE: int = 0
BRANCH_TYPE: int = 1
LEAF_TYPE: int = 2
BINARY_TRIE_NODE_TYPES: tuple[int, int, int] = (0, 1, 2)
KV_TYPE_PREFIX: bytes = bytes([0])
BRANCH_TYPE_PREFIX: bytes = bytes([1])
LEAF_TYPE_PREFIX: bytes = bytes([2])

BYTE_1: bytes = bytes([1])
BYTE_0: bytes = bytes([0])
