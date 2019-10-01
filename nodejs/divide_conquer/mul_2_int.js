const karatsuba = (x, y) => {
    let lenX = x.toString().length;
    let lenY = y.toString().length;

    if (lenX == 1 || lenY == 1) {
        return x*y;
    } else {
        let n = Math.max(lenX, lenY);
        let nby2 = parseInt(n/2);

        let a = parseInt(x / 10**(nby2));
        let b = x % 10**nby2;
        let c = parseInt(y / 10**(nby2));
        let d = y % 10**nby2;

        let ac = karatsuba(a, c);
        let bd = karatsuba(b, d);
        let ad_plus_bc = karatsuba(a+b, c+d) - ac - bd;

        let result = ac * 10**(2*nby2) + ad_plus_bc * 10**nby2 + bd;
        return result;

    }
} 
console.log(karatsuba(1234, 5678 ));