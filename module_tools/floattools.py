from odoo.tools import float_round

def float_is_same(f1, f2):
    f = [f1, f2]
    s = [str(f1), str(f2)]

    def get_len(s):
        if '.' not in s:
            s += '.0'
        return len(str(s).split(".")[1])

    def round_to_len(f):
        return float_round(f, precision_digits=minlen)

    lens = list(map(get_len, s))
    minlen = min(lens)
    f = list(map(round_to_len, f))
    return f[0] == f[1]
