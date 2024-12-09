from django.db import models
class Produit(models.Model):
    nom = models.CharField(max_length=255)
    label = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Secteur(models.Model):
    nom = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

class Representative(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField()
    adress = models.TextField()
    telephone = models.CharField(max_length=15)

class Commercialization(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)

class Gestion(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE)
    label = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)



class Attachment(models.Model):
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    sector = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE)
    commercialization = models.ForeignKey(Commercialization, on_delete=models.CASCADE, null=True, blank=True)
    confirmed = models.BooleanField(default=False)




# Create your models here.
