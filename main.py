from config import *
from etc import *

from sys import argv
from time import sleep

from origamibot import OrigamiBot as Bot
from origamibot.listener import Listener


class BotsCommands:
    def __init__(self, bot: Bot):  # Can initialize however you like
        self.bot = bot

    def start(self, message):   # /start command
        self.bot.send_message(
            message.chat.id,
            'Привет! Я проверяю слова и помогаю в изучении русского языка) Если не знаешь с чего введи команду: /help')

    def echo(self, message, value: str):  # /echo [value: str] command
        self.bot.send_message(
            message.chat.id,
            spell(value)
            )

    def help(self, message):  
            self.bot.send_message(
            message.chat.id,
            'Чтобы вывести список всех комманд используй: /commands. \n Для вывода правил используй: /rules. \n Чтобы проверить правильность слова используй команду: /check.')

    def commands(self, message):
            self.bot.send_message(
             message.chat.id,
             'Список всех команд: \n /start - приветственное сообщение \n /help - справка \n /echo - команда для любителей ложить чужих ботов) \n /rules - вывод списка правил \n /check - исправляет введенное слово \n Так же есть команды пасхалки, удачи их найти)))'   
            )
    
    def spell(self, message, value: str):
        if value == spell(value):
            out = 'Все правильно!'
        else:
            abc = spell(value)
            out = 'Правильный вариант слова - ' + abc
        self.bot.send_message(
            message.chat.id,
            out
        )

    def rules(self, message):
        self.bot.send_message(message.chat_id, 'Выбери одно правило из списка(нужно ввести цифру-номер правила): \n' + list_of_rules)
        while True:
            inp = int(input())
            if inp == '1':
                self.bot.send_message(
                message.chat_id,
                rule1)
            elif inp == '2':
                self.bot.send_message(
                message.chat_id,
                rule2)
            elif inp == '3':
                self.bot.send_message(
                message.chat_id,
                rule3)
            elif inp == '4':
                break
            



    def not_a_command(self):   # This method not considered a command
        print('I am not a command')


class MessageListener(Listener):  # Event listener must inherit Listener
    def __init__(self, bot):
        self.bot = bot
        self.m_count = 0

    def on_message(self, message):   # called on every message
        self.m_count += 1
        print(f'Total messages: {self.m_count}')

    def on_command_failure(self, message, err=None):  # When command fails
        if err is None:
            self.bot.send_message(message.chat.id,
                                  'Command failed to bind arguments!')
        else:
            self.bot.send_message(message.chat.id,
                                  'Error in command:\n{err}')


if __name__ == '__main__':
    token = (token1)
    bot = Bot(token)   # Create instance of OrigamiBot class

    # Add an event listener
    bot.add_listener(MessageListener(bot))

    # Add a command holder
    bot.add_commands(BotsCommands(bot))

    # We can add as many command holders
    # and event listeners as we like

    bot.start()   # start bot's threads
    while True:
        sleep(1)
        # Can also do some useful work i main thread
        # Like autoposting to channels for example