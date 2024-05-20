import logging
from openai import OpenAI

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted


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


class ActionGenerateResponse(Action):

    def name(self) -> str:
        return "generate_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        user_text = tracker.latest_message.get('text')
        logger.info(f"USER_TEXT: {user_text}")
        answer = self.get_answer(user_text)
        if answer:
            dispatcher.utter_message(text=answer)
        else:
            dispatcher.utter_message(response="utter_fallback")
        return []

    def get_answer(self, user_text):
        with open("/app/actions/prompt.txt", "r") as file:
          prompt = file.read()
        try:
            client = OpenAI(base_url="http://host.docker.internal:1234/v1", api_key="lm-studio")

            completion = client.chat.completions.create(
            model="IlyaGusev/saiga_llama3_8b_gguf",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_text}
            ],
            temperature=0.4,
            )
            return(completion.choices[0].message.content)
        except Exception as e:
            logger.error(f"Error in respone generation: {e}")
            return
        