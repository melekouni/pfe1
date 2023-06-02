
from django.contrib.gis.db import models
from django.utils import timezone
from home.models import supervisor
# Create your models here.

# Create your models here.

class client(models.Model):
    nom=models.CharField(max_length=100,null=True)
    e_mail=models.EmailField(max_length=100,null=True)
    mot_pass = models.CharField(max_length=150,null=True)
    superviseur = models.ForeignKey( supervisor ,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.nom }"

class project(models.Model):
    id= models.CharField(primary_key=True,max_length=100)
    nom= models.CharField(max_length=100, null=True )
    region= models.CharField(max_length=100,null=True)
    dat_deb = models.DateField(null=True)
    dat_fin = models.DateField(null=True)
    client = models.ForeignKey(client, null=True, on_delete=models.CASCADE)

    def __str__(self):
        
        return  self.nom



class myPolygon(models.Model):
   
    id = models.AutoField(primary_key=True)
    nom = models.CharField(null=True , max_length=80)
    
    geom = models.PolygonField(null=True)
    project = models.ForeignKey( project ,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return  self.nom


class point(models.Model):
   id = models.AutoField(primary_key=True)
   nom = models.CharField(null=True , max_length=80)
   cord = models.PointField()
   parcelle = models.OneToOneField(myPolygon, null=True, on_delete=models.CASCADE)
   project = models.ForeignKey( project ,null=True,on_delete=models.CASCADE)
   référence = models.CharField(null=True, max_length=50 )
   RSSI = models.FloatField(null=True)
   FWI=models.BigIntegerField(null=True)



class Post(models.Model):
    id= models.AutoField(primary_key=True)
    temperature = models.BigIntegerField()
    humidity = models.BigIntegerField()
    
    wind=models.BigIntegerField(default=0)
    node = models.ForeignKey( point,null=True,on_delete=models.CASCADE)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'Temperature: {self.temperature}, Humidity: {self.humidity} ,wind:{self.wind}'
    

