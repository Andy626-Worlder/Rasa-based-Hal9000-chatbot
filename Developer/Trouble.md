https://blog.csdn.net/weixin_41021342/article/details/124128919

使用完这个方法后进行rasa shell 出现了这种情况：

![image-20220928091029295](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928091029295.png)

E:\Anaconda\Ana\envs\installingrasa2\lib\site-packages\rasa\core\tracker_store.py:168: FutureWarning: Tracker store implementation RedisSentinelTrackerStore is not asynchronous. Non-asynchronous tracker stores are currently deprecated and will be removed in 4.0. Please make the following methods async: ['_stream_new_events', 'create_tracker', 'exists', 'get_or_create_tracker', 'keys', 'number_of_existing_events', 'retrieve', 'retrieve_full_tracker', 'save', 'stream_events'] (will be removed in 4.0.0)



# 用到rasa shell之后，出现这个问题：

![image-20220928092749828](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928092749828.png)



## trying this method：

```py
pip install google-auth==1.10.1 prompt-toolkit==2.0.10 questionary==1.4.0 SQLAlchemy==1.3.12 urllib3==1.25.7
```

[python - I tried to run rasa shell i am getting ERROR asyncio Task exception was never retrieved future - Stack Overflow](https://stackoverflow.com/questions/58686979/i-tried-to-run-rasa-shell-i-am-getting-error-asyncio-task-exception-was-never-re)

![image-20220928094358441](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928094358441.png)



![image-20220928094750700](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928094750700.png)

出现啦很多问题



可能是因为安装的版本不太对。。。

![image-20220928094739050](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928094739050.png)

![image-20220928095338364](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928095338364.png)

根据他的型号一点点改就行。

最后版本：

```py
pip install google-auth==1.10.1 prompt-toolkit==3.0 questionary==1.5.1 SQLAlchemy==1.4.0 urllib3==1.26.5
```



rasa shell还是不行， 虽然解决了一些问题：

![image-20220928101137534](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928101137534.png)

 ERROR    asyncio  - Task exception was never retrieved
future: <Task finished coro=<SignalRouter._dispatch() done, defined at E:\Anaconda\Ana\envs\installingrasa2\lib\site-packages\sanic\signals.py:121> exception=ClientResponseError(RequestInfo(url=URL('http://localhost:5005/webhooks/rest/webhook?stream=true&token='), method='POST', headers=<CIMultiDictProxy('Host': 'localhost:5005', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'User-Agent': 'Python/3.7 aiohttp/3.7.4', 'Content-Length': '63', 'Content-Type': 'application/json')>, real_url=URL('http://localhost:5005/webhooks/rest/webhook?stream=true&token=')), (), status=503, message='Service Unavailable', headers=<CIMultiDictProxy('Content-Length': '79', 'Connection': 'close', 'Content-Type': 'application/json')>)>





## 方法二： 找到 console.py  更改

[ERROR asyncio - Task exception was never retrieve - Rasa Open Source - Rasa Community Forum](https://forum.rasa.com/t/error-asyncio-task-exception-was-never-retrieve/15511/16)

![image-20220928102213694](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928102213694.png)

![image-20220928102405433](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928102405433.png)

虽然找不到：

![image-20220928103341243](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928103341243.png)

但好似这个就是？？ 还是说不应该再 E盘的Anaconda 里找？？

![image-20220928103816919](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928103816919.png)

![image-20220928103904467](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928103904467.png)

![image-20220928103329462](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928103329462.png)



还原。并且注释掉原先的内容之后，（三个文件）

![image-20220928112235337](C:\Users\陈新元 Andy Chen\AppData\Roaming\Typora\typora-user-images\image-20220928112235337.png)

出现这个问题。（不知道有没有影响，但最好解决一下，是不是 pyche 里的那几个生成的文件的问题。





