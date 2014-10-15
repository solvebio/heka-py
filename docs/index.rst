.. heka-py documentation master file, created by
   sphinx-quickstart on Thu Oct  9 13:16:58 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

heka-py
=======

heka-py is a `Python <https://www.python.org/>`_ client for `Heka <http://docs.services.mozilla.com/heka/>`_.

    Heka is a tool for collecting and collating data from a number of different sources, performing "in-flight" processing of collected data, and delivering the results to any number of destinations for further analysis.


Quick Start
-----------

Heka is used in 2 ways primarily.

Without a client::

    import heka

    heka.log('coffee_empty', severity=heka.ERROR, to=('localhost', 5565))

Getting Started
---------------

The simplest way to interact with heka-py is to import the package and create a message::

    import heka

    msg = heka.Message(
        'ads_served',
        severity=heka.INFO,
        fields={'ad_ids': [1, 2, 3], 'time_taken': 0.010},
    )

Try to inspect the data you entered::

    msg.type
    # 'ads_served'

    msg.fields['ad_ids']
    # [1, 2, 3]

    msg.fields['time_taken']
    # [0.01]

*Notice that each field in* ``fields`` *is automatically converted to a list. This is because heka supports multiple value per field and heka-py libary converts user input accordingly for convenience.*

Heka-py automatically adds some attributes to the message::

    msg.timestamp  # timestamp in nanoseconds
    # 1412857650827009024

    msg.uuid  # unique identifier for the message
    # '\xab\x16J\x03\xa3\xd4Uy\x88j\xd1\xf7\x93\xca\x83m'

    msg.pid  # current process ID
    # 8395

    msg.hostname  # hostname of machine
    # 'dev.seriouscompany.net'

To encode the message::

    payload = msg.encode()

    payload
    # '\n\x10\x12\x81\xcc\xc0(\xc3U\xc4\xbb`\xb0h\x00F8\xa2\x10\x80\x9c\xe1\xc3\xfa\x82\xdf\xcd\x13\x1a\nads_served"\x00(\x072\x00:\x030.8@\xcbAJ\x16dev.seriouscompany.netR\x1a\n\ntime_taken\x10\x03\x1a\x00:\x08{\x14\xaeG\xe1z\x84?R\x11\n\x06ad_ids\x10\x02\x1a\x002\x03\x01\x02\x03'

At this point we want to send the message to Heka. We can use any of the input mechanisms that Heka supports. The simplest is UDP packets::

    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(payload, ('localhost, 5565))


Contributors
------------
- Rob Miller (rmiller@mozilla.com)
- Victor Ng (vng@mozilla.com)
- Kashif Malik (kashif610@gmail.com)



Contents:

.. toctree::
   :maxdepth: 2


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

