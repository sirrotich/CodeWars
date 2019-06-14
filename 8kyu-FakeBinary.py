# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.







def fake_bin(x):
    b = []
    for w in x:
        if int(w) > 4:
            b.append('1')
        elif int(w) < 5:
            b.append('0')
    return "".join(b)