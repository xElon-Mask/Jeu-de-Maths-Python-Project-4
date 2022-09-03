import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10


# Posez la question à l'utilisateur : Calculez : 1(nombr aléatoire) + 5(nombre alétoire) = 
# 1 et 5 sont des nombres aléatoires qu'ils faudra définir
# Créez une fonction poser_question(): qui ne prend pas de paramètres, on utilise nombre min et nombre max directement dans le corps de la fonction
# Tirez au sort vos 2 nombres a et b. Vous allez devoir demander la réponse à l'utilisateur, coonvertir la réponse en int, et tester si c'est bien égal à a + b
# pas de cas d'erreurs, faites simple et afficher réponse correcte ou incorrecte


def poser_question():
    # a, b
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    reponse_user = input(f"Calculez : {a} + {b} = ")
    reponse_user_convert = int(reponse_user)
    if reponse_user_convert == a + b:
        print("Correct !")
    else:
        print('Incorrect.')



poser_question()