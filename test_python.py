import math

def test_filter():
    assert list(filter(lambda x: x > 0, [-46, -24, 0, 11, 23])) == [11, 23], 'Не то!'
    assert list(filter(lambda x: -18 < x < 16, [-22, -18, 0, 11, 16, 22])) == [0, 11], 'Не то!'

def test_map():
    assert list(map(lambda x: x//2, [5, 29, 37])) == [2, 14, 18], 'Не правда!'
    assert list(map(int, ['11', '17', '39'])) == [11, 17, 39], 'Не правда!'

def test_sorted():
    # Сортировка строки
    assert sorted('привет') == ['в', 'е', 'и', 'п', 'р', 'т'], 'Провал'
    assert sorted(('привет'), reverse=True) == ['т', 'р', 'п', 'и', 'е', 'в'], 'Провал'
    # Сортировка списка
    assert sorted([1, 6, 12, 436, 22, 168]) == [1, 6, 12, 22, 168, 436], 'Провал'
    assert sorted([1, 6, 12, 44, 55, 66], reverse=True) == [66, 55, 44, 12, 6, 1], 'Провал'

def test_pi():
    assert round(math.pi, 4) == 3.1416, 'Не правильно!'

def test_sqrt():
    assert math.sqrt(2) == 2**(0.5), 'Не правильно!'
    assert round(math.sqrt(48)) == 7, 'Не правильно!'

def test_pow():
    assert math.pow(2, 0.5) == 2 ** 0.5, 'Это ложь!'
    assert math.pow(3, 2) == 9, 'Это ложь!'
    assert math.pow(1.5, 3) == 3.375, 'Это ложь!'
    assert math.pow(4, -1) == 0.25, 'Это ложь'
    assert math.pow(4, -0.5) == 0.5, 'Это ложь!'
    assert round(math.pow(1.5, 3.5,),3) == 4.134, 'Это ложь!'

def test_hypot():
    assert math.hypot(4, 41) == 41.19465984809196, 'Кривда!'
    assert math.hypot(-1, 2) == 2.23606797749979, 'Кривда!'
    assert math.hypot(-2, 0) == 2.0, 'Не реально!'



