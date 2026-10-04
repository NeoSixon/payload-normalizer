# payload-normalizer

Small Python utilities for normalizing metadata fields from API payloads before they are stored or compared.

## Tag normalization contract

`normalize_tags()` should:

- trim surrounding whitespace;
- lowercase tags;
- ignore `None` and blank entries;
- remove duplicates; and
- preserve the order in which each normalized tag first appears.

Example:

```python
from payload_normalizer import normalize_tags

normalize_tags([" Python ", None, "API", "python", " "])
# expected: ["python", "api"]
```

## Running the tests

The project uses only the Python standard library for its test suite:

```bash
python -m unittest discover -s tests -v
```

## License

MIT
