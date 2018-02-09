class Solution(object):

    def four_digit(self):
        for num in range(1000, 9999):
            digits = []
            temp = num
            if num % 1111 == 0:
                continue
            else:
                while num != 0:
                    tail = num % 10
                    num = num // 10
                    digits.append(tail)
                digits.sort()
                small = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]
                large = digits[0] + digits[1] * 10 + digits[2] * 100 + digits[3] * 1000
                if temp == abs(large - small):
                    return temp
                else:
                    continue

obj = Solution()
print(obj.four_digit())



