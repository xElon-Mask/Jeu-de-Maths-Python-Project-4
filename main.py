import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4


# Posez la question à l'utilisateur : Calculez : 1(nombr aléatoire) + 5(nombre alétoire) = 
# 1 et 5 sont des nombres aléatoires qu'ils faudra définir
# Créez une fonction poser_question(): qui ne prend pas de paramètres, on utilise nombre min et nombre max directement dans le corps de la fonction
# Tirez au sort vos 2 nombres a et b. Vous allez devoir demander la réponse à l'utilisateur, coonvertir la réponse en int, et tester si c'est bien égal à a + b
# pas de cas d'erreurs, faites simple et afficher réponse correcte ou incorrecte


# 2 : Posez plusieurs questions à l'user, posez 4 questions en bouclant, rajouter un print en annonçant le numéro de la question (question n°1 sur 4)

# 3 : Ajouter la gestion d'un nombre de points. nb_points = 0, et à chaque fois que vous donnez une bonne réponse, vous aurez plus 1 point, et à la fin
# afficher votre note est par exemple 2/4
# incrémenter le nb_points dans la boucle for, meilleure implémentation que de passer par une variable globale


# 4 : Rajoutez la note, si 4/4 => Excellent
# si 0/4 => révisez vos Maths !
# inferieur ou superieur à la moyenne donc calculez la moyenne qui est le nombre de questions/2 il va donc falloir convertir en int() pour éviter les floats
# donc int(NB_Questions/2)
# si > à la moyenne, on affiche "Pas mal"
# < moyenne on affiche "Peut mieux faire"

def poser_question():
    
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    reponse_user = input(f"Calculez : {a} + {b} = ")
    reponse_user_convert = int(reponse_user)
    if reponse_user_convert == a + b:
        return True
    return False
    
    


nb_points = 0
for i in range(0, NB_QUESTIONS):
        print(f"Question n°{i + 1} sur {NB_QUESTIONS}")
        # la ligne du dessous sous entend if pose_question() == True:
        if poser_question():
            print("Correct !")
            nb_points += 1
        else:
            print('Incorrect.')
        print()
            
            
print(f"Votre note est {nb_points} / {NB_QUESTIONS}")
