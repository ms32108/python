from cal import squ

def test_squ():
    assert squ(2) == 4
    assert squ(3) == 9
    assert squ(-2) == 4
    assert squ(-3) == 9
    assert squ(0) == 0


"""
py -m pip install pytest
py -m pip show pytest(verify installation)
py -m pip list (show all pkgs)

"""
#RUN - pytest cal_pytest.py