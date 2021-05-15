'''
斐波那契数列（Fibonacci sequence），通常也被称作黄金分割数列，是意大利数学家莱昂纳多·
斐波那契（Leonardoda Fibonacci）在《计算之书》中研究在理想假设条件下兔子成长率问题而引入的数列，因此这个数列也常被戏称为“兔子数列”。
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，按照这个规律，
斐波那契数列的前10个数是：1, 1, 2, 3, 5, 8, 13, 21, 34, 55。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用
'''
num=int(input('请输入范围： '))
#生成定长的list；也可以通过append添加 num_list.append()；否则报错
num_list=num*['']
a, b = 1, 1
for x in range(0,num):
    a,b=b,a+b
    #空数组不能直接指定位置
    num_list[x]=a
#list 知识点https://www.runoob.com/python3/python3-list.html
num_list.insert(0,1)
print(list(num_list))