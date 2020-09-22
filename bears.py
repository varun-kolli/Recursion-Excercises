# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):
    if n < 42:
        return False
    if n == 42:
        return True

    is_even = n % 2 == 0
    is_div_3 = n % 3 == 0
    is_div_4 = n % 4 == 0
    is_div_5 = n % 5 == 0

    if is_even:
        ret = bears(int(n / 2))
        if ret:
            return ret

    if is_div_3 or is_div_4:
        ret = bears(n - (n // 10) % 10 * (n % 10))
        if ret:
            return ret

    if is_div_5:
        ret = bears(n - 42)
        if ret:
            return ret
