#!/bin/bash

if [ "$1" == "" ]; then
  echo "Usage: ./findFiles.sh [path to files to be moved]"
  echo "Example: ./findFiles.sh /home/code/Downloads/"
else
  cd $1
  ls | grep .mp4
  ls | grep .mkv
fi
