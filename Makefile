project := iterable
coverage_args := --cov=$(project)

bootstrap:
		pip install -e .
		pip install --upgrade pip
		pip install -r requirements.txt

test:
		py.test $(coverage_args) tests

lint:
		flake8 $(project) tests
