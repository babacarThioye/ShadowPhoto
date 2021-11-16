import sqlobject
from django.shortcuts import render, redirect

# Create your views here.
from album.forms import Album_form
from modele import Album, Utilisateur


def one_album(request, pk_a):
    album = Album.get(id=pk_a)
    cursor = sqlobject.sqlhub.processConnection.getConnection().cursor()
    photos = cursor.execute("select photo.id, image from album, photo, albums_photos "
                            "where album.id = albums_photos.album_id and photo.id = albums_photos.photo_id "
                            "and album.id = ? order by image", (pk_a))
    context = {'titre': 'Album ' + album.titre, 'album': album, 'photos': photos, }
    return render(request, 'album/affiche_album.html', context)


def add_album(request, pk_u):
    message = ''
    if request.method == 'POST':
        form = Album_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            titre = cd.get('titre')
            public = cd.get('public')
            try:
                user = Utilisateur.get(id=pk_u)
                Album(titre=titre, public=public, utilisateur=user)
                return redirect('http://127.0.0.1:8000/utilisateur ' + pk_u + "/")
            except:
                message = f'Titre album {titre} déja utilisé!!!'
    form = Album_form()
    context = {'titre': 'Ajout album' + pk_u, 'form': form, 'mess': message}
    return render(request, 'album/form_album.html', context)
