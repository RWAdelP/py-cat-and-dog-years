import pytest

from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (15, 0, [1, 0]),
        (0, 15, [0, 1]),
        (24, 0, [2, 0]),
        (0, 24, [0, 2]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_all_boundary_ages(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
        ), f"{cat_age} cat years, should be {result[0]} human years, {dog_age} dog years should be {result[1]} human years."
    
"""
def test_zero_ages():
    assert get_human_age(0, 0) == [0, 0]
def test_first_boundary_cat():
    # 15 cat years = 1 human year
    assert get_human_age(15, 0) == [1, 0]
def test_first_boundary_dog():
    # 15 dog years = 1 human year
    assert get_human_age(0, 15) == [0, 1]
def test_second_boundary_cat():
    # 15 + 9 = 24 cat years = 2 human years
    assert get_human_age(24, 0) == [2, 0]
def test_second_boundary_dog():
    # 15 + 9 = 24 dog years = 2 human years
    assert get_human_age(0, 24) == [0, 2]
"""