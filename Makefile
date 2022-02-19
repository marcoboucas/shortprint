package_name = shortprint
lint:
	python -m pylint $(package_name) --disable=W0511
	python -m mypy $(package_name)
	python -m flake8 $(package_name)

test:
	pytest


install:
	pip install -r requirements.txt
install-dev: install
	pip install -r requirements-dev.txt  # Development dependencies
	pip install -r ./docs/requirements.txt  # Doc dependencies
	pre-commit install
	pre-commit install --hook-type commit-msg


clean:
	rm -r test.* test2.* build dist ./**/$(package_name).egg-info

clean-package:
	rm -r build dist ./**/$(package_name).egg-info &

package: clean-package
	pip install wheel
	python setup.py sdist bdist_wheel

ship-test:
	pip install twine --quiet
	python -m twine upload --repository testpypi dist/*

ship:
	pip install twine --quiet
	python -m twine upload dist/*

coverage:
	py.test --cov=$(package_name) --cov-report=xml:coverage.xml  tests/
coverage-report:
	pytest --cov=$(package_name) --cov-report=html tests/
	cd htmlcov && start "http://localhost:8000" && python -m http.server


doc:
	doc.bat html

check:
	python scripts/special_pre_commit.py