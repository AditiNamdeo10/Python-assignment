val = 0xCAFE

test = bin(val & 0xF).count('1') >= 3
print("At least three LSBs on:", test)

rev = ((val & 0xFF) << 8) | ((val >> 8) & 0xFF)
print("Reversed byte order = 0x%X" % rev)

rot = ((val << 4) | (val >> 12)) & 0xFFFF
print("After 4-bit rotation = 0x%X" % rot)