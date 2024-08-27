
class Joueur():
    def __init__(self) -> None:
        pass

    def getMot():
        pass

    def getPositionContact()->tuple:
        # c'est un tuple avec la position x y avec lequel le mot placé sera en contact
        pass


    # seulement si le joueur joue en premier
    def getMilieu():
        pass
    def getSens():
        pass


class Plateau ():
    def __init__(self):

        self.repartition_des_lettres = {"A" : 9,"B":2,"C" : 2, "D":3,"E":15,"F":2,"G":2,"H":2,"I":8,"J":1,"K":1,"L":5,"M":3,"N":6,
            "O":6,"P":2,"Q":1,"R":6,"S":6,"T":6,"U":6,"V":2,"W":1,"X":1,"Y":1,"Z":1,"JOKER":2}
            
        self.valeur_des_lettres = {"A" : 1,"B":3,"C" : 3, "D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,"K":10,"L":1,"M":2,"N":1,
            "O":1,"P":3,"Q":8,"R":1,"S":1,"T":1,"U":1,"V":4,"W":10,"X":10,"Y":10,"Z":10,"JOKER":0}

        self.plateau  = [["0"]*15 for _ in range(15)]
        self.plateau[7][7] = "X" 

        self.liste_joueurs = [] # liste de d'objet Joueur

        self.liste_mots = [] # liste des mots joués 

        



    def placer_mot(self,mot):
        if len(self.liste_mots) ==0 :
            index_milieu = int(input("quelle lettre je mets au millieu, entrez le numéro de la lettre (1 à "+str(len(mot))+") : ")) # joueur.getMilieu
            sens = str(input("horizontal ou vertical (h/v) : ")) # joueur.getSens

            if sens=="h":
                for i in range(len(mot)):
                    self.plateau[7][i+(-index_milieu+1)+7] = mot[i] #si je choisi la lettre 1 alors elle est au milieu du plateau
            elif sens=="v":
                for i in range(len(mot)):
                    self.plateau[i+(-index_milieu+1)+7][7] = mot[i] 
            else : 
                print("tu fais n'import quoi")

        else : 
            estPasse = False
            for i in  range(len(self.plateau)):
                if estPasse : break

                for j in range(len(self.plateau[0])):
                    # x,y = joueur.getPositionContact()

                    if self.plateau[i][j] == mot[0]:
                    #  if self.plateau[i][j] == self.plateau[x][y]
                    
                        if (self.plateau[i][j-1] != "0" or self.plateau[i][j+1] !="0" ) and self.plateau[i+1][j-1]=="0"   : 
                            for lettre in range(len(mot)):
                                self.plateau[lettre+i][j] = mot[lettre] # vertical


                        elif self.plateau[i][j-1] == "0":
                            for lettre in range(len(mot)):
                                self.plateau[i][lettre+j] = mot[lettre] # horizontal

                        estPasse = True


                            
        self.liste_mots.append(mot)
        



plateau = Plateau()
plateau.placer_mot("SALUT")
plateau.placer_mot("SALUT")
plateau.placer_mot("TUER")
plateau.placer_mot("ALLUMER")
plateau.placer_mot("RAT")

print(*plateau.plateau,sep="\n")