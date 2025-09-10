requirements: requirements.txt
	python3 -m venv .venv
	./.venv/bin/pip install -r requirements.txt
	# ensure PEP517 build tool is available for packaging from pyproject.toml
	./.venv/bin/pip install --upgrade build

requirements-test: requirements-test.txt
	python3 -m venv .venv
	./.venv/bin/pip install -r requirements-test.txt
	# ensure PEP517 build tool is available for packaging from pyproject.toml
	./.venv/bin/pip install --upgrade build

clean:
	find . -type f -name '*.pyc' -delete
	rm -rf .venv

test: requirements-test
	./.venv/bin/python manage.py test tests

coverage:
	./.venv/bin/coverage run --source='toconline' manage.py test tests
	./.venv/bin/coverage report -m

build: clean requirements
	# Use PEP 517 build (reads pyproject.toml). produces sdist and wheel in dist/
	./.venv/bin/python -m build --sdist --wheel

pypi: build
	./.venv/bin/python -m twine upload dist/* --config-file ~/.pypirc

test-pypi: build
	./.venv/bin/python -m twine upload --verbose --repository testpypi dist/* --config-file ~/.pypirc
