codespell:
	codespell -w $(shell git ls-files)

codespell-check:
	codespell $(shell git ls-files)

flake8:
	flake8 viewer

format:
	black viewer

format-check:
	black --diff --check viewer

pyupgrade:
	pyupgrade --py3-only --py38-plus $(shell git ls-files | grep .py)
