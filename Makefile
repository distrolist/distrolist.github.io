all: clean create
clean:
	rm -rf build
create:
	python3 main.py
update:
	python3 update_distro.py
