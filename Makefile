install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=lib test_*.py &&\
	python -m pytest --nbval analysis.ipynb

format:	
	black *.py 

movefile:
	mkdir -p excluded_files
	mv ./test_lib.py excluded_files/
	mv ./test_script.py excluded_files/

restorefile:
	mv excluded_files/* .
	rmdir excluded_files

lint:
	make movefile
	ruff check ./*.py
	make restorefile 
all: install lint format test 