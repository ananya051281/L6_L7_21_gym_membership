
import pytest
from hypothesis import given, strategies as st
from gym_membership import parse_plan, calculate_bmi, average_workout


# FUZZ TESTS: Check that unexpected inputs never crash


@given(st.text() | st.none())
def test_parse_plan_no_crash(s):
    result = parse_plan(s)
    assert result is None or (
        isinstance(result, tuple) and len(result) == 2
    )


@given(st.text() | st.none())
def test_calculate_bmi_no_crash(s):
    result = calculate_bmi(s)
    assert result is None or isinstance(result, float)


@given(st.text() | st.none())
def test_average_workout_no_crash(s):
    result = average_workout(s)
    assert result is None or isinstance(result, int)


# VALID INPUT TESTS


def test_parse_plan_valid():
    assert parse_plan("GOLD-12") == ("GOLD", 12)


def test_calculate_bmi_valid():
    assert calculate_bmi("70,1.75") == 22.9


def test_average_workout_valid():
    assert average_workout("45 60 30") == 45


# INVALID INPUT TESTS


@pytest.mark.parametrize("value", [
    None, "", "GOLD", "GOLD-abc", "-12", "GOLD-0"
])
def test_parse_plan_invalid(value):
    assert parse_plan(value) is None


@pytest.mark.parametrize("value", [
    None, "", ",", "abc,1.75", "70,0", "70,nan"
])
def test_calculate_bmi_invalid(value):
    assert calculate_bmi(value) is None


@pytest.mark.parametrize("value", [
    None, "", "abc", ":", "-1 20"
])
def test_average_workout_invalid(value):
    assert average_workout(value) is None
