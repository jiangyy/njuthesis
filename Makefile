all:
	python3 res/render.py
	lyx -E pdf4 example.pdf example/main.lyx

clean:
	rm -rf build
