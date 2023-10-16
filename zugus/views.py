from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Team
from zugus.forms import CreateAccountForm, LoginForm
from django.contrib.auth import authenticate, login


def index(request):
    # Récupérez toutes les équipes depuis la base de données
    teams = Team.objects.all()
    # Passez les équipes au contexte du template
    return render(request, 'index-2.html', {'teams': teams})

def createAccount(request):

    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Le compte a été créé avec succès!')
            # Redirigez vers la page souhaitée après la création du compte.
            return redirect('createAccount')
    else:
        form = CreateAccountForm()
    return render(request, 'account.html', {'form':form})

def connectAccount(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Essayez d'authentifier l'utilisateur
            user = authenticate(request, username=email, password=password)
            if user is not None:
                # L'utilisateur existe et le mot de passe est correct
                login(request, user)
                return redirect('device')
            else:
                messages.error(request, "Email ou mot de passe incorrect.")
    else:
        form = LoginForm()

    return render(request, 'connexion.html', {'form': form})





