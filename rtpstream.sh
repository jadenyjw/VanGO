raspivid -o - -t 0 -n | cvlc -vvv stream:///dev/video0 --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264
