#!/bin/sh
pnpm build &&
    pdm run python src/hymnal/main.py &&
    git clone --depth 1 "https://github.com/hakimel/reveal.js.git" dist/hymnal/lib/reveal.js &&
    podman-compose -p hymnal -f ./compose.yaml down
    podman-compose -p hymnal -f ./compose.yaml up -d
