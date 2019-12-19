from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your models here.


class UploadFile(models.Model):
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)
    upload = models.FileField(upload_to=user_directory_path)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.upload
    # name = models.CharField(max_length=50)
    # file = models.FileField(upload_to="uploads/")
