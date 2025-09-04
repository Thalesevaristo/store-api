run:
	@uvicorn store.main:app --reload

precommit-install:
	@uv run pre-commit install

test:
	@uv run pytest

test-matching:
	@uv run pytest -s -rx -k $(K) --pdb store ./tests/
