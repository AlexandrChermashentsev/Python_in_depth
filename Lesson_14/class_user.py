class User:
    def __init__(self, name: str, u_id: int, level: int = 1):
        if not isinstance(name, str) or not name.isalpha():
            raise TypeError('Имя должно быть текстового вида')
        self.name = name

        if not isinstance(u_id, int):
            raise TypeError('Личный идентификатор должен быть целым числом')
        self.u_id = u_id

        if not isinstance(level, int):
            raise TypeError('Уровень доступа должен быть целым числом')
        elif int(level) < 1 or int(level) > 7:
            raise ValueError('Уровень доступа должен быть в диапазоне от 1 до 7 включительно')
        self.level = level

    def __str__(self) -> str:
        return f'{self.name = }, {self.u_id = }, {self.level = }'
    
    def __eq__(self, other) -> bool:
        return all((self.name == other.name,  self.u_id == other.u_id))

    def __hash__(self):
        return hash(self.name) + hash(self.u_id)


# user1 = User('Joe', 99, -1)