# Domain file



![image-20220915114842847](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220915114842847.png)

最主要的文件。以下是一些例子。

![image-20220915114914495](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220915114914495.png)



utterance 必须有，what should the chatbot should say. 填写在 actions里

![image-20220915115451180](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220915115451180.png)

**Can have multiple examples. More diverse and versatile, make it more like human**





# NLU file

储存信息，写出各种例句，让NLU学习， 来理解用户的intents。

只要是能想到的，就一定要往上写！！！！！

![image-20220916085537992](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916085537992.png)

5 - 10 , maybe not all ways.

 开始自己理解intents。

ex：

order number 也需要提供数据来训练。这样bot一看到就知道可能是订单号。





# stories file

![image-20220916085951845](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916085951845.png)

这里需要designer和developer合作。 （dialogue 应该在这里）

对于**所有的distinct需求**都需要建立对话逻辑。如果只有一个逻辑，会很僵硬。

理论上，**所有**对话都需要一个对应功能性需求的 **happy path ＋ 一个 sad path**。

## 实例

![](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916090431903.png)

happy path 可以随意起名， everything is provided

sad path就不一定了



这个是其中一个逻辑，最好有很多逻辑~~~

步骤： 

+ **检测到**意图：打招呼
+ 动作： 打招呼
+ 动作：做选择 （（在这个之前也可以直接加一个 intent: ask_ability  // 这就是另一个逻辑。其实不太推荐这样做，因为不想让用户有burden，并且限制用户的随机性）
+ **检测到**意图：查看我的订单
+ 动作：追查订单信息
+ **检测到**意图：查询订单详情
+ slot填充成功： 填充order-number（（这步是下一步成功的前提）
+ 动作：查询订单详情
+ 动作：询问还有什么需要我做的吗
+ **检测到**意图：否定
+ 动作：拜拜

整个过程非常顺滑！！！ 机器语言的魅力！！！！！！！！ 爱死了！！！





# Rules file

![image-20220916091720694](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916091720694.png)

MUST! ALWAYS! FOLLOW!

比如用户说再见，bot**必须**说再见

用户说你是谁，bot**必须**说我是你大爷（让然也可以请求用户做个问卷）

don't need to "think".



rules 应该很短。如果长的话，应该加进stories里。

 

 

# Actions file

![image-20220916093457168](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916093457168.png)

查询database--- bot demo

或者查询外部API



# Config - 1 - NLU Pipeline 

![image-20220916102123400](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916102123400.png)

![image-20220916094844528](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916094844528.png)



Natural Language Understanding  to help understand and process。 

make sense the natural language.

## Tokenizers

![image-20220916093632325](C:\Users\陈新元 Andy Chen\Desktop\image-20220916093632325.png)

**分解text 成 tokens。** 其中有简单根据空格分隔的whitespaceTokenizer。English 比较适合这个方法，中文就不适合。

**所有AI 理解语句的基础。**



## Featurizers

![image-20220916094012908](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916094012908.png)

聚合 tokens 成 features。也可以用ML Algorithm。

**理解 token的characteristics，进而判断用户的intent。**

Rasa 用的是 countVectorFeaturizers。 不需要理解原理，只要知道加黑的意义就行。



## Intent classifier

![image-20220916094412793](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916094412793.png)

虽然上面的featurizers 已经把intents 识别出来了，但这个intent应该进入到哪个categories里面去，需要这个。



## Entity extractors

![image-20220916094605125](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916094605125.png)



# Config - 2 - Dialogue Management Policies

![image-20220916102139762](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916102139762.png)

主要有以下三点（还有其他不重要的）

## RulePolicy

如果有 **rule file**，那么就需要 rulepolicy

![image-20220916095329063](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916095329063.png)

有rule就用



优先级是6，比如用户说一句话，经过NLU，判断有几个可能性**(probabilistically figures)**，优先级 1 2 5 6 ， 选6. 进入rulePolicy。 当然priority 可以被 altered。



## Memoization Policy

![image-20220916095554777](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916095554777.png)

依旧是 **probabilistically figures.**, 来决定做什么

不需要define不同的conversation，不需要写不同的user story， 只用走 story file中的happy path， sad path， alternative path......



## TEDClassifier

![image-20220916101819933](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220916101819933.png)

比较复杂，用了 transformer，主要处理 open domain的内容。

这节课只用到domain-specific 的知识，所以可以忽略（因为不是领域内的，因此优先级较低。

















