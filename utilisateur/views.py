from django.shortcuts import render, redirect

# Create your views here.
from modele import Utilisateur, Album
from utilisateur.forms import User_form


def index(request):
    users = Utilisateur.select()
    context = {'users': users, 'titre': 'Accueil'}
    return render(request, 'utilisateur/liste_utilisateur.html', context)


def one_user(request, pk):
    user = Utilisateur.get(id=pk)
    albums = Album.select(Album.q.utilisateur == user)
    context = {'user': user, 'titre': user.prenom + '' + user.nom, 'albums': albums}
    return render(request, 'utilisateur/affiche_utilisateur.html', context)


def add_user(request):
    mess = ""
    if request.method == 'POST':
        form = User_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            nom = cd.get('nom')
            prenom = cd.get('prenom')
            try:
                user = Utilisateur(nom=str(nom).upper(), prenom=prenom)
                return redirect('http://127.0.0.1:8000/utilisateur ' + str(user.id) + '/')
            except:
                mess = "Une erreur est survenue lors de l'ajout de l'utilisateur!!!"
                pass

    form = User_form()
    context = {'form': form, "mess": mess}
    return render(request, 'utilisateur/ajout_user.html', context)


def a_propos(request):
    return render(request, 'a_propos.html', )
