run:
	sudo docker compose up -d --build
down:
	sudo docker compose down
logs:
	sudo docker compose logs
bash:
	sudo docker exec -it nural-api-1 bash
