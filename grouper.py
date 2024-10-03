import argparse

parser = argparse.ArgumentParser(
    prog='grouper',
    description='find fishy friends from familiar folds',
    epilog='See https://github.com/dorianclay/grouper for more info.'
)

parser.add_argument('filename',
                    help='The file to read users from',
                    type=argparse.FileType('r+'))
parser.add_argument('-s', '--size',
                    help='The target size of groups to create',
                    type=int)
parser.add_argument('-o', '--output',
                    help='The output file to write to',
                    type=argparse.FileType('w'))

args = parser.parse_args()

