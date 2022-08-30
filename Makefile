ve:
	test ! -d .ve && python3.9 -m venv .ve; \
	. .ve/bin/activate; \
	.ve/bin/pip3 install -r requirements.txt

clean_ve:
	test -d .ve && rm -rf .ve

install_packages:
	sh install_packages.sh

run:
	python3 run.py

test:
	pytest

test_dev:
	pytest -s -vv
