install:
	poetry install

domain-counter:
	@poetry run domain-counter

lint:
	@poetry run flake8 domain_counter tests
	@poetry run mypy .

test:
	@poetry run pytest tests