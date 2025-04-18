#!/bin/bash -x

# Build
docker build -t j2engine .

# Test
./render.sh
