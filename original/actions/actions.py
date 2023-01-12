# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

# # from typing import Any, Text, Dict, List
# #
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# #
# #
# # class ActionHelloWorld(Action):
# #
# #     def name(self) -> Text:
# #         return "action_hello_world"
# #
# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #
# #         dispatcher.utter_message(text="Hello World!")
# #
# #         return []


# from cgitb import text
# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionUserName(Action):

#     def name(self) -> Text:
#         return "action_greet_name"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         user_name = tracker.get_slot("Username")
#         dispatcher.utter_message(text=user_name)

#         return []


# # from typing import Any, Text, Dict, List

# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.events import UserUtteranceReverted
# # from rasa_sdk.executor import CollectingDispatcher

# # class ActionDefaultFallback(Action):
# #     """Executes the fallback action and goes back to the previous state
# #     of the dialogue"""

# #     def name(self) -> Text:
# #         return ACTION_DEFAULT_FALLBACK_NAME

# #     def ACTION_DEFAULT_FALLBACK_NAME():(
# #         print("Welcome rephrase again")
# #     )

# #     async def run(
# #         self,
# #         dispatcher: CollectingDispatcher,
# #         tracker: Tracker,
# #         domain: Dict[Text, Any],
# #     ) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(template="my_custom_fallback_template")

# #         # Revert user message which led to fallback.
# #         return [UserUtteranceReverted()]





# from typing import Any, Text, Dict, List

# from rasa_sdk import Tracker, FormValidationAction
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict

# import sqlite3


# class ValidateOrderNumberForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_order_number_form"

#     def validate_order_number(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
        
    
#         order = slot_value
#         print(f"Order number = {order} length = {len(order)}")
#         if len(order) == 0:
#             dispatcher.utter_message(text="Please don't fool me.")
#             return {"order_number": None}
#         # elif len(order) < 6:
#         #     dispatcher.utter_message(text="That order number is way too short. How about you provide me a 4-character order number?")
#         #     return {"order_number": None}
#         # elif len(order) > 6:
#         #     dispatcher.utter_message(text="That order number is way too long. How about you provide me a 4-character order number?")
#         #     return {"order_number": None}
#         elif len(order) != 6:
#             dispatcher.utter_message(text="It shouldn't be hard for you to provide me a 6 figure long number.")
#             return {"order_number": None}

#         return {"order_number": order}

# class QueryOrderDetails(Action):

#     def name(self) -> Text:
#         return "query_order_details"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
#         conn = DbQueryingMethods.create_connection(db_file="hal9000/Hal9000.db")

#         slot_value = tracker.get_slot("order_number")

#         get_query_results = DbQueryingMethods.select_by_slot(conn=conn,slot_value=slot_value)
        
#         dispatcher.utter_message(text=str(get_query_results))

#         return 


# class DbQueryingMethods:
#     def create_connection(db_file):
#         """ 
#         create a database connection to the SQLite database
#         specified by the db_file
#         :param db_file: database file
#         :return: Connection object or None
#         """
#         conn = None
#         try:
#             conn = sqlite3.connect(db_file)
#         except Error as e:
#             print(e)

#         return conn

#     def select_by_slot(conn, slot_value):
#         """
#         Query all rows in the Orders table
#         :param conn: the Connection object
#         :return:
#         """
#         cur = conn.cursor()
#         cur.execute(f'''SELECT EstimatedDeliveryDate from Orders
#                     WHERE OrderID="{slot_value}"''')

#         # return an array
#         deliveryDate = cur.fetchall()

#         if len(list(deliveryDate)) < 1:
#             return "There is no such order number."
#         else:
#             for row in deliveryDate:
#                 return f"Looks like your order will be delivered by {(row[0])}."


# class ValidateOrderNumber(Action):
#     def name(self) -> Text:
#         return "action_ValidateOrderNumber" 

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker, domain):
#         order_number = tracker.get_slot("order_number")
#         print(order_number)
#         connQ = sqlite3.connect('hal9001.db')
#         cursorQ = connQ.cursor()
#         tracker.get_slot("order_number")
#         row = cursorQ.execute("SELECT order_number from OrderNumber where order_number = " + order_number)
#         if len(list(row)) != 0:
#             print("order number exist")
#             dispatcher.utter_message(text="order number exist")
#         else:
#             print("order number not exist")
#             dispatcher.utter_message(text="order number not exist")
#         return [SlotSet('order_number', None)]