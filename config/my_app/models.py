from django.db import models
from django.contrib.auth.models import User



class CustomerUser(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='birthday')
    name = models.CharField(max_length=52)
    email = models.EmailField(unique=True)
    birth_day = models.DateField()
    sent_day = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.name}|{self.email}"
    
    


class BirthdayWish(models.Model):
    customer = models.ForeignKey(CustomerUser,  on_delete=models.CASCADE, related_name='wishes')
    name = models.CharField(max_length=52)
    message = models.TextField()
    sent_day = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.name}|{self.sent_day}"
    