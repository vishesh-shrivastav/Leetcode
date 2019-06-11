class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # CANNOT convert the inputs to integer directly
        prod = [0] * (len(num1) + len(num2))
        
        pos = len(prod)-1
        
        for n1 in num1[::-1]:
            temp_pos = pos
            for n2 in num2[::-1]:
                prod[temp_pos] += int(n1) * int(n2)
                prod[temp_pos-1] += prod[temp_pos]//10
                prod[temp_pos] = prod[temp_pos]%10
                temp_pos -= 1
            pos -= 1
        
        ptr = 0
        
        while ptr < len(prod) - 1 and prod[ptr] == 0:
            ptr += 1
        
        return ''.join(str(x) for x in prod[ptr:])
