import unittest
from retriever import VectorRetriever

class TestRAG(unittest.TestCase):
    def test_search(self):
        r = VectorRetriever(["python backend api", "react frontend ui"])
        self.assertIn("python", r.query("backend api")["document"])

if __name__ == "__main__":
    unittest.main()
