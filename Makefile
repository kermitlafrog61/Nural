run:
	docker compose up -d --build
down:
	docker compose down
logs:
	docker compose logs
bash:
	docker exec -it nural-api-1 bash
