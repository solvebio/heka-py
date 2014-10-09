from __future__ import absolute_import
import os
import socket
import time
import uuid
import collections

from heka.message_pb2 import Message, Field


# Envelope version, only changes when the message format changes.
ENV_VERSION = '0.8'

EMERGENCY = 0
ALERT = 1
CRITICAL = 2
ERROR = 3
WARNING = 4
NOTICE = 5
INFORMATIONAL = 6
DEBUG = 7


def _set_field_type_and_return_list(field, value):
    """
    Set the type on the protobuf field and return the resulting list.

    """
    if value is None:
        raise ValueError("None is not allowed for field values.  [%s]" % field.name)

    elif isinstance(value, int):
        field.value_type = Field.INTEGER
        field_list = field.value_integer

    elif isinstance(value, float):
        field.value_type = Field.DOUBLE
        field_list = field.value_double

    elif isinstance(value, bool):
        field.value_type = Field.BOOL
        field_list = field.value_bool

    elif isinstance(value, basestring):
        field.value_type = Field.STRING
        field_list = field.value_string

    else:
        raise ValueError("Unexpected value type : [%s][%s]" % (type(value), value))

    return field_list


def _flatten_fields(msg, field_map, prefix=None):
    for k, v in field_map.items():
        field = msg.fields.add()

        if prefix:
            full_name = "%s.%s" % (prefix, k)
        else:
            full_name = k

        field.name = full_name
        field.representation = ""

        if isinstance(v, collections.Mapping):
            msg.fields.remove(field)
            _flatten_fields(msg, v, prefix=full_name)

        elif isinstance(v, collections.Iterable) and not isinstance(v, basestring):
            values = iter(v)
            try:
                first_value = values.next()
            except StopIteration:
                first_value = None

            field_list = _set_field_type_and_return_list(field, first_value)
            field_list.append(first_value)

            for value in values:
                if not isinstance(value, type(first_value)):
                    raise ValueError("Multiple values in the same field cannot be of different types.  [%s]" % field.name)
                field_list.append(value)
        else:
            field_list = _set_field_type_and_return_list(field, v)
            field_list.append(v)


def create_message(
    type='',
    logger='',
    severity=DEBUG,
    payload='',
    fields=None,

    env_version=None,
    pid=None,
    hostname=None,
    timestamp=None,
):
    if env_version is None:
        env_version = ENV_VERSION

    if pid is None:
        pid = os.getpid()

    if hostname is None:
        hostname = socket.gethostname()

    if timestamp is None:
        timestamp = time.time()

    if fields is None:
        fields = {}

    msg = Message()
    msg.timestamp = int(timestamp * 1000000000)
    msg.type = type
    msg.logger = logger
    msg.severity = severity
    msg.payload = payload
    msg.env_version = ENV_VERSION
    msg.pid = pid
    msg.hostname = hostname
    _flatten_fields(msg, fields)
    msg.uuid = uuid.uuid5(uuid.NAMESPACE_OID, str(msg)).bytes

    return msg.SerializeToString()
