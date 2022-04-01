export MYSQL_ROOT_PASSWORD
docker stack deploy --compose-file docker-compose.yaml finalproject-stack
docker service update --replicas 3 frontend