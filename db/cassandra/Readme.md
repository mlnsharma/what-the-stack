
# Docker build
docker build . -t app:latest

# Docker compose
docker compose up --build --detach
docker compose down

# Clean Docker containers
docker rm $(docker ps -a -q -f status=exited)

# Cassandra commands
describe cluster

