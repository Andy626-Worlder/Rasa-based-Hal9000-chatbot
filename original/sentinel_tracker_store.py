# # sentinel_tracker_store.py 对应type  'sentinel_tracker_store.RedisSentinelTrackerStore'
# import contextlib
# import itertools
# import json
# import logging
# import os

# from time import sleep
# from typing import (
#     Any,
#     Callable,
#     Dict,
#     Iterable,
#     Iterator,
#     List,
#     Optional,
#     Text,
#     Union,
#     TYPE_CHECKING,
#     Generator,
# )

# from boto3.dynamodb.conditions import Key
# from pymongo.collection import Collection

# import rasa.core.utils as core_utils
# import rasa.shared.utils.cli
# import rasa.shared.utils.common
# import rasa.shared.utils.io
# from rasa.shared.core.constants import ACTION_LISTEN_NAME
# from rasa.core.brokers.broker import EventBroker
# from rasa.core.constants import (
#     POSTGRESQL_SCHEMA,
#     POSTGRESQL_MAX_OVERFLOW,
#     POSTGRESQL_POOL_SIZE,
# )
# from rasa.shared.core.conversation import Dialogue
# from rasa.shared.core.domain import Domain
# from rasa.shared.core.events import SessionStarted
# from rasa.shared.core.trackers import (
#     ActionExecuted,
#     DialogueStateTracker,
#     EventVerbosity,
# )
# from rasa.shared.exceptions import ConnectionException, RasaException
# from rasa.shared.nlu.constants import INTENT_NAME_KEY
# from rasa.utils.endpoints import EndpointConfig
# import sqlalchemy as sa
# from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

# if TYPE_CHECKING:
#     import boto3.resources.factory.dynamodb.Table
#     from sqlalchemy.engine.url import URL
#     from sqlalchemy.engine.base import Engine
#     from sqlalchemy.orm import Session, Query
#     from sqlalchemy import Sequence

# logger = logging.getLogger(__name__)

# DEFAULT_REDIS_TRACKER_STORE_KEY_PREFIX = "tracker:"
# from rasa.core.tracker_store import TrackerStore
# from redis.sentinel import Sentinel
# from redis_sentinel_helper import redisSentinelHelper

# class RedisSentinelTrackerStore(TrackerStore):
#     """Stores conversation history in RedisSentinel"""
#     def __init__(
#         self,
#         domain: Domain,
#         host: Text = "localhost",
#         master: Text= "mymaster",
#         port1: int = 6379,
#         port2: int = 6380,
#         port3: int = 6381,
#         db: int = 0,
#         password: Optional[Text] = None,
#         key_prefix: Optional[Text] = None,
#         socket_timeout: Optional[float] = None,
#         record_exp: Optional[float] = None,
#         event_broker: Optional[EventBroker] = None,
#         **kwargs: Dict[Text, Any],
#         ):

#         config=dict()
#         config["host"]=host
#         config["master"]=master
#         config["port1"]=port1
#         config["port2"]=port2
#         config["port3"]=port3
#         config["db"]=db
#         config["password"]=password
#         config["socket_timeout"]=socket_timeout
#         self.red = redisSentinelHelper(config)

#         self.record_exp = record_exp
#         self.key_prefix = DEFAULT_REDIS_TRACKER_STORE_KEY_PREFIX
#         if key_prefix:
#             logger.debug(f"Setting non-default redis key prefix: '{key_prefix}'.")
#             self._set_key_prefix(key_prefix)
#         super().__init__(domain, event_broker, **kwargs)

#     def _set_key_prefix(self, key_prefix: Text) -> None:
#         if isinstance(key_prefix, str) and key_prefix.isalnum():
#             self.key_prefix = key_prefix + ":" + DEFAULT_REDIS_TRACKER_STORE_KEY_PREFIX
#         else:
#             logger.warning(
#                 f"Omitting provided non-alphanumeric redis key prefix: '{key_prefix}'. "
#                 f"Using default '{self.key_prefix}' instead.")

#     def _get_key_prefix(self) -> Text:
#         return self.key_prefix

#     def save(
#         self, tracker: DialogueStateTracker, timeout: Optional[float] = None
#     ) -> None:
#         """Saves the current conversation state."""
#         if self.event_broker:
#             self.stream_events(tracker)

#         if not timeout and self.record_exp:
#             timeout = self.record_exp
#         serialised_tracker = self.serialise_tracker(tracker)
#         self.red.setex_key(self.key_prefix + tracker.sender_id, serialised_tracker, ex=timeout)
#         #self.red.set_key(self.key_prefix + tracker.sender_id, serialised_tracker)

#     def retrieve(self, sender_id: Text) -> Optional[DialogueStateTracker]:
#         """Retrieves tracker for the latest conversation session.
#         The Redis key is formed by appending a prefix to sender_id.
#         Args:
#             sender_id: Conversation ID to fetch the tracker for.
#         Returns:
#             Tracker containing events from the latest conversation sessions.
#         """
#         stored = self.red.get_key(self.key_prefix + sender_id)
#         if stored is not None:
#             return self.deserialise_tracker(sender_id, stored)
#         else:
#             return None

#     def keys(self) -> Iterable[Text]:
#         """Returns keys of the Redis Tracker Store."""
#         return self.red.get_pattern(self.key_prefix + "*")
