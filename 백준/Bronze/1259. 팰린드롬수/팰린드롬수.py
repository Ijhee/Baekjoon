while True:
    N=int(input())
    str_N=list(str(N))
    if N != 0:
        if str_N == str_N[::-1]:
            print('yes')
        else:
            print('no')
    else:
        break