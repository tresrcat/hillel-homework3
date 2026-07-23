class CandyStash:
    MAX_CAPACITY = 50
    @staticmethod
    def validate_amount(value):
        """Перевіряє, що значення є цілим невід'ємним числом."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Кількість цукерок має бути цілим невід'ємним числом.")
    def __init__(self, count: int):
        self.validate_amount(count)
        self._count = min(count, self.MAX_CAPACITY)
    @classmethod
    def full_stash(cls):
        """Створює рюкзак одразу з максимальною кількістю цукерок."""
        return cls(cls.MAX_CAPACITY)
    @property
    def count(self) -> int:
        """Гетер для кількості цукерок."""
        return self._count
    @count.setter
    def count(self, value: int):
        """Сетер, який валідує значення та обмежує його до MAX_CAPACITY."""
        self.validate_amount(value)
        self._count = min(value, self.MAX_CAPACITY)
    def __str__(self) -> str:
        return f"CandyStash ({self._count}/{self.MAX_CAPACITY})"
    def __repr__(self) -> str:
        return f"CandyStash({self._count})"
    def __add__(self, other: int):
        """Додає цукерки до рюкзака, не перевищуючи максимум."""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise ValueError("Не можна додавати від'ємну кількість цукерок.")
        new_count = min(self._count + other, self.MAX_CAPACITY)
        return CandyStash(new_count)
    def __sub__(self, other: int):
        """Забирає цукерки з рюкзака, обрізаючи результат знизу до 0."""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise ValueError("Не можна віднімати від'ємну кількість цукерок.")
        new_count = max(self._count - other, 0)
        return CandyStash(new_count)
    def __eq__(self, other) -> bool:
        """Порівнює за кількістю цукерок з іншим CandyStash або з числом int."""
        if isinstance(other, CandyStash):
            return self._count == other.count
        if isinstance(other, int):
            return self._count == other
        return False
stash = CandyStash(20)
full = CandyStash.full_stash()
print(stash)  # CandyStash (20/50)
print(full)   # CandyStash (50/50)
stash.count = 65
print(stash.count)   
small_stash = CandyStash(10)
more_candies = small_stash + 15
print(more_candies)  # CandyStash (25/50)
overflow = small_stash + 100
print(overflow)  # CandyStash (50/50) 
empty_stash = small_stash - 30
print(empty_stash)  
stash1 = CandyStash(15)
stash2 = CandyStash(15)
print(stash1 == stash2)  # True 
print(stash1 == 15)      # True 
print(stash1 == 20)      # False

