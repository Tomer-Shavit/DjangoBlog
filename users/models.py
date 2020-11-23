from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image

User = get_user_model()

# We are creating a new model to be store in our database as a table and we inheriting from the models.Model class
# and also creating a str function for readability
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Here we are modifying the save() of the new model, by changing the size of the image when saving it
    #pylint: disable=signature-differs
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path) 