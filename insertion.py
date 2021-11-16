from modele import Utilisateur, Album, Photo

user1 = Utilisateur(prenom="Tracey Ellen", nom="MANSHAL")
user2 = Utilisateur(prenom="Lior", nom="CHAMLA")
user3 = Utilisateur(prenom="Aissatou", nom="MBODJ")

album1 = Album(titre='Noël', public=True, utilisateur=user1)
album2 = Album(titre="Végas", public=False, utilisateur=user3)
album3 = Album(titre="Sortie Plage", public=False, utilisateur=user2)

photo1 = Photo(image="photo-1.jpg", date="27/04/2021", heure="16h16")
photo2 = Photo(image="photo-2.jpg", date="07/12/2021", heure="01h00")
photo3 = Photo(image="photo-3.jpg", date="13/07/2021", heure="21h30")
photo4 = Photo(image="photo-4.jpeg", date="01/01/2021", heure="00h00")

album1.addPhoto(photo1)
album1.addPhoto(photo4)
album3.addPhoto(photo1)
album3.addPhoto(photo2)
album3.addPhoto(photo3)
album3.addPhoto(photo4)
album2.addPhoto(photo4)
