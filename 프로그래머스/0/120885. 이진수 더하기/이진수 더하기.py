
def solution(bin1, bin2):
    def binary_to_decimal(binary):
        decimal = 0
        power = len(binary) - 1
        for digit in binary:
            decimal += int(digit) * (2 ** power)
            power -= 1
        return decimal
    def decimal_to_binary_recursive(n):
        if n == 0:
            return ''
        else:
            return decimal_to_binary_recursive(n // 2) + str(n % 2)
    return '0' if len(decimal_to_binary_recursive(binary_to_decimal(bin1)+binary_to_decimal(bin2)))==0 else decimal_to_binary_recursive(binary_to_decimal(bin1)+binary_to_decimal(bin2))