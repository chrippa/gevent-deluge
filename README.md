gevent-deluge
=============

An implementation of the Deluge RPC protocol using gevent.

Example usage
-------------

```python

from geventdeluge import DelugeClient

client = DelugeClient()
client.connect()

# Wait for value
download_location = client.core.get_config_value("download_location").get()

def on_get_config_value(value, key):
    print "Got config value from the daemon!"
    print "%s: %s" % (key, value)

    client.disconnect()

# Callback style
client.core.get_config_value("download_location").callback(on_get_config_value, "download_location")

# Wait for event loop to finish
client.run()
```
