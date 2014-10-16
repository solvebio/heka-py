from ..message import Message
from .. import severity


MESSAGE = Message(
    type='test',
    logger='heka-py-tester',
    severity=severity.INFO,
    fields={
        'field1': 1,
        'field2': [2.3, 4.5],
        'field3': True,
        'field4': 'The4thValue',
    },
    payload='ThisIsVeryImportantInformation',
)

ENCODED_MESSAGE = '\n\x10\'v7\xdf\x81\xdbZT\xabZm\xec\x1b]1G\x10\x80\xfe\xa0\xe3\xe2\x9c\xe5\xce\x13\x1a\x04test"\x0eheka-py-tester(\x062\x1eThisIsVeryImportantInformation:\x030.8@\xbdtJ\x16dev.vagrant.disqus.netR\x1e\n\x06field2\x10\x03\x1a\x00:\x10ffffff\x02@\x00\x00\x00\x00\x00\x00\x12@R\x0f\n\x06field3\x10\x02\x1a\x002\x01\x01R\x0f\n\x06field1\x10\x02\x1a\x002\x01\x01R\x19\n\x06field4\x10\x00\x1a\x00"\x0bThe4thValue'


def test_message_automatically_populates_timestamp():
    assert type(MESSAGE.timestamp) is int


def test_message_automatically_populates_pid():
    assert type(MESSAGE.pid) is int


def test_message_automatically_populates_hostname():
    assert type(MESSAGE.hostname) is str


def test_message_can_encode_itself_into_string():
    payload = MESSAGE.encode()

    assert payload
    assert type(payload) == str


def test_message_can_decode_from_string():
    message = Message.decode(ENCODED_MESSAGE)

    assert type(message) is Message
    assert message.type == MESSAGE.type
    assert message.logger == MESSAGE.logger
    assert message.severity == MESSAGE.severity
    assert message.fields == MESSAGE.fields
    assert message.payload == MESSAGE.payload


def test_message_assigns_unique_uuids_on_consecutive_creations():
    message1 = Message()
    message2 = Message()

    assert message1.uuid != message2.uuid
