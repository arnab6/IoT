# IoT publish / Suscriber roject using python

### Installation

This project needs python 3 runtime, before running please install the python from [here](https://www.python.org/downloads/) 

install the packges 

```python
$ pip3 install paho-mqtt

```

### Run the sample 

The "StorageDevice.py" creates simulated JSON packet for a brevrage storage device and publises it to MQTT broker.

```
$ python StorageDevice.py

```

The "subcriberTempatureCheck.py" suscribes to same topic that "StorageDevice.py" is publishing & checks for the temparature condtion.

```
$ python subcriberTempatureCheck.py

```

```

The "suscriberHumidityCheck.py" suscribes to same topic that "StorageDevice.py" is publishing & checks for the humidity condtion.

```
$ python suscriberHumidityCheck.py

```

