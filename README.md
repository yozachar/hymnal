# [Hymnal](https://yozachar.github.io/hymnal/)

> _O sing unto the Lord a new song..._

## Requirements

- [git](https://git-scm.com/)
- [pnpm](https://pnpm.io/)
- [PDM](https://pdm.fming.dev/latest/)
- [python](https://www.python.org/)
- [podman-compose](https://github.com/containers/podman-compose) / [docker-compose](https://github.com/docker/compose)

## Clone repository

```sh
git clone "https://github.com/yozachar/hymnal.git"
cd hymnal
```

## Install dependencies

```sh
pnpm install && pdm install
```

## Build & Deploy

### Automated

```sh
./deploy.sh
```

### Manual

Build project.

```sh
eval $(pdm venv activate)
pnpm build
python src/hymnal/main.py
git clone --depth 1 "https://github.com/hakimel/reveal.js.git" dist/hymnal/lib/reveal.js
```

Start web-server. Open <http://localhost:8080> in your browser. Replace `podman` with `docker`, if you're using the latter.

```sh
podman-compose -p hymnal -f ./compose.yaml up -d
```

Take down web-server.

```sh
podman-compose -p hymnal -f ./compose.yaml down
```

---

<div style="text-align:center">

[![AGPL-3.0](https://upload.wikimedia.org/wikipedia/commons/0/06/AGPLv3_Logo.svg)](https://wikipedia.org/wiki/GNU_Affero_General_Public_License)

</div>
