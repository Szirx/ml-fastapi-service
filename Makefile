DOCKER_IMAGE = szirx/dep-app
DOCKER_TAG = latest
PORT = 2444

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: build
build:
	docker build -f Dockerfile . -t $(DOCKER_IMAGE):$(DOCKER_TAG)

.PHONY: docker_run
docker_run:
	docker run -d -v ./model:/app/model -p $(PORT):$(PORT) $(DOCKER_IMAGE):$(DOCKER_TAG)

.PHONY: compose
compose:
	docker-compose up --build -d

.PHONY: apply_manifests
apply_manifests:
	kubectl apply -f ./manifests

.PHONY: interactive
interactive:
	kubectl run --image=curlimages/curl curl -it sh

.PHONY: example_run
example_run:
	python3 app.py