Title: Telegram logging handler for Python, Java, Bash
Date: 2018-01-01 10:20
Category: Programming

Did you ever have a piece of code that lasted hours? I did (and do). The problem is that I am usually obsessed with the question "did it finish??". So, I log into my server, and I check whether the code is running. This had to stop. For this reason, [Daniele](http://disi.unitn.it/~foroni/) and myself developed a first, naive version of a Telegram logging system that alerts you whenever something happens. These are the use cases:

* Critical software: send me a Telegram message (and push notification on my phone) whenever something bad happens
* Errors: push a message on errors
* Info: send me a message to my phone when the longest-running software in history (my script let's say) ended.

## Requisites

* [Telegram messanger](https://telegram.org/). I suggest to download the app from the phone as well.

## Configuration

Search the BotFather, the official bot that allows you to create bots :))

![Telegram BotFather](/images/telegram_notificator2.jpg)

Then, create a new bot:

    /newbot

Choose a name for your bot

    UltraNotifier

Choose a username for your bot, which must end with "_bot"

    ultranotifier_bot

Once the bot is created, you will have a long string that is the TOKENID. The message will be similar to:

    Use this token to access the HTTP API:

Now, the bot is only the "guy" who will send you the messages. It has to know the chat where to send them. For this reason, got to the search bar of Telegram, and search your bot. Then, start the bot:

    /start

You can now go to the website `https://api.telegram.org/bot[TOKENID]/getUpdates` (replacing `[TOKENID]` with the ID you received before) and search for your id.

![Telegram chat id](/images/telegram_notificator3.png)

Now you are ready to use a command line code to send your first notification

    $ curl -s -X POST https://api.telegram.org/bot[TOKENID]/sendMessage -d chat_id=[ID] -d text="Hello world"

## Python logger

I decided to write a simple Python logger that sends you a notification/message whenever something happens. Here you have the simple code, with the configuration before the class.


    import requests
    from logging import Handler, Formatter
    import logging
    import datetime
     
    TELEGRAM_TOKEN = 'PUT HERE YOUR TOKENID'
    TELEGRAM_CHAT_ID = 'PUT HERE YOUR CHATID'

    class RequestsHandler(Handler):
    	def emit(self, record):
    		log_entry = self.format(record)
    		payload = {
    			'chat_id': TELEGRAM_CHAT_ID,
    			'text': log_entry,
    			'parse_mode': 'HTML'
    		}
    		return requests.post("https://api.telegram.org/bot{token}/sendMessage".format(token=TELEGRAM_TOKEN),
    							 data=payload).content
     
    class LogstashFormatter(Formatter):
    	def __init__(self):
    		super(LogstashFormatter, self).__init__()
        
    	def format(self, record):
    		t = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        
    		return "<i>{datetime}</i><pre>\n{message}</pre>".format(message=record.msg, datetime=t)

It can be simply used as all the usual logger handlers:

	logger = logging.getLogger('trymeApp')
	logger.setLevel(logging.WARNING)
     
	handler = RequestsHandler()
	formatter = LogstashFormatter()
	handler.setFormatter(formatter)
	logger.addHandler(handler)
     
	logger.setLevel(logging.WARNING)
     
	logger.error('We have a problem')

The message will be:

![Telegram error notification](/images/telegram_notificator1.png)

## Java, Bash, others

Thanks to Daniele, now we have [a new repo with other languages as well](https://github.com/forons/telegram-log). I hope you will enjoy it. Thanks!








