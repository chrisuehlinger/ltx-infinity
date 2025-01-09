#!/bin/bash -x

RUN_NAME=${1:-"ltx-infinity"}

mkdir -p output

pushd ../storage/ComfyUI/output/ltxinfinity
rm output.mp4
find *.mp4 | sed 's:\ :\\\ :g'| sed 's/^/file /' > fl.txt
ffmpeg -f concat -i fl.txt -c copy output.mp4
rm fl.txt
popd

mv ../storage/ComfyUI/output/ltxinfinity/output.mp4 "./output/${RUN_NAME}.mp4"