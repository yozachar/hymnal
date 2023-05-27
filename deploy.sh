#!/bin/sh
pnpm build &&
    poetry run python hymnal/main.py &&
    git clone --depth 1 "https://github.com/hakimel/reveal.js.git" dist/hymnal/lib/reveal.js &&
    podman-compose -p hymnal -f ./compose.yaml up -d
