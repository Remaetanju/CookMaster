docker rmi -f  $(docker images -a -q)
docker compose down
docker rm -f $(docker ps -a -q)
docker volume rm $(docker volume ls -q)
#docker volume prune
#docker compose up --force-recreate --build

