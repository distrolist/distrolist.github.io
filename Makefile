all: clean create
clean:
	rm -rf build
create:
	python3 main.py
