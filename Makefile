run:
	docker compose up --build

test:
	docker build -t backend-test -f Dockerfile.backend.test .
	docker run --rm backend-test

format:
	black .
	flake8 --ignore E501
	cd frontend; npx prettier --write .
