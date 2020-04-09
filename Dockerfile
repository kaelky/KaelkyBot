FROM python:3.8.2

RUN pip3 install python-telegram-bot

RUN mkdir /KaelkyBot
ADD . /KaelkyBot
WORKDIR /KaelkyBot

CMD python3 /KaelkyBot/bot.py