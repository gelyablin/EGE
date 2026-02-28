print('x y z w F')
for x in [1,0]:
    for y in [1,0]:
        for z in [1,0]:
            for w in [1,0]:
                if ((x == y) <= ((not z) or w)) == (not ((w <= x) or (y <= z))):
                    print(x, y, z, w, 1)







answer = 'wzyx'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 2, answer, 'e0abee87e4ba1de22c6b8cf076c5016b'))