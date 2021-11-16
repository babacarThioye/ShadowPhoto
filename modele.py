import os

from sqlobject import *

db_filename = os.path.abspath('bdd.sqlite3')
connection_string = 'sqlite:' + db_filename
connection = connectionForURI(connection_string)
sqlhub.processConnection = connection


# connection.debug = True


class Utilisateur(SQLObject):
    nom = StringCol()
    prenom = StringCol()
    albums = MultipleJoin("Album")


class Album(SQLObject):
    titre = StringCol(unique=True)
    public = BoolCol()
    utilisateur = ForeignKey("Utilisateur", cascade="null")
    index_utilisateur = DatabaseIndex("utilisateur")
    photo = RelatedJoin("Photo", intermediateTable='albums_photos')


class Photo(SQLObject):
    image = StringCol()
    date = StringCol()
    heure = StringCol()
    album = RelatedJoin("Album", intermediateTable='albums_photos')


Utilisateur.createTable(ifNotExists=True)
Album.createTable(ifNotExists=True)
Photo.createTable(ifNotExists=True)
