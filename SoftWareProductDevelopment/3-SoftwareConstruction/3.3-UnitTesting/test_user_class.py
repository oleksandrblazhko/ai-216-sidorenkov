import unittest
from user_class import User

class TestUser(unittest.TestCase):
    def test_request_support(self):
        user = User(1, "Іван", "ivan@example.com")
        result = user.request_support("довідка")
        self.assertEqual(result["status"], "created")
        self.assertEqual(result["type"], "довідка")
        self.assertEqual(result["user"], "Іван")

if __name__ == "__main__":
    unittest.main()
