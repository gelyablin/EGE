print('x y w z F')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0,2):
                if ((x or (not y)) <= (w == z)) == ((x or (not y)) == (w <= z)) == 0:
                    print(x, y, w, z, 0)






answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 11, answer, '7379de4777f5748aa568b8d0bf8c3795'))