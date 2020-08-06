#!/usr/bin/env bash

##
# Displays the field of view.
# Usage
# bin/run.sh 100x100 50x50

size=3360x2100
output=100x100

ffplay \
  -pixel_format 0rgb \
  -video_size $output \
  -f rawvideo \
  <(bin/capture.sh | bin/focus.py $size $output)
