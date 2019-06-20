class Solution:
    def countPrimes(self, n: int) -> int:
    """
    refer https://leetcode.com/problems/count-primes/discuss/153528/Python3-99-112-ms-Explained%3A-The-Sieve-of-Eratosthenes-with-optimizations
    and LeetCode's solution
    """
    
    
        if n < 2:
            return 0
        
        is_prime = [1] * n
        is_prime[0] = 0
        is_prime[1] = 0
        
        for i in range(2, int(n**0.5)+1):
            if not is_prime[i]:
                continue
            for j in range(i*i, n, i):
                is_prime[j] = 0
            
        return sum(is_prime)
