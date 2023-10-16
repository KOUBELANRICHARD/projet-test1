from django.db import models
from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Team(models.Model):
    name = models.CharField(max_length=100)
    fonction = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    dateEmbauche = models.DateField(null=True, blank=True)
    timeConsultation = models.TimeField()
    posteDescription = models.TextField()
    experience = models.PositiveIntegerField()  
    contrat = models.BooleanField(default=False)  
    linked = models.URLField()
    slug = models.SlugField()  
    salaire = models.DecimalField(max_digits=10, decimal_places=2) 

class Compte(models.Model):
    username = models.CharField(max_length=25)  
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=128)  # length for hashed password
    dateCreation = models.DateField(auto_now_add=True)
    slug = models.SlugField() 
    is_active = models.BooleanField(default=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username
    
    class device(models.Model):
        name = models.CharField(max_length=25)  
        type = models.CharField(max_length=25) 
        localisation = models.CharField(max_length=50) 
        dateCreation = models.DateField(auto_now_add=True)
        slug = models.SlugField() 
        is_active = models.BooleanField(default=True)





