#!/bin/bash

# List of possible video devices
VIDEO_DEVICES=("/dev/video0" "/dev/video1" "/dev/video2")

echo "Start stream."

# Function to check if a video device exists and is accessible
find_working_device() {
    for device in "${VIDEO_DEVICES[@]}"; do
        if [ -e "$device" ]; then
            echo "$device"  # Output the device name
            return 0
        fi
    done
    echo "No working video device found." >&2
    exit 1
}

# Get the first working video device
VIDEO_DEVICE=$(find_working_device)

# Ensure VIDEO_DEVICE is not empty
if [[ -z "$VIDEO_DEVICE" ]]; then
    echo "Error: No valid video device found!" >&2
    exit 1
fi

echo "Starting stream with device: $VIDEO_DEVICE"

# Run mjpg-streamer with the selected device
exec /opt/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer \
     -i "input_uvc.so -d $VIDEO_DEVICE -r 640x480 -f 30" \
     -o "output_http.so -w ./www -p 8080"
