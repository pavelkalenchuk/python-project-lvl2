install:
		poetry install

gendiff:
		poetry run gendiff

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --force-reinstall dist/*.whl

os-inst:
		python3 -m pip install --user --force-reinstall dist/*.whl

lint:
		poetry run flake8 gendiff

black:
		poetry run black gendiff