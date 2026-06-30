#!/bin/bash
 

NUM_SERVERS=${1:-2}
BASE_PORT=3300

for i in $(seq 1 $NUM_SERVERS); do
  PORT=$((BASE_PORT + i))
  NAME="playwright-server-$(printf '%02d' $i)"
  
  echo "Starting $NAME on port $PORT..."
  
  podman run -d \
    --name "$NAME" \
    -p "$PORT:3000" \
    --init \
    --ipc=host \
    --userns=keep-id \
    --user pwuser \
    --security-opt seccomp="$(pwd)/seccomp_profile.json" \
    --workdir /home/pwuser \
    mcr.microsoft.com/playwright:v1.57.0-noble \
    /bin/sh -c "npx -y playwright@1.57.0 run-server --port 3000 --host 0.0.0.0"
done

echo "Started $NUM_SERVERS Playwright servers on ports $((BASE_PORT + 1))-$((BASE_PORT + NUM_SERVERS))"
