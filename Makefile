# Various needed programs
PYTHON3 = python3

FIND_FILES = bin/find-files

.PHONY: dist clean install

dist: docs $(shell $(FIND_FILES) --ext=.py src)
	@ $(PYTHON3) src/build_dist.py

docs: $(shell $(FIND_FILES) --ext=.html --ext=.png src)
	@ $(PYTHON3) src/render_docs.py

install: dist
	@ $(PYTHON3) src/install_dist.py

clean:
	@ echo "[CLEANING]"
	@ rm -rf src/__pycache__ src/*/__pycache__ bin/__pycache__ generated dist
	@ echo "[DONE]"
