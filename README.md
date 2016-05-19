# VanGO
This is the server for a Raspberry Pi Rover.

When `vango.py` is ran with `python2` , it initializes a TCP socket server on port 8888 (unprivileged port), listening for commands.

When `rtpstream.sh` is ran, it creates an RTSP stream utilizing VLC on port 8854 (unprivileged port).
