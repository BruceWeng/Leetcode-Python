"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
"""
Example:
n1 = 123
n2 = 456

        123
    *   456
------------
        738
       615
      492
------------
      56088
"""
"""
Solution1:
"""
def multiply(num1, num2):
    product = [0] * (len(num1) + len(num2))
    pos = len(product) - 1
    for n2 in range(len(num2) - 1, -1, -1):
        multiplyPos = pos
        for n1 in range(len(num1) - 1, -1, -1):
            current = int(num1[n1]) * int(num2[n2])
            product[multiplyPos] += current
            product[multiplyPos - 1] += product[multiplyPos] // 10
            product[multiplyPos] %= 10
            multiplyPos -= 1
        print(product)
        pos -= 1

    start = 0
    while start < len(product) - 1 and product[start] == 0:
        start += 1

    strList = map(str, product[start:]) # [1, 2, 3] -> ["1", "2", "3"]
    return "".join(strList) # "123"

"""
Solution2:
"""
def multiply(num1, num2):
    return str(int(num1) * int(num2))
    
if __name__=="__main__":
    print(multiply("123", "456"))
    print(multiply("9", "9"))
