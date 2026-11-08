def add_numbers(*args):
    return sum(args)


def test_add_numbers(numbers):
    result = add_numbers(*numbers)
    expected = sum(numbers)
    assert result == expected