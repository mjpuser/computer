#!/usr/bin/env bash

##
# Displays the field of view.
# Usage
# bin/run.sh 100x100 50x50


ffplay \
  -f rawvideo \
  -pix_fmt gray \
  -video_size $2 \
  <(bin/capture.sh $1 | bin/focus.py $1 $2)
