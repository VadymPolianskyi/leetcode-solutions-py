import pytest

from easy.palindrome_number import Solution

success_cases = [
    121,
    3443,
    1234567887654321,
    0,
    1,
    11
]

failed_cases = [
    -1,
    134323,
    123,
    -49,
    10000,
    11221133,
    111111111110,
    10,
    -121
]


@pytest.fixture(scope="function")
def solution():
    s = Solution()
    return s


@pytest.fixture(params=success_cases)
def success_case(request):
    return request.param


@pytest.fixture(params=failed_cases)
def fail_case(request):
    return request.param


def test_palindrome_number_success(solution, success_case):
    assert solution.isPalindrome(success_case) is True


def test_palindrome_number_failures(solution, fail_case):
    assert solution.isPalindrome(fail_case) is False
