import pytest

from medium.zigzag_conversion import Solution

cases = {
    ('PAYPALISHIRING', 1): 'PAYPALISHIRING',
    ('PAYPALISHIRING', 3): 'PAHNAPLSIIGYIR',
    ('PAYPALISHIRING', 4): 'PINALSIGYAHRPI',
    ('PAYPALISHIRING', 10): 'PAYPALGINSIHRI',
    ('A', 1): 'A',
    ('AB', 1): 'AB',
    ('AB', 4): 'AB'
}


@pytest.fixture(scope="function")
def solution():
    s = Solution()
    return s


@pytest.fixture(params=cases.items())
def case(request):
    return request.param


def test_zigzag_conversion_success(solution, case):
    arg1 = case[0][0]
    arg2 = case[0][1]
    expected = case[1]
    assert solution.convert(arg1, arg2) == expected
