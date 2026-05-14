import pytest
import sys
sys.path.insert(0, 'c:/GitHubb/ProgStud/lab_4')
from task_1 import find

def test_find_existing_number():
    mas = [1, 2, [3, 4, [5, [6, []]]]]
    assert find(mas, 4) == 3

def test_find_non_existing_element():
    mas = [1, 2, [3, 4, [5, [6, []]]]]
    assert find(mas, 'spam') is None
