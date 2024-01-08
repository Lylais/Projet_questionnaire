import random
score=0
# QCM sur lequel, on va travailler
qcm=[{'question': "Quelle est la capitale de l'Espagne :", 'exacte': "MADRID", 'inexacte': "BARCELONE", 'good points' : 3, 'bad points' : 1},
     {'question': "2 x 3 = ", 'exacte': "6", 'inexacte': "5", 'good points' : 3, 'bad points' : 1},
     {'question': "Un tuple est : ", 'exacte': "non mutable", 'inexacte': "mutable", 'good points' : 3, 'bad points' : 1},
     {'question': "Une liste est : ", 'exacte': "mutable", 'inexacte': "non mutable", 'good points' : 3, 'bad points' : 1},
     {'question': "range(5) est l'ensemble des entiers : ", 'exacte': "0;1;2;3;4", 'inexacte': "0;1;2;3;4;5", 'good points' : 3, 'bad points' : 1}
     ]

def interrogation(q,nbr):
    """ reçoit en entrée une liste de dictionnaire (le qcm) et un entier (choix de la question
      Cette fonction affiche la question,
                     affiche les 2 propositions aléatoirement,
                     lit et stocke la réponse de l’utilisateur 
                     affiche « Bonne réponse » ou « Mauvaise réponse »
    """
    global score
    question = q[nbr]['question']
    bonne_reponse = q[nbr]['exacte']
    mauvaise_reponse = q[nbr]['inexacte']
    good_point = q[nbr]['good points']
    bad_point = q[nbr]['bad points']
    options = [bonne_reponse, mauvaise_reponse]
    random.shuffle(options)  # Shuffle the options
    print(question, '\n')
    print("1-", options[0], '\n' "2-", options[1]) 
    reponse = None
    user_answer = None

    while reponse not in ['1', '2']:
        reponse = str(input("Quelle est la bonne réponse? Entrez 1 ou 2: "))
        if reponse not in ['1', '2']:
            print("Veuillez choisir une réponse entre 1 et 2 !\n")

        if reponse in ['1', '2']:
            user_answer = options[int(reponse) - 1]
            if user_answer == bonne_reponse:
                score += good_point
                print("Bien joué, la réponse est correcte!\n")
            else:
                score -= bad_point
                print("Dommage, c'est la mauvaise réponse!\n")
    
        

def questionnaire(q):
    global score
    i = 0
    

    
    
    # Trouver et extraire la valeur de 'scale_point'
    scale_point_dict = next((item for item in q if 'scale_point' in item), None)
    scale_point = scale_point_dict.get('scale_point', 15) if scale_point_dict else 15
    
    # Supprimer le dictionnaire avec la clé 'scale_point'
    q.remove(scale_point_dict)
    number_list = list(range(len(q)))
    print(number_list)

    print(q)

    random.shuffle(number_list)  # Shuffle the list of question numbers
    for nbr in number_list:  # Iterate over the shuffled list
        print("-- Question", i + 1, "--")
        interrogation(q, nbr)
        i += 1
        if score < 0:
            score = 0

    print("Fin du questionnaire, merci d'avoir répondu!")
    print(f"Votre score est de {score}/{scale_point}")


