from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    A Django management command for calling a
    chat bot's training method.
    """

    help = 'Trains the database used by the chat bot'
    can_import_settings = True

    def handle(self, *args, **options):
        from chatterbot import ChatBot
        from chatterbot.ext.django_chatterbot import settings
        from chatterbot.trainers import ChatterBotCorpusTrainer

        chatterbot = ChatBot(**settings.CHATTERBOT)

        trainer = ChatterBotCorpusTrainer(chatterbot)

        trainer.train('chatterbot.corpus.english')

        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/action.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/baseball.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/basketball.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/beatles.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/comedy.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/football.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/harry_potter.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/horror.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/icehockey.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/movies.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/music.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/music_and_movies.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/pop.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/rap.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/rock.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/star_wars.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/superhero.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/thriller.json")
        trainer.train("/Users/willryan/PycharmProjects/django_chat_try/chat_corpus/newwest_twitter.json")

        # Django 1.8 does not define SUCCESS
        if hasattr(self.style, 'SUCCESS'):
            style = self.style.SUCCESS
        else:
            style = self.style.NOTICE

        self.stdout.write(style('Starting training...'))
        training_class = trainer.__class__.__name__
        self.stdout.write(style('ChatterBot trained using "%s"' % training_class))
