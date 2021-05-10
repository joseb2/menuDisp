import logging
import os


from flask import Flask
from flask_ask import Ask, request, session, question, statement


app = Flask(_name_)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG) 



#"ask.launch" acts as decorator for defined "launched" function/returned variables
@ask.launch
def launched():
    speech_text = "Testing Raspberry Pi Automation"
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)


#ask.intent acts as decorator for command help intent
@ask.intent('Amazon.HelpIntent') 
def help(): 
    speech_text = 'Request for testcase' 
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text) 


@ask.session_ended
def session_ended(): 
    return "{}", 200 

