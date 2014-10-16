from collections import namedtuple

from ..framing import frame
from ..signing import SignerConfig


Result = namedtuple('TestResult', ('hash_function_value', 'hash'))

PAYLOAD = """
This is a bunch of bytes.
Do you like my bytes?
I love my bytes.
"""

SIGNER_CONFIG = SignerConfig('signer1', 3, 'thiskeyisthebestkey', 'sha1')

FRAMING_RESULTS = {
    'not_signed': '\x1e\x02\x08B\x1f\nThis is a bunch of bytes.\nDo you like my bytes?\nI love my bytes.\n',
    'signed': '\x1e%\x08B\x18\x01"\x07signer1(\x032\x14\xc1\xa6\xab3\xb0\x8d\xaf\xaf\xa4\xa5\xfa\xea\xab&\'@o\xe8C\xe4\x1f\nThis is a bunch of bytes.\nDo you like my bytes?\nI love my bytes.\n',
}


def test_frame_without_signing():
    """
    Test that frame returns the correct bytes given a payload.

    """

    assert frame(PAYLOAD) == FRAMING_RESULTS['not_signed']


def test_frame_with_signing():
    """
    Test that frame signs and returns the correct bytes given a payload.

    """

    assert frame(PAYLOAD, SIGNER_CONFIG) == FRAMING_RESULTS['signed']
