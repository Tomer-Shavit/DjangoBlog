from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Here we are creating a new model, a model is the source of information about our data, each model will represent a table in our database
# Each new model will inherit the models.Model class
# here for example we are making the Post model for all our posts, each post will have its attrebutes and they will be stored in our database
# We are also creating a __str__ function for this class for it to be more readable when debugging 
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # After clicking the "Update" button when updating a page, django will want to rederect us, and this function will set the correct path
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
