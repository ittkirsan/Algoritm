'''Реализация Ассоциативного массива и его функций.'''
from typing import Any


class NativeDictionary:
    '''Класс представления ассоциативного массива.'''

    def __init__(self, sz: int):
        '''Иницилизация ассоциативного массива.'''
        self.size = sz
        self.slots = [None] * self.size  # для хранения ключей
        self.values = [None] * self.size  # для хранения значений

    def hash_fun(self, key: str):
        '''Хеш-функция, оределяет индекс.'''
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        if not isinstance(key, str):
            return None
        return sum(key.encode()) % self.size

    def is_key(self, key: str):
        '''Метод проверяет емеется ли ключ в слотах.'''
        # возвращает True если ключ имеется,
        # иначе False
        if not isinstance(key, str):
            return None
        if key in self.slots:
            return True
        return False

    def put(self, key: str, value: Any):
        '''Метод сохраненяет внутри класса ассоциативного массива пары ключ-значение.'''
        if not isinstance(key, str):
            return None

        if self.is_key(key):
            self.values[self.hash_fun(key)] = value
        else:
            self.slots[self.hash_fun(key)] = key
            self.values[self.hash_fun(key)] = value
        # гарантированно записываем
        # значение value по ключу key

    def get(self, key: str):
        '''Метод поиска и извлечения значения по ключу, или None, если ключ не найден.'''
        # возвращает value для key,
        # или None если ключ не найден
        if not isinstance(key, str):
            return None
        if self.is_key(key):
            return self.values[self.hash_fun(key)]
        return None
