
#  works oki ig
# pin to match local client (playwright==1.58.0 in pyproject.toml)
podman pull mcr.microsoft.com/playwright:v1.58.0-jammy


podman run -d \
  --name playwright-server-01 \
  -p 3301:3301 \
  --init \
  --ipc=host \
  --userns=keep-id \
  --user pwuser \
  --security-opt seccomp=$(pwd)/seccomp_profile.json \
  --workdir /home/pwuser \
  mcr.microsoft.com/playwright:v1.58.0-jammy \
  /bin/sh -c "npx -y playwright@1.58.0 run-server --port 3301 --host 0.0.0.0"

