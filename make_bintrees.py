# file: make_bintrees.py
# Andrew Jarcho
# 2017-10-31


import sys


def parse(A, ix, out):
    if ix >= len(A):
        return ''
    out += '{"value":' + A[ix] + ','  # process root
    left_ix = ix * 2 + 1
    if left_ix < len(A):
        out += '"left":'  # process left child
        if A[left_ix] == 'x':
            out += 'null'
        else:
            out = parse(A, left_ix, out)
    else:
        out += '"left":null'
    out += ','  # between left child and right child
    right_ix = ix * 2 + 2
    if right_ix < len(A):
        out += '"right":'  # process right child
        if A[right_ix] == 'x':
            out += 'null'
        else:
            out = parse(A, right_ix, out)
    else:
        out += '"right":null'
    return out + '}'  # after right child


if __name__ == '__main__':
    with open(sys.argv[1]) as infile:
        in_list = []
        for line in infile:
            line = line.rstrip().split()
            in_list.extend(line)
    print(parse(in_list, 0, ''))
