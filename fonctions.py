import numpy as np
import datetime
import re

#Fonction de verification pour les données du projet 4

def birth_verif(value):
    """Vérification que la date de naissance est bien une date possible
    """
    date = datetime.datetime.now()

    if value > 1900 and value < date.year:
        return value
    return np.NaN

def sex_verif(value):
    """Vérification que le sexe entré est un sexe qui existe, nous avons pour ça la liste VALID_SEX
    """
    VALID_SEX = ['f','m']

    if value not in VALID_SEX:
        return np.NaN
    return value

def clientId_verif(value):
    """Vérification que tous les identifiants clients on la même architecture
    """
    found = re.search('c_\d*', value)
    if found is None:
        return np.NaN
    return value

def idProd_verif(value):
    """Fonction qui verifie que l'identifiant de tous les produits suis la même logique
    """
    found = re.search('^[0-2]_\d+', value)
    if found is None:
        return np.NaN
    return value

def sessionId_verif(value):
    """Fonction qui verifie l'identifiant des sessions
    """
    found = re.search('^s_\d+', value)
    if value is None:
        return np.NaN
    return value

def price_verif(value):
    """Fonction qui verifie qu'un prix est positif
    """
    if value < 0:
        return np.NaN
    return value

def categ_verif(value):
    """Verification que la categorie est une categorie qui existe, la liste des categories existante est donner par VALID_CATEG
    """
    VALID_CATEG = [0,1,2]

    if value not in VALID_CATEG:
        return np.NaN
    return value

def date_verif(value):
    """Cette fonction verifie que les dates soit bien toute au même formats, a savoir que des digits
    """
    found = re.search('^\D+', value)
    if found is None:
        return value
    else:
         return np.NaN
