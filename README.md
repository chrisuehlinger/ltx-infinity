# LTX Infinity

This is a small project I'm working on to try and get LTX to generate videos of indefinite length. I'm still experimenting a lot here, so nothing in this repo should necessarily be taken as a "well thought out best practice". Also a lot of things in here could change, and I'm not going to be able to provide support for maintaining this as LTX and the other models undergo massive changes in the next year.

But for now, enjoy!

I built all of this on an RTX 3090 with 24GB of RAM. You'll need similar hardware or you'll need to change the parameters.

## Setup

I run ComfyUI in Docker on Linux. You don't have to do that, but if you run ComfyUI some other way you'll need to change the hard-coded paths in the Cache Node and Load Cache Node to point to your `ComfyUI/input` directory.

First load up these workflows in `ui-workflows` ComfyUI and make sure you have all the necessary nodes. Run the `ltx-infinity-init` workflow, then clear your VRAM completely, then runthe one called `ltx-infinity`. If those both work, you can try using the automated scripts.

If you run `ui-workflows/ltx-infinity.json` multiple times, you'll need to completely clear ComfyUI's cache every time (not just unload the models) so that the Load Cache node will be forced to reload the cached image.

# Running the automated workflow

On Linux or WSL, run `./ltx-infinity.sh <run_name>` (the run_name will be used in the output video file at the end). I often kill this script long before it has gone through 600 iterations, in which case `./ltx-infinity-concat.sh <run_name>` will assemble your final video for you. Beware that `./ltx-infinity.sh` blows away your old results when it starts a new run.

Oh also, you probably need to change the path in `./ltx-infinity-concat.sh` to point to your ComfyUI output folder, wherever that is.