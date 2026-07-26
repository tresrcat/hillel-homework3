class CandyStash:
    MAX_CAPACITY = 50
    @staticmethod
    def validate_amount(value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Кількість цукерок має бути цілим невід'ємним числом.")
    def __init__(self, count):
        CandyStash.validate_amount(count)
        if count > self.MAX_CAPACITY:
            self._count = self.MAX_CAPACITY
        else:
            self._count = count
    @classmethod
    def full_stash(cls):
        return cls(cls.MAX_CAPACITY)
    @property
    def count(self):
        return self._count
    @count.setter
    def count(self, value):
        CandyStash.validate_amount(value)
        if value > self.MAX_CAPACITY:
            self._count = self.MAX_CAPACITY
        else:
            self._count = value
    def __str__(self):
        return f"CandyStash ({self._count}/50)"
    def __repr__(self):
        return self.__str__()
    def __add__(self, other):
        if isinstance(other, int):
            if other < 0:
                raise ValueError("Не можна додавати від'ємну кількість цукерок.")
            total = self._count + other
            return CandyStash(total)
    def __sub__(self, other):
        if isinstance(other, int):
            if other < 0:
                raise ValueError("Не можна віднімати від'ємну кількість цукерок.")
            total = self._count - other
            if total < 0:
                total = 0
            return CandyStash(total)
    def __eq__(self, other):
        if isinstance(other, CandyStash):
            return self._count == other._count
        if isinstance(other, int):
            return self._count == other
        return False
#Перевірка 
stash = CandyStash(20)
full = CandyStash.full_stash()
print(stash)  # CandyStash (20/50)
print(full)   # CandyStash (50/50)
stash.count = 65
print(stash.count)  # 50
small_stash = CandyStash(10)
more_candies = small_stash + 15
print(more_candies)  # CandyStash (25/50)
overflow = small_stash + 100
print(overflow)  # CandyStash (50/50)
empty_stash = small_stash - 30
print(empty_stash)  # CandyStash (0/50)
stash1 = CandyStash(15)
stash2 = CandyStash(15)
print(stash1 == stash2)  # True
print(stash1 == 15)     # True
print(stash1 == 20)     # False