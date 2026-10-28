run:
	uv run main.py

install:
	uv sync

clean:
	rm -rf .venv uv.lock
	find . -name __pycache__ -exec rm -rf {} +

re: clean install

.PHONY: run install clean re
