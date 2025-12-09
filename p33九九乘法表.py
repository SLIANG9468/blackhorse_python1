'''
https://www.bilibili.com/video/BV1sHU9BmEne?spm_id_from=333.788.videopod.episodes&vd_source=f91c72f5e6c586dc724d0e8738d874e8&p=33

1 * 1 = 1
1 * 2 = 2   2 * 2 = 4
1 * 3 = 3   2 * 3 = 6
...
1 * 9 = 9   2 * 9 = 18  3 * 9 = 27  4 * 9 = 36 ... 9 * 9 = 81 
'''

for row in range(1, 10):
    for col in range( 1, row + 1 ):
        print(f"{col} * {row} = {col * row}", end="\t" )
    print()
