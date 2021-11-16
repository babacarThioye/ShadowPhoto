import datetime

import sqlobject
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from modele import Photo, Album
from .forms import Photo_form, Photo_form_Add


# Create your views here.
def one_photo(request, pk_a, pk_p):
    photo = Photo.get(id=pk_p)
    pk_a = pk_a
    cursor = sqlobject.sqlhub.processConnection.getConnection().cursor()
    albums = cursor.execute("select album.id, album.titre from album, photo, albums_photos "
                            "where album.id = albums_photos.album_id and photo.id = albums_photos.photo_id "
                            "and photo.id = ?  order by album.titre desc", (pk_p))
    context = {'titre': 'photo' + pk_p, 'photo': photo, 'albums': albums, 'pk_a': int(pk_a)}
    return render(request, 'photo/affiche_photo.html', context, )


def add_photo(request, pk_a):
    if request.method == 'POST':
        form = Photo_form_Add(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            image = cd.get('image')
            date = cd.get('date')
            heure = cd.get('heure')
            date = date.strftime("%d/%m/%Y")
            heure = heure.strftime("%Hh%M")
            try:
                fss = FileSystemStorage("static/photos/")
                file = fss.save(image.name, image)
                fss.url(file)
                photo = Photo(image=str(image), date=str(date), heure=str(heure))
                album = Album.get(id=pk_a)
                album.addPhoto(photo)
                return redirect('http://127.0.0.1:8000/album ' + pk_a + "/")
            except:
                pass
    form = Photo_form_Add()
    context = {'titre': 'Ajout photo', 'form': form, "act": 'Ajouter', 'add': True}
    return render(request, 'photo/form_photo.html', context)


def update_photo(request, pk_a, pk_p):
    photo = Photo.get(id=pk_p)
    if request.method == 'POST':
        form = Photo_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            date = cd.get('date')
            heure = cd.get('heure')
            date = date.strftime("%d/%m/%Y")
            heure = heure.strftime("%Hh%M")
            photo.date = str(date)
            photo.heure = str(heure)
            return redirect('http://127.0.0.1:8000/album ' + pk_a + "/photo " + pk_p + "/")

    dat = str(photo.date).split("/")
    date = datetime.date(int(dat[2]), int(dat[1]), int(dat[0]))

    heure = str(photo.heure).split("h")
    heure = datetime.time(int(heure[0]), int(heure[1]), )
    image = photo.image
    form = Photo_form(initial={'date': date, 'heure': heure, 'image': image})
    context = {'titre': 'Modifier photo' + pk_p, 'form': form, 'act': 'Modifier'}
    return render(request, 'photo/form_photo.html', context)


def delete_photo(request, pk_a, pk_p):
    photo = Photo.get(id=pk_p)
    album = Album.get(id=pk_a)
    album.removePhoto(photo)
    return redirect('http://127.0.0.1:8000/album ' + pk_a + "/")
