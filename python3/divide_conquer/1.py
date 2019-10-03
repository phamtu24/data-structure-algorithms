def karatsuba(x,y):
    lenX = len(str(x))
    lenY = len(str(y))
    if lenX == 1 or lenY == 1:
        return x*y
    else:
        n = max(lenX,lenY)
        nby2 = int(n / 2)
        a = int(x / 10**(nby2))
        b = x % 10**(nby2)
        c = int(y / 10**(nby2))
        d = y % 10**(nby2)
                        
                                
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
                        
                                
        result = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
        return result

print(karatsuba(12,100))
