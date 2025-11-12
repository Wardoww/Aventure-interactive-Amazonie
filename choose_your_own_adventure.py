# Intro
def aventure():
    name = input("Écrit ton nom : ")
    print(f"\nBienvenue à cette aventure, {name} !\n")
    print("=" * 70 + "\n")

    while True:
        q1 = scene_jungle()

        if q1 == "gauche":
            scene_pont()
        elif q1 == "droite":
            q3 = scene_grotte()
            if q3 == "lumière":
                scene_rubis()
            elif q3 == "noir":
                chemin_noir()

        # Rejouer ?
        if not rejouer():
            print("\nMerci d'avoir joué !")
            break
        print("\n" + "=" * 70 + "\n")


# Fonctions pour chaque scène
def scene_jungle():
    while True:
        q1 = input(
            "\nSeul et perdu, tu es dans la jungle dense et humide d'Amazonie.\n"
            "Il se fait tard, il pleut et le soleil est presque complètement couché.\n"
            "Sur ta droite tu apperçois une entrée vers une grotte sombre et reculée,\n"
            "sur ta gauche un vieux pont suspendu en bois au loin dans une épaisse brume.\n"
            "Quel direction choisiras-tu ? (gauche/droite) : "
        ).lower()
        if q1 in ["gauche", "droite"]:
            return q1
        print("\nCette option n'est pas valide ! Réessaie.\n")


def scene_pont():
    while True:
        q2 = input(
            "\nUne fois arrivé près du pont, il te paraît encore plus long.\n"
            "Tu peux décider de sois marcher sur le pont vers l'autre coté de la rivière\n"
            "ou nager pour traverser. (marcher/nager) : "
        ).lower()
        if q2 == "marcher":
            print("\nTu entames la traversée du pont.\n"
                  "Soudainement tu entends un lourd craquement sous tes pieds.\n"
                  "Rapidement tu jettes un coup d'oeil et observes une des vieilles planches du pont se fracturer.\n"
                  "Le cordage qui semblait tenir le pont se rompit.\n"
                  "Le pont cédait sous ton poids et celui des années de non-entretien et tu finis emporté par le courant.\n"
                  "Fin de partie.\n")
            break
        elif q2 == "nager":
            print("\nLe courant était fort et l'eau plutôt marécageuse mais tu décidas tout de même de nager.\n"
                  "La traversée se passait bien et tu étais presque rendu sur l'autre rive quand un énorme crocodile couvert de balafres surgit de l'ombre.\n"
                  "Il t'agrippa violemment la jambe et un éclair laissa parraître sa gueule remplie de dents tranchantes comme des rasoirs.\n"
                  "Tu finis trainé jusqu'au fond de l'eau et dévoré vivant.\nFin de partie.\n")
            break
        else:
            print("\nCette option n'est pas valide ! Réessaie.\n")


def scene_grotte():
    while True:
        q3 = input(
            "\nUne fois l'embouchure de la grotte atteinte, tu sens un courant d'air froid s'en dégager.\n"
            "L'atmosphère y est pesante et tu n'y vois presque rien sauf une légère lumière dans le noir qui scintille grâce à la lueur de la lune.\n"
            "Veux-tu te diriger vers cette lumière scintillante ou continuer dans le noir ? (lumière/noir) : "
        ).lower()
        if q3 in ["lumière", "noir"]:
            return q3
        print("\nCette option n'est pas valide ! Réessaie.\n")


def scene_rubis():
    while True:
        q4 = input(
            "\nQuelques mètres plus loin, tu arrives finalement face à cette étrange lumière scintillante.\n"
            "Tu te penches pour observer d'avantage et il s'agit en fait d'un rubis !\n"
            "Prendras-tu le rubis ou tu rebrousses chemin ? (prendre/rebrousser) : "
        ).lower()
        if q4 == "prendre":
            print("\nDès que tu soulèves la pierre rouge écarlate du sol, tu entends un mécanisme s'enclencher.\n"
                  "Avant même de pouvoir réagir, un sifflement se fit entendre.\n"
                  "Une fléchette empoisonnée te heurta au niveau du cou et te laissa dans un état de paralysie complète.\n"
                  "Pendant plusieurs heures tu restas au sol conscient et agonisant de douleur.\n"
                  "Jusqu'à ce que tu entendes des cris et des pas se dirigeant vers ta position.\n"
                  "Cet alors qu'un petit groupe de 3 personnes semblant appartenir à une tribu récupéra ton corps et l'enmèna pour achever leurs rituel sanglant.\n"
                  "Fin de partie.\n")
            break
        elif q4 == "rebrousser":
            chemin_noir()
            break
        else:
            print("\nCette option n'est pas valide ! Réessaie.\n")


def chemin_noir():
    while True:
        q5 = input(
            "\nAprès de longues minutes de marche dans un silence lourd, tu atteins finalement un cul de sac.\n"
            "Tu remarques un levier bi-directionnel taillé dans la pierre froide et mouillé de la paroi rocheuse de la grotte.\n"
            "Tu peux soit actionner le levier vers la droite ou la gauche. (droite/gauche) : "
        ).lower()
        if q5 == "droite":
            print("\nLorsque tu tires le levier vers la droite, une trappe s'ouvre brusquement sous tes pieds.\n"
                  "Tu tombes alors sur des pics acérés qui te transperse et t'empale.\n"
                  "Tu meurs lentement te vidant de ton sang petit à petit sans que personnes ne vienne à ton secours.\n"
                  "Fin de partie.\n")
            break
        elif q5 == "gauche":
            print(
                "\nLorsque tu tires le levier vers la gauche, une lourde porte coulissante dissimulée dans la pierre s'ouvre lentement devant toi.\n"
                "C'est alors que tu découvres une salle secrète remplie de trésors perdus depuis des centaines d'années.\n"
                "Tu t'approches et aperçois des tonnes de pièces d'or, des bijoux incrustés de pierres précieuses massives et des artefacts anciens ayant une valeur inestimable.\n"
                "Tu as trouvé le trésor perdu ! Félicitations tu as réussis cette aventure !\n")
            break
        else:
            print("\nCette option n'est pas valide ! Réessaie.\n")


def rejouer():
    while True:
        choix = input("\nVeux-tu recommencer la partie ? (oui/non) : ").lower()
        if choix == "oui":
            return True
        elif choix == "non":
            return False
        else:
            print("\nCette option n'est pas valide ! Réessaie.\n")


# Lancer le jeu
aventure()
