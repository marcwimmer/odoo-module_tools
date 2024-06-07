from odoo.tools import float_round
from decimal import Decimal


def float_is_same(f1, f2, precision_rounding=None, tolerance=None):
    f = list(map(Decimal, [f1, f2]))
    if precision_rounding:
        digits = len(str(Decimal(str(precision_rounding))).split(".")[1])
        f = list(map(lambda x: round(x, digits), f))
    s = [str(f1), str(f2)]

    def get_len(s):
        if "." not in s:
            s += ".0"
        return len(str(s).split(".")[1])

    def round_to_len(f):
        return float_round(float(f), precision_digits=minlen)

    lens = list(map(get_len, s))
    minlen = min(lens)
    f = list(map(round_to_len, f))
    if f[0] == f[1]:
        return True
    if not tolerance:
        return False
    diff = abs(f[0] - f[1])
    return diff < tolerance

