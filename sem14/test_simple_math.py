import logging

import pytest

import simple_math

logger = logging.getLogger(__name__)
fh = logging.FileHandler("log.txt")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


# def test_add():
#     test_cases = [(4, 4), (10, 15), (-10, 10), (0.1, 0.2), (0.1, 0.2)]
#     test_answers = [8, 25, 0, 0.3, 0.3]

#     for case, answer in zip(test_cases, test_answers):
#         # assert abs(simple_math.add(case[0], case[1]) - answer) < 1e-8
#         assert simple_math.add(case[0], case[1]) == answer


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((4, 4), 8),
        ((10, 15), 25),
        ((-10, 10), 0),
        ((0.1, 0.2), 0.3),
        ((0.1, 0.2), 0.3),
        pytest.param((1, 1), 3, marks=pytest.mark.xfail),
    ],
)
def test_add(test_input, expected):
    # assert simple_math.add(test_input[0], test_input[1]) == expected
    assert (
        abs(simple_math.add(test_input[0], test_input[1]) - expected) < 1e-8
    )


@pytest.fixture(scope="session")
def resource_setup(request):
    logger.warning("Fixture setup")
    # db initialization
    db = {"red": 1, "blue": 2, "green": 3}

    def resource_teardown():
        logger.warning("Fixture teardown")
        # db cleanup
        db.clear()

    request.addfinalizer(resource_teardown)
    return db


def test_db_red(resource_setup):
    assert resource_setup["red"] == 1


def test_db_blue(resource_setup):
    assert resource_setup["blue"] == 2


def test_db_green(resource_setup):
    assert resource_setup["green"] == 3
