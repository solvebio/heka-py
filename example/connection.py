import heka


msg = heka.Message(
    'ads_served',
    'ads_server',
    heka.INFO,
    {'ad_ids': [1, 2, 3]}
)

conn = heka.HekaConnection('localhost:5565')
conn.send_message(msg)
