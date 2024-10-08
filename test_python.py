#Пример тестов для filter, map, sorted:
def test_filter():
    assert list(filter(lambda x: x > 2, [1, 2, 3, 4])) == [3, 4]
    assert list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])) == [2, 4]
    assert list(filter(None, [0, 1, False, 3])) == [1, 3]

def test_map():
    assert list(map(lambda x: x * 2, [1, 2, 3, 4])) == [2, 4, 6, 8]
    assert list(map(lambda x: x ** 2, [1, 2, 3, 4])) == [1, 4, 9, 16]
    assert list(map(str.upper, ['a', 'b', 'c'])) == ['A', 'B', 'C']

def test_sorted():
    assert sorted([4, 1, 3, 2]) == [1, 2, 3, 4]
    assert sorted(['banana', 'apple', 'cherry']) == ['apple', 'banana', 'cherry']
    assert sorted([{'name': 'John', 'age': 45}, {'name': 'Jane', 'age': 30}], key=lambda x: x['age']) == [{'name': 'Jane', 'age': 30}, {'name': 'John', 'age': 45}]

#Пример тестов для math:
import math

def test_pi():
    assert math.pi == 3.141592653589793

def test_sqrt():
    assert math.sqrt(4) == 2
    assert math.sqrt(9) == 3
    assert math.sqrt(0) == 0

def test_pow():
    assert math.pow(2, 3) == 8
    assert math.pow(3, 3) == 27
    assert math.pow(10, 0) == 1

def test_hypot():
    assert math.hypot(3, 4) == 5
    assert math.hypot(5, 12) == 13
    assert math.hypot(0, 0) == 0
