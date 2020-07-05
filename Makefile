# Various needed programs
PYTHON3 = python3

FIND_FILES = bin/find-files

.PHONY: dist clean install

# note we just build on any changed extension, this might be unwise, but is better than tracking down every possible webfont, js, image type etc
dist: $(shell $(FIND_FILES) --ext=.py --ext=.* src)
	@ $(PYTHON3) src/build_dist.py

install: dist
	@ $(PYTHON3) src/install_dist.py

clean:
	@ echo "[CLEANING]"
	@ rm -rf src/__pycache__ src/*/__pycache__ bin/__pycache__ generated dist
	@ echo "[DONE]"
