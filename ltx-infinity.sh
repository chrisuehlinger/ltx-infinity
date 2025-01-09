#!/bin/bash -x

RUN_NAME=${1:-"ltx-infinity"}

rm -rf ../storage/ComfyUI/output/ltxinfinity

python ltx-infinity.py

./ltx-infinity-concat.sh RUN_NAME