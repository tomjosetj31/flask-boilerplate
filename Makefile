.PHONY: help install setup test lint format clean run docker-build docker-run docker-stop

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies
	pip install -r requirements.txt

setup: ## Setup the project (create venv, install deps, init db)
	python setup.py

test: ## Run tests
	pytest tests/ -v

lint: ## Run linting
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format: ## Format code with black
	black .

clean: ## Clean up cache and temporary files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/

run: ## Run the Flask application
	python app.py

run-dev: ## Run Flask in development mode
	export FLASK_ENV=development && export FLASK_DEBUG=1 && flask run

db-init: ## Initialize database
	flask db init

db-migrate: ## Create a new migration
	flask db migrate -m "$(message)"

db-upgrade: ## Apply migrations
	flask db upgrade

db-downgrade: ## Downgrade migrations
	flask db downgrade

docker-build: ## Build Docker image
	docker build -t flask-boilerplate .

docker-run: ## Run with Docker Compose
	docker-compose up -d

docker-stop: ## Stop Docker Compose services
	docker-compose down

docker-logs: ## View Docker logs
	docker-compose logs -f

shell: ## Start Flask shell
	flask shell

create-admin: ## Create admin user
	python manage.py create-admin

create-user: ## Create regular user
	python manage.py create-user

list-users: ## List all users
	python manage.py list-users

list-posts: ## List all posts
	python manage.py list-posts 