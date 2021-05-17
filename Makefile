all: clean create
clean:
	rm -rf build
	rm -rf site
create:
	python3 main.py
	make -C site-builder build
