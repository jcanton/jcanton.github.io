#!/bin/bash

inputVideo=$1

dirname=$(dirname "$inputVideo")
filename=$(basename "$inputVideo")
extension="${filename##*.}"
filename="${filename%.*}"

outputGif="${dirname}/${filename}.gif"


command="ffmpeg\
 -y\
 -ss 00:00:00 -to 00:00:12\
 -i ${inputVideo}\
 -r 15\
 -vf 'scale=-1:500,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse'\
 -loop 0\
 ${outputGif}"

printf "\n\nConverting:\n"
printf "    input video: ${inputVideo}\n"
printf "    output gif : ${outputGif}\n"
printf "    command    : ${command}\n"

eval $command
