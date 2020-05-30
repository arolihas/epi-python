def multiply(x, y):
    def add(a, b):
        run, cin, k, tmp_a, tmp_b = 0, 0, 1, a, b
        while tmp_a or tmp_b:
            ak = a & k
            bk = b & k
            cout = (ak & bk) | (ak & cin) | (bk & cin)
            run |= ak ^ bk ^ cin
            cin, k  = cout << 1, k << 1
            tmp_a, tmp_b = tmp_a >> 1, tmp_b >> 1
        return run | cin
    
    runsum = 0
    while x:
        if x & 1:
            runsum = add(runsum, y)
        x, y = x >> 1, y << 1 
    return runsum
