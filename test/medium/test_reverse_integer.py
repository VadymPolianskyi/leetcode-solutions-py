import pytest

from medium.reverse_integer import Solution

cases = {
    123: 321,
    -123: -321,
    120: 21,
    0: 0,
    1: 1,
    -123456789: -987654321,
    -1: -1,
    -300: -3,
    -5: -5,
    1534236469: 0
}


@pytest.fixture(scope="function")
def solution():
    s = Solution()
    return s


@pytest.fixture(params=cases.items())
def case(request):
    return request.param


def test_success(solution, case):
    arg = case[0]
    expected = case[1]
    assert solution.reverse(arg) == expected


def test_chec():
    x = 1534236469

    is_not_32 = x >= 2 ** 31 - 1 or x <= -2 ** 31
    assert is_not_32
