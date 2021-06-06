def main():
    #input 字符串，如果跟数字相比，需要数据转换
    num = int(input('Number of rows: '))
    #列表嵌套[[]];[[]]*2 为[[],[]]；每一行数据集合在仪器就是一个list，如果输入9行，就有9个list
    yh = [[]] * num
    for row in range(len(yh)):
        #每一行有几个数据就有几个list
        # None,不是0 空字符串，它没有值，为空值；None数据类型为NoneType，None是其唯一值
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
'''
杨辉三角特点
1	
1	1	
1	2	1	
1	3	3	1	
1	4	6	4	1	
1	5	10	10	5	1	
1	6	15	20	15	6	1	

[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1]]
'''