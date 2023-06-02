from django import forms 
from django.forms import ModelForm
from .models import  project , client
from home.models import supervisor
from django.contrib.auth.models import User


# create a project form 
class projectform(ModelForm):
     class Meta:
        model = project
        fields = ('id','nom')
        labels = {
            'id'  :'',
            'nom' :'' ,
           
  
        }
        widgets = {
            'id' : forms.TextInput(attrs={'class' : 'form-control  form-control-lg bg-light fs-6 shadow p-3 mb-5 bg-body rounded', 'placeholder' : 'id project' }),
            'nom' : forms.TextInput(attrs={'class ': 'form-control  form-control-lg bg-light fs-6 shadow p-3 mb-5 bg-body rounded', 'placeholder' : 'nom project' }),
            
           
        }
       
            
class Form_client(forms.Form):
    nom = forms.CharField(required=True, max_length=client._meta.get_field(
        'nom').max_length, widget=forms.TextInput(attrs={ 'class' : 'form-control    fs-6 shadow p-3 mb-5 bg-body rounded', 'id': 'username', 'name': 'username','placeholder': 'Entre username'}))
    
    
    email = forms.EmailField(max_length=client._meta.get_field(
        'e_mail').max_length, required=True, widget=forms.EmailInput(attrs={ 'class ': 'form-control    fs-6 shadow p-3 mb-5 bg-body rounded', 'id': 'username', 'name': 'username','placeholder': 'Entre Email'}))
    
    mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput( attrs={'class' : 'form-control   fs-6 shadow p-3 mb-5 bg-body rounded' , 'id': 'password', 'name': 'password', 'placeholder': 'mot de passe' }))
    
    confirmation_mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(attrs={  'class' : 'form-control    fs-6 shadow p-3 mb-5 bg-body rounded', 'id': 'password', 'name': 'password', 'placeholder': 'confirmation mot de passe' }))

    def is_valid(self):
            nom = self.data['nom']
            if any(char.isdigit() for char in nom):
                self.add_error("nom", "Nom est incorrect!")
            email = self.data['email']
            if client.objects.filter(e_mail=email).exists():
                self.add_error("email", "email déja existant!")
            mot_de_passe = self.data['mot_de_passe']
            if len(mot_de_passe) < 8:
                self.add_error(
                    "mot_de_passe", "Le mot de passe doit contenir au moins 8 caractères.")
            confirmation_mot_de_passe = self.data['confirmation_mot_de_passe']
            if confirmation_mot_de_passe != mot_de_passe:
                self.add_error("confirmation_mot_de_passe",
                            "Les mots de passe ne correspondent pas.")
            value = super(Form_client, self).is_valid()
            return value


    def enregistrer(self,user):
            nom = self.cleaned_data['nom']
            email = self.cleaned_data['email']
            confirmation_mot_de_passe = self.cleaned_data['confirmation_mot_de_passe']
            print('aaaaaaaccccccccccccccc')
            print(id)
            super = supervisor.objects.get(nom=user)
            print(super)

            data = client (nom=nom, e_mail=email, mot_pass= confirmation_mot_de_passe ,superviseur=super)

            data.save()
            data = User.objects.create_user(nom, email, confirmation_mot_de_passe)
            data.save()













