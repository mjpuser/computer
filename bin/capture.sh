#!/usr/bin/env bash

set -e

##
# Starts screencapture in grayscale with the specified dimension
# Usage:
# ./bin/capture.sh 100x100

ffmpeg \
	-video_size $1 \
	-framerate 10 \
	-f x11grab \
	-i :0.0+200,200 \
	-c:v rawvideo \
	-pix_fmt:v gray \
	-f rawvideo -
