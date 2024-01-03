# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# import domain

class ActionplayRPS(Action):

    def name(self) -> Text:
        return "action_play_rps"

    def computer_choice(self):
        generatednum = random.randint(1,3)
        if generatednum == 1:
            computer_choice = "rock"
        elif generatednum ==2:
            computer_choice = "paper"
        elif generatednum == 3:
            computer_choice = "scissors"

        return computer_choice
    
    # def run(self, dispatcher: CollectingDispatcher,
    #         tracker = Tracker,
    #         domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    

        # play rock paper scissors
        user_choice = tracker.get_slot("choice")
        dispatcher.utter_message(text=f"You chose {user_choice}")
        comp_choice = self.computer_choice()
        dispatcher.utter_message(text=f"The computer chose {comp_choice}")


        if user_choice == "rock" and comp_choice == "scissors":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "rock" and comp_choice == "paper":
            dispatcher.utter_message(text="The computer won this round.")
        elif user_choice == "paper" and comp_choice == "rock":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "paper" and comp_choice == "scissors":
            dispatcher.utter_message(text="The computer won this round.")
        elif user_choice == "scissors" and comp_choice == "paper":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "scissors" and comp_choice == "rock":
            dispatcher.utter_message(text="The computer won this round.")
        else:
            dispatcher.utter_message(text="It was a tie!")
 
        return []















