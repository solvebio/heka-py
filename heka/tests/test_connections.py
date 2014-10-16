from mock import patch

from ..connections import HekaConnection
from ..message import Message
from .. import severity
from .. import framing


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

ENCODED_MESSAGE = MESSAGE.encode()
FRAMED_MESSAGE = framing.frame(ENCODED_MESSAGE)


def test_heka_connection_initializes_socket():
    conn = HekaConnection()
    assert conn.socket is not None


def test_heka_connection_lazy_option_does_not_initialize_socket():
    conn = HekaConnection(lazy=True)
    assert conn.socket is None


def test_heka_connection_send_frames_message_and_writes_to_socket():
    conn = HekaConnection()

    with patch.object(conn, 'socket') as mock_socket:
        conn.send(ENCODED_MESSAGE)

    mock_socket.send.assert_called_once_with(FRAMED_MESSAGE)
