import pickle
import os
from gestion_qcm import questionnaire
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, 'liste_nom_qcm.txt')
dossier_nom = "Save_questionaire"  # Remplacez cela par le nom du dossier que vous souhaitez
chemin_dossier = os.path.join(script_directory, dossier_nom)


def CreerQcm():
    """ fonction permettant de créer un fichier portant le nom de QCM"""
    
    qcm = []
    scale_point = 0
    nom=input("Saisir le nom de votre QCM : ")
    nom = nom.strip()
    
  # Créez le dossier s'il n'existe pas déjà
    if not os.path.exists(chemin_dossier):
        os.makedirs(chemin_dossier)
    
    # Obtenez le chemin complet pour le fichier pickle
    nom_fichier_pickle = f'{nom}.pkl'
    chemin_pickle = os.path.join(chemin_dossier, nom_fichier_pickle)

    while True:
        question = input("Veuillez entrer la question : ")
        # Ajoutez '?' à la fin de la question si ce n'est pas déjà fait
        question = question.strip() + '?' if not question.strip().endswith('?') else question.strip()
        
        bonne_reponse = input("Veuillez entrer la bonne réponse : ")
        mauvaise_reponse = input("Veuillez entrer la mauvaise réponse : ")
        
        # Gestion d'erreur pour la saisie des points
        while True:
            try:
                point_bonne_reponse = int(input("Veuillez entrer le nombre de points rapportés par la bonne réponse (doit être supérieur à 0) : "))
                point_mauvaise_reponse = int(input("Veuillez entrer le nombre de points perdus par la mauvaise réponse (doit être supérieur ou égal à 0) : "))
                
                # Vérification des exigences
                if point_bonne_reponse > 0 and point_mauvaise_reponse >= 0:
                    print("Barème valide")
                else:
                    print("Les points doivent être supérieurs à 0 (pour la bonne réponse) et supérieurs ou égaux à 0 (pour la mauvaise réponse).")
            except ValueError:
                print("Veuillez entrer des chiffres pour les points.")
        
        scale_point += point_bonne_reponse
        qcm.append({
            'question': question,
            'exacte': bonne_reponse,
            'inexacte': mauvaise_reponse,
            'good points': point_bonne_reponse,
            'bad points': point_mauvaise_reponse
        })

        print(qcm)
        print(scale_point)

        choix_utilisateur = input("Voulez-vous ajouter une autre question ? O/N ").upper()
        if choix_utilisateur != 'O':
            qcm.append({'scale_point': scale_point})
            print(qcm)

            with open(file_path, 'r') as fichier:
                # Utilisez la fonction readlines() pour obtenir une liste de toutes les lignes du fichier
                lignes = fichier.readlines()

            with open(file_path,'a') as file :
                file.write(f'{nom}\n')

            with open(chemin_pickle, 'wb') as d:
                pickle.dump(qcm, d)
                
            print(f"Fichier pickle créé avec succès dans le dossier : {chemin_dossier}")
            print(f"Chemin complet du fichier pickle : {chemin_pickle}")
            return scale_point




def ModyQcm(): #Dont work
    while True:
        qcm = []
        question = input("Veuillez entrer la question : ")
        bonne_reponse = input("Veuillez entrer la bonne réponse : ")
        mauvaise_reponse = input("Veuillez entrer la mauvaise réponse : ")
        point_bonne_reponse = int(input("Veuillez entrer le nombre de points rapportés par la bonne réponse : "))
        point_mauvaise_reponse = int(input("Veuillez entrer le nombre de points perdus par la mauvaise réponse : "))

        qcm.append({
            'Question': question,
            'exacte': bonne_reponse,
            'inexacte': mauvaise_reponse,
            'good points': point_bonne_reponse,
            'bad points': point_mauvaise_reponse
        })

        scale_point += point_bonne_reponse

        print(qcm)
        print(scale_point)

        choix_utilisateur = input("Voulez-vous ajouter une autre question ? O/N ").upper()  


def start():
   
    file_size = os.path.getsize(file_path)
    if file_size < 1:
        CreerQcm()
    else : 
        print("Bienvenu au menu du jeu ! ")
        print("1. Lancer une partie \n 2. Modifier un QCM \n 3. Créer un QCM")
        choice_start = None
        while choice_start not in ['1', '2', '3'] :
            choice_start = str(input("Veuillez choisir une option : "))
            if choice_start not in ['1', '2', '3']:
                print("Veuillez rentrer une réponse correcte")
            elif choice_start == '1':
                lecture_qcm()
            elif choice_start =='2':
                ModyQcm()
            elif choice_start =='3':
                CreerQcm()


# à l'issue de l'exécution, vous remarquerez la présence d'un fichier texte dans le dossier
# Pour tester, décommenter la ligne ci-dessous et nommer le qcm : qcm1
# CreerQcm()
def lecture_qcm():

    with open(file_path, 'r') as file:
        lignes = file.readlines()

    print("Liste des questionnaires : ")
    for i, ligne in enumerate(lignes, 1):
        print(f"{i}. {ligne.strip()}")

    number_list = [str(i) for i in range(1, len(lignes) + 1)]
    print(number_list)

    user_choice = input("\nVeuillez choisir un des questionnaires ici présent : ")

    while user_choice not in number_list:
        print("Veuillez entrer une option correcte")
        user_choice = input("Veuillez choisir un des questionnaires ici présent : ")

    # Obtenez le nom du questionnaire sélectionné
    index_questionnaire = int(user_choice) - 1
    nom_questionnaire = lignes[index_questionnaire].strip()
    print(nom_questionnaire)
    # Construisez le chemin complet du fichier pickle
    chemin_pickle = os.path.join(chemin_dossier, f'{nom_questionnaire}.pkl')
    print(chemin_pickle)
    # Vérifiez si le fichier pickle existe avant de le désérialiser
    if os.path.exists(chemin_pickle):
        with open(chemin_pickle, 'rb') as file_pickle:
            qcm_deserialize = pickle.load(file_pickle)
            print("Désérialisation réussie :")
            questionnaire(qcm_deserialize)
            

    else:
        print("Le fichier pickle n'existe pas pour le questionnaire sélectionné.")
    print("Ok")

    # à compléter
if __name__ == "__main__" : 
    start()
