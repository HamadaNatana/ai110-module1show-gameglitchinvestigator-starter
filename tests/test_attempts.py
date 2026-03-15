import pytest

attempt_limit_map = {
    "Easy": 8,
    "Normal": 6,
    "Hard": 5,
}


def test_easy_attempts():
    assert attempt_limit_map["Easy"] == 8


def test_normal_attempts():
    assert attempt_limit_map["Normal"] == 6


def test_hard_attempts():
    assert attempt_limit_map["Hard"] == 5
