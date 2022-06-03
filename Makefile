install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

domain-counter:
	poetry run domain-counter

lint:
	@poetry run flake8 domain_counter tests
	@poetry run mypy . --ignore-missing-imports

test:
	poetry run coverage run --source=domain_counter -m pytest tests

test-coverage:
	poetry run coverage xml
