import heka


def send_through_transport(payload):
    pass


msg = heka.create_message(
    type='ads_served',
    logger='tempest',
    severity=heka.INFO,
    payload='We served so many ads!',
    fields={
        'ids': [1, 2, 3],
        'authenticated': False,
    },
)

send_through_transport(msg)
