'''
📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень)
📌 Напишите 3-7 тестов pytest (или unittest на ваш выбор) для данного проекта
📌 ОБЯЗАТЕЛЬНО! Используйте фикстуры
'''
from class_user import User
import unittest
from unittest.mock import patch


class TestUnitMy(unittest.TestCase):
    def setUp(self):
        self.first_user = User('Alex', 123, 4)
        self.second_user = User('Alex', 323, 6)


    def test_not_eq(self):
        self.assertFalse(self.first_user == self.second_user)

    def test_eq(self):
        self.assertTrue(self.first_user == User('Alex', 123, 4))

    def test_value(self):
        with self.assertRaises(ValueError):
            User('Will', 22, 12)
            User('Joe', 99, -1)

    def test_type(self):
        with self.assertRaises(TypeError):
            User(111000, 43, 2)
            User('milk_nagibator', 777, 7)
            User('Alex22.2', 22.2, 2)
            User('Will', '22', 2)



if __name__ == '__main__':
    unittest.main(verbosity=2)