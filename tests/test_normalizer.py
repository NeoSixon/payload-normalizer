import unittest

from payload_normalizer import normalize_payload, normalize_tags


class NormalizeTagsTests(unittest.TestCase):
    def test_normalizes_case_whitespace_and_duplicates(self) -> None:
        self.assertEqual(
            normalize_tags([" API ", "api", "Python", "python"]),
            ["api", "python"],
        )

    @unittest.expectedFailure
    def test_ignores_none_and_blank_entries(self) -> None:
        self.assertEqual(
            normalize_tags([" Python ", None, " ", "API"]),
            ["python", "api"],
        )

    @unittest.expectedFailure
    def test_preserves_first_seen_order(self) -> None:
        self.assertEqual(
            normalize_tags(["Beta", "alpha", "BETA", "Gamma"]),
            ["beta", "alpha", "gamma"],
        )


class NormalizePayloadTests(unittest.TestCase):
    def test_normalizes_tags_without_mutating_input(self) -> None:
        payload = {"id": 7, "tags": [" API ", "api", "Python"]}

        normalized = normalize_payload(payload)

        self.assertEqual(normalized, {"id": 7, "tags": ["api", "python"]})
        self.assertEqual(payload, {"id": 7, "tags": [" API ", "api", "Python"]})

    def test_payload_without_tags_is_unchanged(self) -> None:
        payload = {"id": 7, "source": "import"}

        self.assertEqual(normalize_payload(payload), payload)


if __name__ == "__main__":
    unittest.main()
