test *ARGS:
	pytest -v {{ARGS}}

install-dev:
	pip install -r requirements.txt

clean:
	rm -rf .pytest_cache */__pycache__
