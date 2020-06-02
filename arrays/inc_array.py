def increment_array(digits):
    digits[-1] += 1
    inc = digits[-1]
    i = len(digits) - 1
    while (inc == 10 and i > 0):
        digits[i] == 0
        i -= 1
        digits[i] += 1 
        inc = digits[i]
    if (i == 0 and digits[0] == 10):
        digits[0] = 1
        digits.append(0)
    
    
