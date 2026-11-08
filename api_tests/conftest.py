import pytest

@pytest.fixture(params=[
    (2, 3),                    # два положительных
    (-1, 5, -3),               # разные знаки
    (0, 0, 5, 0),              # с нулями
    (10, -2, 0, 4, -1),        # несколько чисел
])
def numbers(request):
    return request.param