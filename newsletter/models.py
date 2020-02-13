from django.db import models

class Email(models.Model):
    # Required Information
    user_email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_email) + " - " + str(self.date_added)