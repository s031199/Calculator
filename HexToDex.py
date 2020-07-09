def hexadecimalToDecimal(hexval):
    length = len(hexval)
    base = 1
    dec_val = 0

    for i in range(length - 1, -1, -1):
        if '0' <= hexval[i] <= '9':
            dec_val += (ord(hexval[i]) - 48) * base
            base = base * 16
        elif 'A' <= hexval[i] <= 'F':
            dec_val += (ord(hexval[i]) - 55) * base
            base = base * 16
    return dec_val
