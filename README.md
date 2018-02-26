# mqtool

A small MQTT tool to publish or subscribe to a topic. 

Examples:
```
mqtool -h 192.168.4.1 -t home/clock --sub

mqtool -h 192.168.4.1 -t home/clock -m "Hello World"
```

It can be compiled to a MS-DOS executable using py2exe.
```
python -OO compile.py py2exe
```

Help:

```
usage: mqtool [--help] [--sub] [-h HOST] [-p PORT] [-t TOPIC] [-m MESSAGE]
                [-u USER] [-P PASSWORD]

Simple MQTT publish/subscribe tool

optional arguments:
  --help       show this help message and exit.
  --sub        Subscribe and listen topic, use CTRL+C to exit
  -h HOST      host name or IP address
  -p PORT      set port number, default is 1883
  -t TOPIC     set topic
  -m MESSAGE   message to publish
  -u USER      set user
  -P PASSWORD  password
```

