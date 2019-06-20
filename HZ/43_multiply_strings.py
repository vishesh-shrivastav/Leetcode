class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # CANNOT convert the inputs to integer directly
        prod = [0] * (len(num1) + len(num2)) #placeholder for multiplication -> ndigit by mdigit results in n+m digits
        
        pos = len(prod)-1 #position within the placeholder
        
        for n1 in num1[::-1]:
            temp_pos = pos
            for n2 in num2[::-1]:
                prod[temp_pos] += int(n1) * int(n2) # add the results of single multiplication
                prod[temp_pos-1] += prod[temp_pos]//10 # bring out carry number to the left array
                prod[temp_pos] = prod[temp_pos]%10 # remove the carry out from the current array
                temp_pos -= 1 # first shifting the multplication to the end of the first integer
            pos -= 1 # then once first integer is exhausted shifting the second integer and starting
        
        # once the second integer is exhausted we want to make sure we are not zero padding
        ptr = 0
        
        while ptr < len(prod) - 1 and prod[ptr] == 0:# if we have zero before the numbers shift the pointer to the right
            ptr += 1
        
        return ''.join(str(x) for x in prod[ptr:]) # only report the digits to the right side of the pointer
