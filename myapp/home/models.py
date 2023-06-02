from django.db import models

class supervisor(models.Model):
    id = models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100,null=True)
    e_mail=models.EmailField(max_length=100,null=True)
    mot_pass = models.CharField(max_length=150,null=True)
    
    def __str__(self):
        return f"{self.nom}"
    


