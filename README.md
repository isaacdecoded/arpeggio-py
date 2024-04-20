<p align="center">
  <img src="../misc/0-Arpeggio-on-Python.png" loading="lazy"/>
</p>

# ARPEGGIO ON PYTHON

This is the [Arpeggio](https://github.com/isaacdecoded/arpeggio) coding template based on [Python](https://www.python.org/).

### Requirements
- [Poetry](https://python-poetry.org/docs)

### Scripts

You can execute it by using Poetry:

```bash
poetry install
poetry run python src/main.py
```

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

You can also manually evaluate the pre-commit-config.yaml rules by running the following command:
```bash
poetry run pre-commit run --all-files
```

### Dependencies

Arpeggio on Python keeps the codebase clean by including only the minor requirement tooling dependency as they are _asyncio_ for asynchronicity features and _pytest_ for testing.

## The Plan Concept example

You can take a look to the example by visiting the [plan-concept-example](https://github.com/isaacdecoded/arpeggio-py/tree/plan-concept-example) branch
