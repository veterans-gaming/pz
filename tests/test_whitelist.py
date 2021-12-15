from pz import database
import unittest


class TestWhitelistTable(unittest.TestCase):

    def setUp(self):
        self.whitelist_table = database.WhitelistTable(db="C:\\users\\mark\\PycharmProjects\\pz\\servertest.db")

    def test_get_users(self):
        result = self.whitelist_table.get_users()
        self.assertIsNotNone(result)

    def test_get_user_valid(self):
        result = self.whitelist_table.get_user("death")
        self.assertIsNotNone(result)

    def test_get_user_invalid(self):
        result = self.whitelist_table.get_user("deth")
        self.assertIsNone(result, msg="Get user should return None on no match")

    def test_user_in(self):
        self.assertIn("death", self.whitelist_table)

    def test_user_not_in(self):
        self.assertNotIn("deth", self.whitelist_table)


if __name__ == '__main__':
    unittest.main()
