# Chat App

> Django Chat App that uses the Chatterbot module

I will be uploading this to the internet on the domain name techchatbot.com. I am currently
working on figuring out the linux server issues with uploading a Django app.

### Requirements

***Django***

***ChatterBot***

```shell script
pip install -r requirements.txt
```

### Training
I compiled the training data mostly from the twitter API and various sources across the
internet. I put them in JSON files in the chat_corpus directory where they are grouped together
by subject


This command will train the bot. It takes approximately 15 - 30 minutes to train. I used
this amount of data because more data will cause performance issues.
```shell script
python manage.py train
```

