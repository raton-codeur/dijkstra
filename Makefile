run:
	mkdir -p states
	rm -rf states/*.png
	uv run main.py

install:
	uv sync

clean:
	rm -rf .venv uv.lock states
	find . -name __pycache__ -exec rm -rf {} +

re: clean install

.PHONY: run install clean re
