from cal import squ


def main():
    test_squ()

def test_squ():
    try:
        assert squ(2) == 4
    except AssertionError:
        print("2 is not square of 4")
    try:
        assert squ(3) == 9
    except AssertionError:
        print("3 is not square of 9")
    try:
        assert squ(0) == 0
    except AssertionError:
        print("0 is not square of 0")

if __name__ == "__main__":
    main()