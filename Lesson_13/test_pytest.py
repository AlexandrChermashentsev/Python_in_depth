from class_user import User
import pytest


def test_type():
    with pytest.raises(TypeError):
        User(111000, 43, 2)
        User('milk_nagibator', 777, 7)
        User('Alex22.2', 22.2, 2)
        User('Will', '22', 2)

def test_value():
    with pytest.raises(ValueError):
        User('Will', 22, 12)
        User('Joe', 99, 0)

def test_value_with_text():
    pytest.raises(ValueError, 
                  User('Joe', 99, -1), 
                  match=r'Уровень доступа должен быть в диапазоне от 1 до 7')


if __name__ == '__main__':
    pytest.main(['-v'])