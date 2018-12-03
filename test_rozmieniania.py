
from rozmienianie import rozmien


for i in range(10):
    wynik, suma = rozmien([0, 2, 0, 0, 2, 2], i)
    print(i, wynik, suma)

