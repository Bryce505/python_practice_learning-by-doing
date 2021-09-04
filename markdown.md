# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题

文本
------
### 普通文本
这是一段普通的文本
### 单行文本
  hello大家好，我是bryce
### 文本块
#### 语法1
  欢迎到访  
  很高兴  
  见到您 
#### 语法2
```
欢迎到访    
很高兴  
见到您  
```

### 文字高亮
```
`linux` `网络编程` `socket` `epoll`
```
`linux` `网络编程` `socket` `epoll`

### 换行
直接回车不能换行，   
可以再上一行文本后面补加`两个空格`   
这样下一行的文本就可以换行了 
### 斜体、粗体、删除线
|语法|效果|
|---|---|
|`*斜体1*`|*斜体1*|
|`_斜体_`|_斜体2_|
|`**粗体**`|**粗体**|
|`__粗体__`|__粗体__|
|`这是一个~~删除线~~`|~~删除线~~|
|`***斜粗体***`|***写粗体***|

图片
-------
基本格式：
```
![alt](URL title)
```
-alt 表示图片显示失败时的替代文本  
-title表示鼠标悬停在图片时的显示文本（注意这里要加引号）  
URL即图片的url地址，如果引用本地仓库中的图片，直接适用**相对路径**就可以了，如果引用其它仓库中的图片要注意格式，即：`仓库地址/raw/分支名/图片路径`，如：  
```
https://github.com/guodongxiaren/ImageCache/raw/master/logo/foryou.gif
```
|#|语法|效果|
|---|---|---|
|1 |`![baidu](http://www.baidu.com/img/bdlogo.gif '百度logo')` |![baidu](http://www.baidu.com/img/bdlogo.gif "百度logo")|


![baidu](http://www.baidu.com/img/bdlogo.gif "百度logo")

链接
----
### 链接外部URL
|#|语法|效果|
|1|`[我的博客](http://blog.csdn.net/guodongxiaren "悬停显示")`|[我的微博](https://mubu.com/app/edit/home/11na7ejULr4 "我的幕布")|
