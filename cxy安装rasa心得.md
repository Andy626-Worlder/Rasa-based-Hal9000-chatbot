![image-20220916153919376](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916153919376.png)

大家主要看看官方的视频，配合着我的各种报错来看，效果极佳。

[Installing Rasa Open Source 1.x & 2.x: Windows 10 (64 bit) - YouTube](https://www.youtube.com/watch?v=4ewIABo0OkU&list=PL75e0qA87dlEWUA5ToqLLR026wIkk2evk&index=1)



# Set up Conda



![image-20220916160131833](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916160131833.png)

## 进入 conda promot

[(21条消息) Anaconda Prompt 下切换路径问题_WeiXy+的博客-CSDN博客](https://blog.csdn.net/weixin_44054487/article/details/94173705#:~:text=Anaconda Prompt ： 默认 路径 ：默认 路径 是你的用户名,只能在根目录 下 进行 切换 盘符。 在用户名 路径下 ，输入cd..)

![image-20220916160849985](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916160849985.png)

**注意！！！**

在这一步，一定要记得，把python版本换成python 3.7： 具体怎么做请看目录：“退回python3.7”！！

![image-20220916180407888](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916180407888.png)

然后降级python成功后，把下图的 python==3.10.4 变成 3.7.

其余操作一样。

![image-20220916161156541](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916161156541.png)

tmd 打错了。。



# **这张图非常重要！！！！**

![image-20220916161533149](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916161533149.png)



## 激活conda下的installingrasa

![image-20220916161639039](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916161639039.png)



## 下载ujson （ultra json）

![image-20220916161846782](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916161846782.png)

![image-20220916161854971](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916161854971.png)



## 下载tensorflow

### 出现问题 python不对？

![image-20220916162507119](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916162507119.png)

[anaconda - conda: ResolvePackageNotFound python=3.1 - Stack Overflow](https://stackoverflow.com/questions/71215294/conda-resolvepackagenotfound-python-3-1)

#### 用它的方法试一试 

conda create --n installingrasa2 python==3.10.4

![image-20220916162850241](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916162850241.png)

![image-20220916163001148](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916163001148.png)

![image-20220916170632825](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916170632825.png)

![image-20220916170645793](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916170645793.png)

conda install tensorflow： 成功！！！！！！

![image-20220916170835383](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916170835383.png)



## 下载rasa

![image-20220916171050094](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916171050094.png)

出错？

![image-20220916171101776](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916171101776.png)



[(21条消息) pip下载包时出现不适配导致无法下载安装包:error: subprocess-exited-with-error；error: metadata-generation-failed；_被rua弄的小狸花的博客-CSDN博客](https://blog.csdn.net/weixin_42455006/article/details/125793559)

可能是pip install 的事？ 说是用下conda install

事实证明。应该不是。



这个靠谱点，https://forum.rasa.com/t/unable-to-install-rasa-due-to-error/51898

![image-20220916173141769](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916173141769.png)

最终都是python 3.10.4 的错！！！！

### 退回python 3.7

[(21条消息) anaconda python 3.8降级_西瓜6的博客-CSDN博客_python3.8降级3.7](https://blog.csdn.net/qq_37924224/article/details/117712061)

![image-20220916173922264](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916173922264.png)

![image-20220916173942917](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916173942917.png)

![image-20220916174131404](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916174131404.png)



#### 继续下载rasa

不从头回去conda create name -- python==3.7.13 了

直接pip install rasa

![image-20220916174247725](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916174247725.png)

看起来不错，可以可以。

![image-20220916174329547](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916174329547.png)

这个tensorflow的包好大！

感觉盘要爆满了。。。

![image-20220916174828008](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916174828008.png)

安装了好久哇。。

应该是解决了。



C盘真的要爆炸了。。。

前后对比差不多2G

![image-20220916174901096](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916174901096.png)



### 需要 Visual C +++

但这个Visual Studio已经把C++ JAVA 各种都合并了。

所以可能没事（我是在Microsoft的商店里直接安装的，贼简单）



## 进入Rasa操作

### rasa init

![image-20220916175349098](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916175349098.png)

![image-20220916175409562](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916175409562.png)

成功建立。

### 训练model

![image-20220916175453245](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916175453245.png)

![image-20220916175513034](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916175513034.png)

![image-20220916175540244](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916175540244.png)

训练成功。

### 简单对话！

![image-20220916175616992](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916175616992.png)

![image-20220916175750625](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916175750625.png)

对话成功。

可以对自己的项目进行修改训练了。

![image-20220916175958236](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916175958236.png)













