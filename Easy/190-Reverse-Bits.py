# Example 1:
# Input:  00000010100101000001111010011100
# Output: 00111001011110000010100101000000
# Explanation: The input binary string 00000010100101000001111010011100 
# represents the unsigned integer 43261596, so return 964176192 
# which its binary representation is 00111001011110000010100101000000.

# Example 2:
# Input:  11111111111111111111111111111101
# Output: 10111111111111111111111111111111
# Explanation: The input binary string 11111111111111111111111111111101 
# represents the unsigned integer 4294967293, so return 3221225471 which its 
# binary representation is 10111111111111111111111111111111.

# Runtime: 32 ms, faster than 47.83% of Python3 online submissions for Reverse Bits.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Reverse Bits.

class Solution:
    def reverseBits(self, n: int) -> int:
        rev_bits = 0
        for i in range( 32 ):
            
            rev_bits = rev_bits << 1
            
            # rev_bits get binary bit from LSB to MSB of n
            rev_bits = rev_bits | ( n & 1 )
            
            n = n >> 1
            
        
        return rev_bits

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line)
            
            ret = Solution().reverseBits(n)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

# https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-19.php

# n = "43261596" # 964176192
# n = "4294967293" # 3221225471
# ret = Solution().reverseBits(int(n))
# print(ret)
