from cal import squ


def main():
    test_squ()

def test_squ():
    assert squ(2) == 4
    assert squ(3) == 9

if __name__ == "__main__":
    main()