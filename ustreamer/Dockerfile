# Use an official Debian image
FROM debian:latest

# Install necessary packages
RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    git \
    cmake \
    libjpeg-dev \
    v4l-utils

# Clone the mjpg-streamer repository and build it
RUN git clone https://github.com/jacksonliam/mjpg-streamer.git /opt/mjpg-streamer \
    && cd /opt/mjpg-streamer/mjpg-streamer-experimental \
    && make

# Expose port 8080 for the HTTP stream
EXPOSE 8080




#CMD ["bash", "-c", "while true; do ls; sleep 100; done"]

# Start mjpg-streamer with input and output plugins.
WORKDIR /opt/mjpg-streamer/mjpg-streamer-experimental
COPY start_stream.sh /start_stream.sh
RUN chmod +x /start_stream.sh
CMD ["/start_stream.sh"]

#CMD ["/opt/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer", \
#     "-i", "input_uvc.so -d /dev/video1 -r 640x480 -f 30", \
#     "-o", "output_http.so -w ./www -p 8080"]


# v4l2-ctl -d /dev/video0 --list-ctrls

# cd /opt/mjpg-streamer/mjpg-streamer-experimental

# CMD /opt/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer -i "./input_uvc.so -d /dev/video0 -r 640x480 -f 30" -o "./output_http.so -w ./www -p 8080"