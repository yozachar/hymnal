#!/bin/bash

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
RESET='\033[0m'

# check if a command exists
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# cleanup
rm -rf ./build/

# build
echo -e "${BLUE}==> Build & Generate${RESET}"
pdm run python ./src/hymnal/main.py &&
  pnpm build

# preview
pnpm preview

# # deploy
# commands=("docker" "podman")
# for cmd in "${commands[@]}"; do
#   if command_exists "$cmd"; then
#     echo -e "\n${BLUE}==> Deploy with '$cmd'${RESET}\n"
#     $cmd-compose -p hymnal -f ./compose.yaml down
#     $cmd-compose -p hymnal -f ./compose.yaml up -d
#     echo -e "\n${GREEN}==> Open http://[::1]:8080 in your browser${RESET}"
#     exit $?
#   else
#     echo -e "\n${YELLOW}==> Warning: Command '$cmd' not found${RESET}"
#   fi
# done
# echo -e "\n${RED}==> Error: Deploymnet failed${RESET}"
# exit 1

set +e
