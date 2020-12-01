import argparse


def add(x, y):
    """Simple addition.

    Not intended for complex numbers...

    Parameters
    ----------
    x : float
        Argument 1
    y : float
        Argument 2

    Returns
    -------
    sum : float
        Sum of x and y
    """
    return x + y


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", required=True, help="First argument", type=float)
    parser.add_argument("-y", required=True, help="Second argument", type=float)
    parser.add_argument("-o", required=True, help="Operation", type=str,
                        choices=["+"])
    args = parser.parse_args()

    if args.o == '+':
        print(f'{args.x} {args.o} {args.y} = {add(args.x, args.y)}')

    print('Program End')
