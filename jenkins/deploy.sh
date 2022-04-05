export MYSQL_ROOT_PASSWORD= ${MYSQL_ROOT_PASSWORD}
docker stack deploy --compose-file docker-compose.yaml finalproject-stack

docker service update --replicas 3 finalproject-stack_accountnumber
docker service update --replicas 3 finalproject-stack_frontend
docker service update --replicas 3 finalproject-stack_letters
docker service update --replicas 3 finalproject-stack_numbers
