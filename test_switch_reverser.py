from unittest import TestCase
from switch_reverser import list_check


class Tests(TestCase):
    def test_reverse_list(self):
        self.assertEqual(list_check([1, 2, 3, 4, 5, 6, 7, 8, 9]), [9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(list_check(["Air", "God", "Jesus", "Developer", "Man"]),
                         ["AIR", "GOD", "JESUS", "DEVELOPER", "MAN"])
        self.assertEqual(list_check([2, 8, ("Arnold", 24), "Books"]), [2, 8, ("Arnold", 24), "Books"])
