import random
from typing import List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction, SlotSet, SessionStarted, ActionExecuted, Restarted
import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class ActionSessionStart(Action):

    def name(self) -> str:
        return "start_message"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        dispatcher.utter_message(response="utter_start")
        dispatcher.utter_message(response="utter_main")
        return [Restarted()]


class ActionFallbackHandler(Action):

    def name(self) -> str:
        return "fallback_handler"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        dispatcher.utter_message(response="utter_fallback")
        return []
