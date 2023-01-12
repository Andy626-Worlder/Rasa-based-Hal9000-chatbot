# # sentinel_lock_store.py 对应sentinel_lock_store.RedisSentinelLockStore
# import asyncio
# import json
# import logging
# import os

# from async_generator import asynccontextmanager
# from typing import Text, Union, Optional, AsyncGenerator

# from rasa.shared.exceptions import RasaException, ConnectionException
# import rasa.shared.utils.common
# from rasa.core.constants import DEFAULT_LOCK_LIFETIME
# from rasa.core.lock import TicketLock
# from rasa.utils.endpoints import EndpointConfig

# logger = logging.getLogger(__name__)

# from redis.sentinel import Sentinel

# def _get_lock_lifetime() -> int:
#     return int(os.environ.get("TICKET_LOCK_LIFETIME", 0)) or DEFAULT_LOCK_LIFETIME


# LOCK_LIFETIME = _get_lock_lifetime()
# DEFAULT_SOCKET_TIMEOUT_IN_SECONDS = 10

# DEFAULT_REDIS_LOCK_STORE_KEY_PREFIX = "lock:"
# import redis
# from redis.sentinel import Sentinel
# from rasa.core.lock_store import LockStore
# from redis_sentinel_helper import redisSentinelHelper


# class RedisSentinelLockStore(LockStore):
#     """Redis store for ticket locks."""
#     def __init__(
#         self,
#         endpoint_config: EndpointConfig
#     ) -> None:
        
#         self.red = redisSentinelHelper(endpoint_config.kwargs)
#         key_prefix=endpoint_config.kwargs['key_prefix']
#         self.key_prefix = DEFAULT_REDIS_LOCK_STORE_KEY_PREFIX
#         if key_prefix:
#             logger.debug(f"Setting non-default redis key prefix: '{key_prefix}'.")
#             self._set_key_prefix(key_prefix)
#         super().__init__()

#     def _set_key_prefix(self, key_prefix: Text) -> None:
#         if isinstance(key_prefix, str) and key_prefix.isalnum():
#             self.key_prefix = key_prefix + ":" + DEFAULT_REDIS_LOCK_STORE_KEY_PREFIX
#         else:
#             logger.warning(
#                 f"Omitting provided non-alphanumeric redis key prefix: '{key_prefix}'. "
#                 f"Using default '{self.key_prefix}' instead."
#             )

#     def get_lock(self, conversation_id: Text) -> Optional[TicketLock]:
#         """Retrieves lock (see parent docstring for more information)."""
#         serialised_lock = self.red.get_key(self.key_prefix + conversation_id)
#         if serialised_lock:
#             return TicketLock.from_dict(json.loads(serialised_lock))
#         return None

#     def delete_lock(self, conversation_id: Text) -> None:
#         """Deletes lock for conversation ID."""
#         deletion_successful = self.red.delete_key(self.key_prefix + conversation_id)
#         self._log_deletion(conversation_id, deletion_successful)

#     def save_lock(self, lock: TicketLock) -> None:
#         self.red.set_key(self.key_prefix + lock.conversation_id, lock.dumps())
