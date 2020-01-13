class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        
        a_real = int(a[:a.index("+")])
        a_complex = int(a[a.index("+")+1:-1])
        
        b_real = int(b[:b.index("+")])
        b_complex = int(b[b.index("+")+1:-1])
        
        real_res = a_real * b_real
        
        complex_const = a_real*b_complex + b_real*a_complex
        
        complex_mul = -(a_complex*b_complex)
        
        real_res += complex_mul
        
        return str(real_res) + "+" + str(complex_const) + "i"
        
