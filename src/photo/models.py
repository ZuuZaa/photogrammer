from django.db import models
from account.models import CustomUser

class Photo(models.Model):

    img = models.ImageField(upload_to='images')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    description = models.CharField(max_length=250)
    sharing = models.BooleanField(default=False)
    shared_users = models.ManyToManyField(CustomUser, related_name='shared_user',blank=True,null=True)
    sharing_end_date = models.DateField()

