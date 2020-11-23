from django.apps import AppConfig


# Here we are making sure that our signals will be called once, and to do that we rae importing it only when the ready func is called
# the ready() will be called once the app regestry is completed in django (in this case the users app)
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        #pylint: disable=unused-import
        import users.signals
     