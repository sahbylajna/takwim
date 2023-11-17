# client_api/models.py

from django.db import models

class ClientUser(models.Model):
    phone = models.CharField(max_length=15, unique=True)
    firstnamear = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    lastnamear = models.CharField(max_length=50)
    firstnameen = models.CharField(max_length=50)
    lastnameen = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
    uid = models.CharField(max_length=50, unique=True)
    singater = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    token = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    supvaser_id = models.ForeignKey('Client.ClientUser',related_name='supvaser', on_delete=models.CASCADE, null=True)  # Replace 'YourClientModel' with your actual client model

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['firstnamear']
    def __str__(self):
        return self.phone
    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False
