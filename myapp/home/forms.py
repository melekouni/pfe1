from django import forms

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from django import forms
from .models import *




class Form_supervisor(forms.Form):
    nom = forms.CharField(required=True, max_length=supervisor._meta.get_field(
        'nom').max_length, widget=forms.TextInput(attrs={'id': 'username', 'name': 'username','placeholder': 'Entre username'}) )
    
    email = forms.EmailField(max_length=supervisor._meta.get_field('e_mail').max_length, required=True, widget=forms.EmailInput(attrs={'id': 'username', 'name': 'username','placeholder': 'Entre Email'}))
    
    mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput( attrs={'id': 'password', 'name': 'password', 'placeholder': 'Password'}))
    confirmation_mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'id': 'password', 'name': 'password', 'placeholder': 'Confirmer Password'}))

    def is_valid(self):
            nom = self.data['nom']
            if any(char.isdigit() for char in nom):
                self.add_error("nom", "Nom est incorrect!")
           
            
            email = self.data['email']
            if supervisor.objects.filter(e_mail=email).exists():
                self.add_error("email", "email déja existant!")
            
           
            mot_de_passe = self.data['mot_de_passe']
            if len(mot_de_passe) < 8:
                self.add_error(
                    "mot_de_passe", "Le mot de passe doit contenir au moins 8 caractères.")
           
            value = super(Form_supervisor, self).is_valid()
            return value


    def enregistrer(self):
            nom = self.cleaned_data['nom']
           
            email = self.cleaned_data['email']
            
            
            confirmation_mot_de_passe = self.cleaned_data['confirmation_mot_de_passe']
            
            data = supervisor(nom=nom, e_mail=email,mot_pass=confirmation_mot_de_passe)
            data.mot_pass=(make_password(data.mot_pass))
            data.save()


