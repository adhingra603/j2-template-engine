#!/bin/bash
set -e

docker run -v $PWD:/home/overwatch j2engine $@

# debug mode
#docker run -v $PWD:/home/overwatch -it --entrypoint /bin/bash j2engine
