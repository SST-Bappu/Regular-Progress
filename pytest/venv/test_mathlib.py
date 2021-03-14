import mathlib
import pytest
import sys

#@pytest.mark.skip(reason="This is not my priority right now!")
#@pytest.mark.skipif(sys.version_info < (3,5), reason="This is not priority right now!")
def test_calc_total():
    total = mathlib.calc_total(5,4)
    assert total ==9

def test_calc_multiply():
    total = mathlib.calc_multiply(3,10)
    assert total ==30
