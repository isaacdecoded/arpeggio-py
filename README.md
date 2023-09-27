# ARPEGGIO ON PYTHON

This template is based on [Poetry](https://python-poetry.org/docs/). In order to start using it, execute the following command:

```bash
poetry install
poetry run python src/main.py
```

### Requirements
- [Poetry](https://python-poetry.org/docs)

### Tests

Execute tests by using the [Pytest](https://docs.pytest.org/en/7.4.x/) included library:

```bash
poetry run pytest
```

### Pre-Commit configurations
To install/refresh the pre-commit-config.yaml file over the .git/hooks, run the following command:
```bash
poetry run pre-commit install
```

To run/simulate the pre-commit-config.yaml file behaviors, run the following command:
```bash
poetry run pre-commit run --all-files
```
