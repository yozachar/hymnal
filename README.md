# Hymnal

Just a hymnal.

## Local setup

### Requirements

- Git
- pnpm
- pdm
- Python
- Podman / Docker
- Podman-Compose / Docker-Compose

### Clone repository

```sh
git clone "https://github.com/joe733/hymnal.git"
cd hymnal
```

### Install dependencies

```sh
pnpm install && pdm install
```

### Build & Deploy

#### Automated

```sh
./deploy.sh
```

#### Manual

Build project

```sh
eval $(pdm venv activate)
pnpm build
python src/hymnal/main.py
git clone --depth 1 "https://github.com/hakimel/reveal.js.git" dist/hymnal/lib/reveal.js
```

Deploy project (start web-server)

```sh
podman-compose -p hymnal -f ./compose.yaml up -d
```

Open <http://localhost:8080> in your browser.

### Take down web-server

```sh
podman-compose -p hymnal -f ./compose.yaml down
```
