# Setup

## Docker

### Easy setup (everything belongs to `root`):

```bash
docker compose build
docker compose up
```

### Setup with your host user instad of `root`:

Uncomment all these lines in [`./docker-compose.yml`](./docker-compose.yml):
```yaml
# Remove comments
user: ${DOCKER_USER}
```

Build containers and add your host user to them:

```bash
export DOCKER_USER="$(id -u):$(id -g)"
docker compose build
docker compose up
docker compose exec --user root flask useradd -m -s /bin/bash $USER
docker compose exec --user root vue useradd -m -s /bin/bash $USER
```

## Local

### Backend

Dependencies:
```bash
cd server
export PIPENV_VENV_IN_PROJECT=1
pipenv install 
```

Migrations:
```bash
export FLASK_APP=src/app.py
pipenv run flask db upgrade
```
Server:

```bash
pipenv run flask --debug run
```

Flask API will be running on port `5000`.

### Frontend

Dependencies:

```bash
cd client
npm install
```

Server:

```bash
npm run dev
```

Vite server will be running on port `5173`.
