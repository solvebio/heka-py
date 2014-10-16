import mock
from collections import namedtuple

from ..signing import sign_header, SignerConfig


Result = namedtuple('TestResult', ('hash_function_value', 'hash'))

PAYLOAD = """
This is a bunch of bytes.
Do you like my bytes?
I love my bytes.
"""

SIGNER_CONFIG_CASES = {
    'sha1': SignerConfig('signer1', 3, 'thiskeyisthebestkey', 'sha1'),
    'md5': SignerConfig('other_signer', 5, 'butthisoneisbetter', 'md5'),
}

CASE_RESULTS = {
    'sha1': Result(hash_function_value=1, hash='\xc1\xa6\xab3\xb0\x8d\xaf\xaf\xa4\xa5\xfa\xea\xab&\'@o\xe8C\xe4'),
    'md5': Result(hash_function_value=0, hash='\xe0)\n\xe8\xd2z\xa5v\x04_\xa3F\xb6\x9f\x8a\\'),
}


def test_sign_header_sets_attributes_on_header():
    """
    Test that sign_header sets the appropriate attributes on the header object.

    """
    header = mock.Mock()

    # Delete mock attributes
    del header.hmac_signer
    del header.hmac_key_version
    del header.hmac_hash_function
    del header.hmac

    sign_header(header, PAYLOAD, SIGNER_CONFIG_CASES['sha1'])

    # Check attribute presence
    assert header.hmac_signer
    assert header.hmac_key_version
    assert header.hmac_hash_function
    assert header.hmac


def test_sign_header_signs_sha1():
    """
    Test that sign_header signs the header correctly using SHA1.

    """
    header = mock.Mock()
    sign_header(header, PAYLOAD, SIGNER_CONFIG_CASES['sha1'])

    # Check attributes from signer config
    assert header.hmac_signer == SIGNER_CONFIG_CASES['sha1'].name
    assert header.hmac_key_version == SIGNER_CONFIG_CASES['sha1'].version

    # Check hash function protobuf value
    assert header.hmac_hash_function == CASE_RESULTS['sha1'].hash_function_value

    # Check hash
    assert header.hmac == CASE_RESULTS['sha1'].hash


def test_sign_header_signs_md5():
    """
    Test that sign_header signs the header correctly using MD5.

    """
    header = mock.Mock()
    sign_header(header, PAYLOAD, SIGNER_CONFIG_CASES['md5'])

    # Check attributes from signer config
    assert header.hmac_signer == SIGNER_CONFIG_CASES['md5'].name
    assert header.hmac_key_version == SIGNER_CONFIG_CASES['md5'].version

    # Check hash function protobuf value
    assert header.hmac_hash_function == CASE_RESULTS['md5'].hash_function_value

    # Check hash
    assert header.hmac == CASE_RESULTS['md5'].hash
