# # redis_sentinel_helper.py 连接redis 哨兵模式的工具类
# import asyncio
# import json
# import logging
# import os
# import redis
# from redis.sentinel import Sentinel

# logger = logging.getLogger(__name__)


# class redisSentinelHelper():
#     def __init__(self,endpoint_config):
#         self.url = endpoint_config['host']
#         self.port1 = endpoint_config['port1']
#         self.port2 = endpoint_config['port2']
#         self.port3 = endpoint_config['port3']
#         self.sentinel_list = []
#         self.sentinel_list.append((self.url, self.port1))
#         self.sentinel_list.append((self.url, self.port2))
#         self.sentinel_list.append((self.url, self.port3))


#         self.password= endpoint_config['password']
#         self.socket_timeout= endpoint_config['socket_timeout']
#         self.db= endpoint_config['db']
#         self.service_name= endpoint_config['master']
#         try:
#             self.sentinel = Sentinel(self.sentinel_list, socket_timeout=self.socket_timeout, sentinel_kwargs={'password':self.password})
        
#             self.master = self.sentinel.master_for(
#             service_name=self.service_name,
#             socket_timeout=self.socket_timeout,
#             password=self.password,
#             db=self.db)
#         except redis.ConnectError as err:
#             logger.debug(str(err))

#     def get_master_redis(self):
#         return self.sentinel.discover_master(self.service_name)
    
#     def get_slave_redis(self):
#         return self.sentinel.discover_slaves(self.service_name)
    
#     def setex_key(self, key, value, ex):
#         if self.master:
#             return self.master.setex(key, ex, value)
#         else:
#             return None
#     def set_key(self, key, value):
#         if self.master:
#             return self.master.set(key, value)
#         else:
#             return None
    
#     def get_key(self, key):
#         if self.master:
#             return self.master.get(key)
#         else:
#             return None
#     def delete_key(self, key):
#         if self.master:
#             return self.master.delete(key)
#         else:
#             return None
