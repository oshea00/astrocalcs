
def easter_date(year):
    _, a = divmod(year,19)
    b, c = divmod(year,100)
    d, e = divmod(b,4)
    f, _ = divmod(b+8,25)
    g, _ = divmod(b-f+1,3)
    _, h = divmod(19*a + b - d - g + 15,30)
    i, k = divmod(c,4)
    _, l = divmod(32 + 2*e + 2*i - h - k,7)
    m, _ = divmod(a + 11*h + 22*l, 451)
    n, p = divmod(h + l - 7*m + 114,31)
    month = n
    day = p + 1
    return month, day

def divmod(dividend, divisor):
    d = dividend/divisor
    return int(d), dividend-int(d)*int(divisor)