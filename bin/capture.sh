#!/usr/bin/env bash

set -e

##
# Starts screencapture in grayscale with the specified dimension
# Usage:
# ./bin/capture.sh 100x100

ffmpeg \
	-framerate 10 \
	-pix_fmt 0rgb \
	-f avfoundation \
	-i "1" \
	-r 10 \
	-pix_fmt:v 0rgb \
	-f rawvideo \
	-
