import heka
import socket


msg = heka.Message(
    'ads_served',
    'ads_server',
    heka.INFO,
    {'ad_ids': [1, 2, 3]}
)

signer_config = heka.SignerConfig(
    name='signed',
    version=1,
    key='password',
    hash='sha1',
)


payload = heka.frame(msg.encode(), signer_config)
print repr(payload)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(payload, ('localhost', heka.DEFAULT_PORT))
