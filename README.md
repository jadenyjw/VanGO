# VanGO
This is the command server for a rover made with a Raspberry Pi.
The client source code can be viewed [here](https://github.com/jadenyjw/vango-java).

## Usage

When `vango.py` is ran with `python2` , it initializes a TCP socket server on port 8888 (unprivileged port), listening for commands.

When `rtpstream.sh` is ran, it creates an RTSP stream utilizing VLC as a dependency on port 8554 (unprivileged port).
