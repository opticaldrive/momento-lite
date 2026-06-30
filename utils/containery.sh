
podman pull mcr.microsoft.com/playwright:latest


podman run -d \
  --name playwright-server-01 \
  -p 3301:3301 \
  --init \
  --ipc=host \
  --userns=keep-id \
  --user pwuser \
  --security-opt seccomp=$(pwd)/seccomp_profile.json \
  --workdir /home/pwuser \
  mcr.microsoft.com/playwright:latest \
  /bin/sh -c "npx -y playwright@latest run-server --port 3301 --host 0.0.0.0"

