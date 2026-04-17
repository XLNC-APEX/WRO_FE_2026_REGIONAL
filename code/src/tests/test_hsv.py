from utils import ColorHSV

print(ColorHSV.from_rgb((0, 112, 192)))
print("expected:\n",ColorHSV(205, 100, 75.3))

print(ColorHSV.from_rgb((237, 125, 49)))
print("expected:\n",ColorHSV(24, 79.3, 92.9))

print(ColorHSV.from_rgb((0, 125, 49)))
print("expected:\n",ColorHSV(144, 100, 49))
# print(ColorHSV(2, 2, 2))

