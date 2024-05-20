import random
from typing import Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted
import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


BUTTON_TYPE = "inline"
MAIN_BUTTONS = [
    {
        "english": "Documents",
        "russian": "Документы",
        "payload": "/documents",
    },
    {
        "english": "Set up your company",
        "russian": "Открыть свой бизнес",
        "payload": "/set_up_company",
    },
    {
        "english": "Taxation",
        "russian": "Налогообложение",
        "payload": "/taxation",
    },
]
END_SCRIPT_BUTTONS = [
    {
        "english": "Back",
        "russian": "Назад",
        "payload": "/back",
    },
    {
        "english": "Thanks",
        "russian": "Спасибо",
        "payload": "/thanks",
    },
]
DOCUMENTS_BUTTONS = [
    {
        "english": "Визы для въезда",
        "russian": "Visas for entry",
        "payload": "/entry_visas",
    },
    {
        "english": "Справка о несудимости",
        "russian": "Police clearance certificate",
        "payload": "/police_clearance",
    },
    {
        "english": "Перевод документов",
        "russian": "Translation of documents",
        "payload": "/translation",
    },
    {
        "english": "Другой вопрос",
        "russian": "Another question",
        "payload": "/another_question",
    },
]


class ActionMain(Action):

    TEXTS_EN = [
        "Write your question or choose one of the sections.",
        "Click on the appropriate section or write a question.",
        "Choose one of the buttons or ask your question.",
    ]
    TEXTS_RU = [
        "Напиши свой вопрос или выбери один из разделов.",
        "Кликни на нужный раздел или напиши вопрос.",
        "Выбери одну из кнопок или задай свой вопрос.",
    ]

    def name(self) -> Text:
        return "action_main"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("language") == "english":
            answer = random.choice(self.TEXTS_EN)
            buttons = [{"payload": button.get("payload"), "title": button.get("english")} for button in MAIN_BUTTONS]
        else:
            answer = random.choice(self.TEXTS_RU)
            buttons = [{"payload": button.get("payload"), "title": button.get("russian")} for button in MAIN_BUTTONS]
        dispatcher.utter_message(text=answer, buttons=buttons, button_type=BUTTON_TYPE)
        return []


class ActionAnyQuestions(Action):

    TEXTS_EN = [
        "Do you want to know something else?",
        "Curious to know anything else?",
        "Do you have more questions?",
    ]
    TEXTS_RU = [
        "Хочешь узнать что-нибудь еще?",
        "Интересно узнать что-нибудь еще?",
        "Остались еще вопросы?",
    ]

    def name(self) -> Text:
        return "action_any_questions"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("language") == "english":
            answer = random.choice(self.TEXTS_EN)
            buttons = [{"payload": button.get("payload"), "title": button.get("english")} for button in MAIN_BUTTONS]
        else:
            answer = random.choice(self.TEXTS_RU)
            buttons = [{"payload": button.get("payload"), "title": button.get("russian")} for button in MAIN_BUTTONS]
        dispatcher.utter_message(text=answer, buttons=buttons, button_type=BUTTON_TYPE)
        return [SlotSet("main_state", True)]


class ActionHelp(Action):
    
    TEXT_EN = (
        "I can provide you with useful information for life in Cyprus! ☀️\n"
        "Choose one of the sections to get started or write your own question:"
    )
    TEXT_RU = (
        "Я могу предоставить тебе полезную информацию для жизни на Кипре! ☀️\n"
        "Выбери один из разделов, чтобы начать или напиши свой вопрос:"
    )

    def name(self) -> Text:
        return "action_help"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("language") == "english":
            answer = self.TEXT_EN
            buttons = [{"payload": button.get("payload"), "title": button.get("english")} for button in MAIN_BUTTONS]
        else:
            answer = self.TEXT_RU
            buttons = [{"payload": button.get("payload"), "title": button.get("russian")} for button in MAIN_BUTTONS]
        dispatcher.utter_message(text=answer, buttons=buttons, button_type=BUTTON_TYPE)
        return []


class ActionAnotherQuestion(Action):

    TEXT_EN = (
        "What do you want to know?What do you want to know?"
    )
    TEXT_RU = (
        "Что вы хотите узнать?"
    )

    def name(self) -> Text:
        return "action_another_question"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("language") == "english":
            answer = self.TEXT_EN
            buttons = [{"payload": button.get("payload"), "title": button.get("english")} for button in MAIN_BUTTONS]
        else:
            answer = self.TEXT_RU
            buttons = [{"payload": button.get("payload"), "title": button.get("russian")} for button in MAIN_BUTTONS]
        dispatcher.utter_message(text=answer, buttons=buttons, button_type=BUTTON_TYPE)
        return []


class ActionDocuments(Action):

    TEXTS_EN = [
        "Click the button and find out more:",
        "To read the information, click on one of the buttons:",
        "Select the button and find out the details:",
    ]
    TEXTS_RU = [
        "Нажми на кнопку и узнай подробнее:",
        "Чтобы прочитать информацию, нажми на одну из кнопок:",
        "Выбери кнопку и узнай подробности:",
    ]

    def name(self) -> Text:
        return "action_documents"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("language") == "english":
            answer = random.choice(self.TEXTS_EN)
            buttons = [{"payload": button.get("payload"), "title": button.get("english")} for button in DOCUMENTS_BUTTONS]
        else:
            answer = random.choice(self.TEXTS_RU)
            buttons = [{"payload": button.get("payload"), "title": button.get("russian")} for button in DOCUMENTS_BUTTONS]
        dispatcher.utter_message(text=answer, buttons=buttons, button_type=BUTTON_TYPE)
        return []


class ActionVisas(Action):
    
    TEXT_EN = (
        "Citizens of EU countries and holders of residence permits of these countries don't need a visa to enter Cyprus.\n"
        "Third-country nationals can enter Cyprus with a Schengen visa or with a Cypriot national visa.\n"
        "To find complete information about visas and rules for staying in Cyprus, you can check the website of the Migration Department:\n"
        "http://www.moi.gov.cy/moi/crmd/crmd.nsf/home_en/home_en?openform#"
    )
    TEXT_RU = (
        "Для граждан стран Евросоюза и владельцев ВНЖ этих стран не нужна виза для въезда на Кипр.\n"
        "Граждане третьих стран могут въехать на Кипр по Шенгенской визе или оформив национальную визу Кипра.\n"
        "Чтобы найти полную информацию по визам и правилам пребывания на Кипре, вы можете перейти на сайт Миграционного департамента: http://www.moi.gov.cy/moi/crmd/crmd.nsf/home_en/home_en?openform#"
   )

    def name(self) -> Text:
        return "action_visas"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("language") == "english":
            answer = self.TEXT_EN
            buttons = [{"payload": button.get("payload"), "title": button.get("english")} for button in END_SCRIPT_BUTTONS]
        else:
            answer = self.TEXT_RU
            buttons = [{"payload": button.get("payload"), "title": button.get("russian")} for button in END_SCRIPT_BUTTONS]
        dispatcher.utter_message(text=answer, buttons=buttons, button_type=BUTTON_TYPE)
        return []


class ActionPoliceClearance(Action):
    
    TEXT_EN = (
        "⚖️ Справка о несудимости на Кипре\n"
        "Прожив на Кипре полгода и более, можно получить кипрскую справку о несудимости.\n"
        "Справка выдаётся в главном отделении полиции в Никосии по будням до 15:00. Для получения справки, необходимо заполнить и подписать заявление.\n"
        "Скачать форму\n"
        "📍 Адрес: Cyprus Police Headquarters Nicosia 1478, Cyprus\n"
        "Телефон: +357 (22) 808944\n\n"
        "http://www.police.gov.cy\n"
        "❗При себе нужно иметь копии и оригиналы загранпаспорта и PinkSlip."
    )
    TEXT_RU = (
        "⚖️ Police clearance certificate in Cyprus\n"
        "Having lived in Cyprus for six months or more, you can get a Cypriot certificate of good conduct.\n"
        "The certificate is issued at the main police station in Nicosia on weekdays until 15:00. To receive a certificate, you must fill out and sign an application.\n"
        "Download form\n"
        "📍 Address: Cyprus Police Headquarters Nicosia 1478, Cyprus\n"
        "Phone: +357 (22) 808944\n\n"
        "http://www.police.gov.cy\n"
        "❗You need to have copies and originals of your passport and PinkSlip with you."
   )

    def name(self) -> Text:
        return "action_police_clearance"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("language") == "english":
            answer = self.TEXT_EN
            buttons = [{"payload": button.get("payload"), "title": button.get("english")} for button in END_SCRIPT_BUTTONS]
        else:
            answer = self.TEXT_RU
            buttons = [{"payload": button.get("payload"), "title": button.get("russian")} for button in END_SCRIPT_BUTTONS]
        dispatcher.utter_message(text=answer, buttons=buttons, button_type=BUTTON_TYPE)
        return []


class ActionTranslation(Action):
    
    TEXT_EN = (
        "💬 If you need to translate documents, you can find a certified translator in the registry: https://www.pio.gov.cy/en/register-of-sworn-translators.html"
    )
    TEXT_RU = (
        "💬 Если вам нужно сделать перевод документов, вы можете посмотреть реестр официальных переводчиков на Кипре: https://www.pio.gov.cy/en/register-of-sworn-translators.html"
   )

    def name(self) -> Text:
        return "action_translation"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("language") == "english":
            answer = self.TEXT_EN
            buttons = [{"payload": button.get("payload"), "title": button.get("english")} for button in END_SCRIPT_BUTTONS]
        else:
            answer = self.TEXT_RU
            buttons = [{"payload": button.get("payload"), "title": button.get("russian")} for button in END_SCRIPT_BUTTONS]
        dispatcher.utter_message(text=answer, buttons=buttons, button_type=BUTTON_TYPE)
        return []
