from gen import big_int_to_array

e = 65537
# n = 218037176684383184653287605151347250011
# d = 165737797440925234728498761829584192825
n = 16864325190094293761
d = 869759359060353473

encrypted = pow(17104, e, n)
decrypted = pow(6129553454723941295, d, n)

signed = pow(9502, d, n)
designed = pow(signed, e, n)

print(f"encrypted: {encrypted}")
print(f"decrypted: {decrypted}")

print(f"signed: {signed}")
print(f"designed: {designed}")
print(f"signed as array: {big_int_to_array(signed)}")

print(f"e: {big_int_to_array(e)}")
print(f"n: {big_int_to_array(n)}")
print(f"d: {big_int_to_array(d)}")