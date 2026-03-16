import pytest
from ..logic_utils import update_score

def test_update_score_win():
    assert update_score(100, "Win", 1) == 90

def test_update_score_too_high():
    assert update_score(100, "Too High", 1) == 95

def test_update_score_too_low():
    assert update_score(100, "Too Low", 1) == 95