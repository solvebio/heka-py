import heka


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

conn = heka.HekaConnection('localhost:5565', signer_config)
conn.send_message(msg)
