import pytest

def test_loop_calculation():
    u = 2
    v = 3
    k = 5
    
    a, b = u, v
    
    for i in range(2, k + 1):
        a = 2 * b + a
        b = 2 * b * b + b
    
    assert a == 3265298
    assert b == 5325028475403