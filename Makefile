APP=yt_trending.api.main:app
PYTHONPATH=src

.PHONY: help install data train run test e2e docker clean

help:
	@echo "make install   -> install dependencies"
	@echo "make data      -> download Kaggle dataset"
	@echo "make train     -> train ML models (IN + US)"
	@echo "make run       -> run FastAPI locally"
	@echo "make test      -> run unit + e2e tests"
	@echo "make e2e       -> full system validation"
	@echo "make docker    -> run via Docker Compose"
	@echo "make clean     -> remove caches"

install:
	pip install -r requirements.txt

data:
	python scripts/download_dataset.py

train:
	PYTHONPATH=$(PYTHONPATH) python src/yt_trending/ml/train_model.py

run:
	PYTHONPATH=$(PYTHONPATH) uvicorn $(APP) --reload

test:
	PYTHONPATH=$(PYTHONPATH) pytest

e2e:
	bash scripts/e2e_validate.sh

docker:
	docker compose -f docker/docker-compose.yml up --build

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
