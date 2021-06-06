from random import randrange, randint,sample
def display(balls):
    '''
    输出列表中的双色球球号码
    '''
    for index,ball in enumerate(balls):
        if index==len(balls)-1:
            print('|',end=' ')
        print('%02d'%ball,end=' ')
    print()

def random_select():
    '''
    随机选择一组号码
    :return:
    '''
    red_balls=[x for x in range(1,34)]
    selected_balls=[]
    selected_balls=sample(red_balls,6)
    selected_balls.sort()
    selected_balls.append (randint(1,16))
    return selected_balls
def main():
    n=int(input('机选几注：'))
    for _ in range(n):
        display(random_select())

if __name__=='__main__':
    main()

'''
知识点：
1）enumerate(sequence, [start=0])，其中sequence是一个可迭代序列，start是一个可选参数，表示序列下标的起始位置
    enumerate() 函数：用于将一个可迭代的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
    一般用在 for 循环当中
    1.enumerate()函数是Python中的内置函数，可以直接配合for循环使用
2）print()函数： print(*objet,sep=' ',end='\n',file=sys.stdout,flush=False)
    1.objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
    2.sep -- 用来间隔多个对象，默认值是一个空格。
    3.end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
    4.file -- 要写入的文件对象。
    5.flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新。
3） sort()与 sorted()
    对象上：sort是应用于list的方法；sorted可以用于所有可迭代对象进行排序操作；
    效果：list 的 sort 方法返回的是对已经存在的列表进行操作，会修改原始的list，如果不需要原始的list，list.sort()高效些
         而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作
4)random模块的sample函数 实现从列表中选择不重复的n个元素
    '''