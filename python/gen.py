import random
from math import gcd

def miller_rabin(n, k=40):
    """Miller-Rabin 质数检测"""
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    # 将 n-1 写成 d * 2^r
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    """生成指定位数的大质数"""
    while True:
        n = random.getrandbits(bits)
        n |= (1 << bits - 1) | 1  # 设置最高位和最低位为1，确保位数和奇数
        if miller_rabin(n):
            return n

def mod_inverse(e, phi):
    """扩展欧几里得算法求模逆: d ≡ e⁻¹ mod φ(n)"""
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi

def generate_rsa_keys(bits=1024):
    """生成 RSA 密钥对 (n, e, d)"""
    # 生成两个大质数 p 和 q
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)

    # 确保 p != q
    while p == q:
        q = generate_prime(bits // 2)

    n = p * q
    phi = (p - 1) * (q - 1)

    # 常用公钥指数
    e = 65537
    if gcd(e, phi) != 1:
        # 极小概率发生，重新生成
        return generate_rsa_keys(bits)

    d = mod_inverse(e, phi)

    return {
        'p': p,
        'q': q,
        'n': n,
        'e': e,
        'd': d
    }

def big_int_to_array(x):
    """
    将大整数 x 转换为 base=10000 的数组，低位在前
    例如: 100050006 -> [6, 5, 1]
    """
    if x == 0:
        return [0]
    
    digits = []
    base = 10000
    while x > 0:
        digits.append(x % base)
        x //= base
    return digits  # 低位在前，符合 Minecraft 系统要求

def main():
    keys = generate_rsa_keys(64)

    n = keys['n']
    e = keys['e']  # 65537
    d = keys['d']

    print(f"p = {keys['p']}")
    print(f"q = {keys['q']}")
    print(f"n = {n}")
    print(f"e = {e}")
    print(f"d = {d}")
    print("\n" + "="*50)
    print("For Minecraft system (base 10000, little-endian):")
    print("="*50)

    e_array = big_int_to_array(e)
    n_array = big_int_to_array(n)
    d_array = big_int_to_array(d)

    print(f"e_digits: {e_array}  # {e}")
    print(f"n_digits: {n_array}  # {n}")
    print(f"d_digits: {d_array}  # {d}")

    print("\nUsage in Minecraft:")
    print("data modify storage bigint:tmp a_digits set value " + str(e_array))
    print("data modify storage bigint:tmp b_digits set value " + str(d_array))
    print("data modify storage bigint:tmp m_digits set value " + str(n_array))
    print("function abs_mod_pow  # computes a^b mod m")

if __name__ == "__main__":
    main()