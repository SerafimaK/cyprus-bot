import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction, SlotSet, SessionStarted, ActionExecuted
import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class ActionSessionStart(Action):

    def name(self) -> str:
        return "action_session_start"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        events = [SessionStarted(),]
        metadata = tracker.get_slot("session_started_metadata")
        language = metadata.get("language")
        logger.info(f"Chosen language: {language}")
        # Set the language slot
        events.append(SlotSet("language", language))
        dispatcher.utter_message(response="utter_start")
        events.append(FollowupAction("action_main"))
        return events
