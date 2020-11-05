
#lien vers mon interpreter que j'ai mis dans l'environement virtuel
#vous pouvez changer le shebang ici ou bien directement le raccourci dans le dossier indiqué

#Bonjour Monsieur, j'ai essayé de faire le programme du pendu

#règles : 
#    -pas de chiffres (joueurs)
#    -pas de majuscules (joueurs)
#    -pas de mots de plus de 15 charactères (pour les devs)
#    -pas de lettres répétés dans le mot (devs)

#init librairies (vérifiez que vous avez tkinter, pygame et python3 (3.8 c'est le mieux))
#normalement il devrait y avoir une histoire d'environnement virtuel comme Venv mais je n'arrive pas a 
#le mettre en place... (rectification j'ai presque réussi je vous expliqsue dans le README)
#Si les deux lignes suivantes sont soulignés c'est que je n'utilise pas toutes les 
#fonctions de la librairie
from random import *
from tkinter import *
import tkinter.font as tkFont
import pygame
from moviepy.editor import *
from time import *
import sys
pygame.mixer.init()

# fenêtre acceuil (Je commance par faire une petite fenètre d'acceuil pour que ce soit propre)
#continueracc c'est une variable qui nous permet de gérer la boucle de l'acceuil
global continueracc
continueracc = True
#on initialise la fenètre
acceuil = Tk()
#ici on spécifie que la fenetre n'aura pas de bordures
acceuil.overrideredirect(1)
#on défini sa géométrie
acceuil.geometry("550x500")
#Sa taille max et min ( pour la rendre non modifiable)
acceuil.minsize(550, 500)
acceuil.maxsize(550, 500)
#son titre
acceuil.title("Maurice le Pendu Acceuil")

#on charge la vidéo e fin
VidéoFin = VideoFileClip("Data/Video/PPFin.mp4") 

#on définit les variables qu'on vas utiliser dans l'acceuil
#j'explique pas tout sinon ça va prendre 500 lignes de commentaires
global X
X = int
global Y
Y = int
global rs1
rs1 = False
global rs2
rs2 = False

#la couleur principale de mes objets
ColorFond = "#505050"
ColorVert = "#57ff29"
ColorRouge = "#ff1111"
ColorOrange ="#ff7025"

#init font (je défini les polices de l'acceuil)
ftacc = tkFont.Font(family="playball", size=20, )
ftacc2 = tkFont.Font(family="playball", size=20, )

#Les 3 fonctions correspondantes aux 3 boutons
def res1():
    global X
    global Y
    global continueracc
    global rs1
    X = 1366
    Y = 768
    rs1 = True
    continueracc = False

def res2():
    global X
    global Y
    global rs2
    global continueracc
    X = 1920
    Y = 1080
    rs2 = True
    continueracc = False

def info():
    Info = Tk()
    Info.focus_set()
    Info.maxsize(410,300)
    Info.minsize(410,300)
    Info.title("Info")
    infC1 = Label(Info,bg="#505050", fg= ColorOrange, font=ftacc2, text="\n \n La barre grise en haut est une zone de saisie \n appuyer sur [Ok] ou pressez [Entrée] pour valider \n Ceci est un jeu de Pendu classique \n Le mot à touver est représenté \n par des tirets en bas \n \n vous pouvez appuyer sur [échape] ou [Quitter] \n pour partir\n bon jeu \n \n \n Directed By Titouan Charrier (Moi)\n \n \n ")
    infC1.grid()

#acceuil init (j'affiche le l'acceuil, je détaille pas l'utilisation d'un canvas ni des boutons )
accFond = Canvas(width=550, height=500)
accFond.create_rectangle(0,0,550,500, fill="#404040")
RB1 = Button(acceuil,width=10,height=1, text="1366 x 768", command=res1, font=ftacc, bg="#505050", fg= ColorOrange)
RB2 = Button(acceuil,width=10,height=1, text="1920 x 1080", command=res2, font=ftacc, bg="#505050", fg= ColorOrange)
RB3 = Button(acceuil,width=20,height=1, text="Info", command=info, font=ftacc, bg="#505050", fg= ColorOrange)
txt = Label(bg="#404040", fg= ColorOrange, font=ftacc, text="Salut ! \n Heureusement que tu es arrivé jusqu'ici. \n Maurice s'est fait kidnapper \n et ils veulent le pendre \n tu dois trouver le mot en tirets \n avant qu'il n'ait une jolie cravate.\n Choisis une résolution pour continuer")

#Et là j'affiche tout ce qu'on à défini avant, méthode : définition et affichage ensuite
#ATTENTION l'ordre d'affichage est défini en fonction de l'ordre d'initialisation et non de l'ordre
#d'affichage codé
accFond.grid(row=0, column=0, rowspan=4, columnspan=2, sticky=W)
txt.grid(row=0, column=0, columnspan=2)
RB1.grid(row=1, column=0)
RB2.grid(row=1, column=1)
RB3.grid(row=2, column=0, columnspan=2)

# acceuil algo 
while continueracc == True:
    acceuil.update()

acceuil.destroy()
# acceuil algo fin

#OK on passe au jeu en lui même

#init fenetre principale (je défini la fenètre principale avec sa géométrie, 
#et je décide qu'elle ne soit pas modifiable)
ecr = Tk()
ecr.attributes("-fullscreen",True)
ecr.geometry("{}x{}".format(X,Y))
ecr.maxsize(X,Y)
ecr.minsize(X,Y)
#titre
ecr.title("Maurice le Pendu")
print("debug 1")
#musique (c'est là qu'on utilise le module pygame, je l'ai pas utilisé pour autre
#chose que la musique parcequ'il est vraiment moins pratique en terme d'affichage
#que le module tkinter...)
# -- Déplacé dans le while principale -- 
#le chemin indiqué est le chemin relatif, donc parfois il faut augmenter ou descendre d'un niveau
hurlement = pygame.mixer.Sound("Data/Sons/Hurlement.wav")
rire = pygame.mixer.Sound("Data/Sons/rire.wav")
app = pygame.mixer.Sound("Data/Sons/applause.wav")
hué = pygame.mixer.Sound("Data/Sons/hué.wav")

#init Canvas (ça va servir à placer mes composants avec la méthode "grid")
G1 = Canvas(width=X//6.83, height=Y//12)
G2 = Canvas(width=X//6.83, height=Y//12)

#init video (bon en fait ça c'est plutot un canvas qui vas etre en arrière plan afin 
#de gérer la taille des colonnes et des lignes...)
V = Canvas(width=X//1.41, height=Y//1.64)
V.create_rectangle(0,0,X//1.41,Y//1.64,fill="white")
V.grid(row=1, column=1, columnspan=15, rowspan=15)
V2 = Canvas(width=0,height=100)
V2.grid(row=15,column=12)
V3 = Canvas(width=0,height=100)
V3.grid(row=0,column=0)

#init fond (j'initialise tous les fond d'écran en figurant le chemin d'accés)
#Oui ça fait beaucoup de lignes mais j'ai pas trouvés de moyens de faire autrement, 
# d'ailleur si vous avez un moyen de définir des variables de manières automatique
# je suis preneur 

#Evidemment on fait tout cela en fonction de la résolution entrée au début

#1366x768
if rs1 == True :
    fond1 = PhotoImage(file="Data/Images/images1/PP1.png")
    image1 = Canvas(ecr, width=1366, height=768)

    fond2 = PhotoImage(file="Data/Images/images1/PP2.png")
    image2 = Canvas(ecr, width=1366, height=768)

    fond3 = PhotoImage(file="Data/Images/images1/PP3.png")
    image3 = Canvas(ecr, width=1366, height=768)

    fond4 = PhotoImage(file="Data/Images/images1/PP4.png")
    image4 = Canvas(ecr, width=1366, height=768)

    fond5 = PhotoImage(file="Data/Images/images1/PP5.png")
    image5 = Canvas(ecr, width=1366, height=768)

    fond6 = PhotoImage(file="Data/Images/images1/PP6.png")
    image6 = Canvas(ecr, width=1366, height=768)

    fond7 = PhotoImage(file="Data/Images/images1/PP7.png")
    image7 = Canvas(ecr, width=1366, height=768)

    fond8 = PhotoImage(file="Data/Images/images1/PP8.png")
    image8 = Canvas(ecr, width=1366, height=768)

    fond9 = PhotoImage(file="Data/Images/images1/PP9.png")
    image9 = Canvas(ecr, width=1366, height=768)

    fond10 = PhotoImage(file="Data/Images/images1/PP10.png")
    image10 = Canvas(ecr, width=1366, height=768)


    #init police (je créé les polices avec des tailles différentes)
    ft = tkFont.Font(family="C059", size=30, )
    ft2 = tkFont.Font(family="playball", size=20, )
    ft3 = tkFont.Font(family="C059", size=15, )
    ft4 = tkFont.Font(family="C059", size=50, )
    ft5 = tkFont.Font(family="C059", size=40, )
#1920x1080
elif rs2 == True :
    fond1 = PhotoImage(file="Data/Images/images2/2PP1.png")
    image1 = Canvas(ecr, width=X, height=Y)

    fond2 = PhotoImage(file="Data/Images/images2/2PP2.png")
    image2 = Canvas(ecr, width=X, height=Y)

    fond3 = PhotoImage(file="Data/Images/images2/2PP3.png")
    image3 = Canvas(ecr, width=X, height=Y)

    fond4 = PhotoImage(file="Data/Images/images2/2PP4.png")
    image4 = Canvas(ecr, width=X, height=Y)

    fond5 = PhotoImage(file="Data/Images/images2/2PP5.png")
    image5 = Canvas(ecr, width=X, height=Y)

    fond6 = PhotoImage(file="Data/Images/images2/2PP6.png")
    image6 = Canvas(ecr, width=X, height=Y)

    fond7 = PhotoImage(file="Data/Images/images2/2PP7.png")
    image7 = Canvas(ecr, width=X, height=Y)

    fond8 = PhotoImage(file="Data/Images/images2/2PP8.png")
    image8 = Canvas(ecr, width=X, height=Y)

    fond9 = PhotoImage(file="Data/Images/images2/2PP9.png")
    image9 = Canvas(ecr, width=X, height=Y)

    fond10 = PhotoImage(file="Data/Images/images2/2PP10.png")
    image10 = Canvas(ecr, width=X, height=Y)

    #init police (je créé les polices avec des tailles différentes)
    ft = tkFont.Font(family="C059", size=40, )
    ft2 = tkFont.Font(family="playball", size=30, )
    ft3 = tkFont.Font(family="C059", size=20, )
    ft4 = tkFont.Font(family="C059", size=55, )
    ft5 = tkFont.Font(family="C059", size=45, )

#je defini le canvas pour pouvoir afficher l'image
FondList = [fond1,fond2,fond3,fond4,fond5,fond6,fond7,fond8,fond9,fond10]
ImageList = [image1,image2,image3,image4,image5,image6,image7,image8,image9,image10]
for à in range(0,10):
    ImageList[à].create_image(0,0,image=FondList[à],anchor=NW)

#init variables (bon la toutes les variables dont je vais me servir... je les aies presques
# toutes défini en global car je vais devoir les modifier dans une fonction
# et si on les laisse en local on a seulement accé en lecture dans les fonctions)
global Quit
Quit = False
global lettre
lettre = str
#la c'est la bibliothèque de mots, dsl si il y a des fautes
#également si vous trouvez un mot qui à 2 fois la même lettre il faut l'enlever
mots = ["morphée","théatre","calme","santé","fleur","fière","flair","racine","pleur","astre","lune","univers","amoché","nyctalope","martiens","voyages","récit","oublier","pages","lire","livre","document","ancolie","tulipe","rosier","numéro","pacte","vampire","loup","djin","sortilège","stéroide","domaine","étrange","bisou","culoté","saint","esprit","songe","sangle","nuage","mésaventure","stupide","héritage","fou","images","silence","bruit","calme","bruyant","beauté","mocheté","mystérieux","lucide",'gentil',"amour","méchant","savoir","imbécile","durée","temps","relié","ouvrage","fermé","ouvert","santé","médecin","courage","lion","courge","légume","légion","romain","liste","course","epsilon","delta","zeta","iota","chaise","médisant","sépulcre","tombe","croix","choix","décimètre","décimer","tuer","vers","mort","sang","boire","cheval","chien","chat","monstre","lit","ombre","ténèbres","hadès"]
global continuer
continuer = True
global perdu
perdu = 0
global etr
etr = str
global ok
ok = False
global gagné
gagné = 0
global mot
mot = str
global char
char = int
global VictoireNbr
VictoireNbr = 0
global DéfaiteNbr
DéfaiteNbr = 0
global Rec 
Rec = False



#ça c'est la barre de saisie de lettre
global Elettre
Elettre = Entry(ecr,font=ft,bg=ColorFond)
#en dessous je défini une liste qui va me permettre de stocker toutes les lettres
# téstés afin qu'on ne perde pas un point si on la remet
listest = []

#les fonctions que je vais attribuer aux boutons (QUitter, OK et Recommencer)
def casser():
    global lettre
    lettre = "a"
    global Quit
    Quit = True
    global Rec
    Rec = True
    ecr.destroy()
#CasserEvent et OkEvent sont faites pour etre commander par un évènement (des touches en l'occurence)
def CasserEvent(event):
    global lettre
    lettre = "a"
    global Quit
    Quit = True
    global Rec
    Rec = True
    pygame.mixer.fadeout(300)
    ecr.destroy()
def OkEvent(event):
    global ok
    ok = True
def OK():
    global ok
    ok = True
def rec():
    global Rec
    Rec = True

# je met une fonction while afin de pouvoir recommancer en fin de partie
while True:
    
    #musique
    pygame.mixer.music.load("Data/Musique/ROE.mp3")
    pygame.mixer.music.play(loops=-1)
    #je choisis un mot dans ma banque
    mot = mots[randint(0,len(mots)-1)]
    #je compte son nombre de charactère
    char = len(mot)
    #ca c'est pour aprés...
    Rec = False

    #afficheurs (c'est l'espace en bas où on vas afficher le mot en suivant)
    A1 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A2 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A3 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A4 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A5 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A6 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A7 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A8 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A9 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A10 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A11 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A12 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A13 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A14 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)
    A15 = Label(text="_", font=ft, fg=ColorOrange, bg=ColorFond)

        
    #init clavier ( le clavier c'est la grille de droite où on as les lettre en vert, rouge et bleu)

    #partie graphique
    cl1 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl2 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl3 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl4 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl5 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl6 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl7 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl8 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl9 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl10 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl11 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl12 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl13 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl14 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl15 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl16 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl17 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl18 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl19 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl20 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl21 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl22 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl23 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl24 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl25 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl26 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl27 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl28 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    cl29 = Canvas(width=X//45.5, height=Y//25.6, bg=ColorFond)
    
    #afficher tous les carrés
    listCarré1=[cl1,cl2,cl3,cl4,cl5,cl6,cl7,cl8,cl9,cl10,cl11,cl12,cl13,cl14]
    listCarré2=[cl15,cl16,cl17,cl18,cl19,cl20,cl21,cl22,cl23,cl24,cl25,cl26,cl27,cl28]
    for à in range(0,14):
        listCarré1[à].grid(row=à+1, column=16)
        listCarré2[à].grid(row=à+1, column=17)

    #partie utile (#on défini les lettres dur le coté droit)
    a = Label(text="a", font=ft3, fg="white", bg=ColorFond)
    b = Label(text="b", font=ft3, fg="white", bg=ColorFond)
    c = Label(text="c", font=ft3, fg="white", bg=ColorFond)
    d = Label(text="d", font=ft3, fg="white", bg=ColorFond)
    e = Label(text="e", font=ft3, fg="white", bg=ColorFond)
    f = Label(text="f", font=ft3, fg="white", bg=ColorFond)
    g = Label(text="g", font=ft3, fg="white", bg=ColorFond)
    h = Label(text="h", font=ft3, fg="white", bg=ColorFond)
    i = Label(text="i", font=ft3, fg="white", bg=ColorFond)
    j = Label(text="j", font=ft3, fg="white", bg=ColorFond)
    k = Label(text="k", font=ft3, fg="white", bg=ColorFond)
    l = Label(text="l", font=ft3, fg="white", bg=ColorFond)
    m = Label(text="m", font=ft3, fg="white", bg=ColorFond)
    n = Label(text="n", font=ft3, fg="white", bg=ColorFond)
    o = Label(text="o", font=ft3, fg="white", bg=ColorFond)
    p = Label(text="p", font=ft3, fg="white", bg=ColorFond)
    q = Label(text="q", font=ft3, fg="white", bg=ColorFond)
    r = Label(text="r", font=ft3, fg="white", bg=ColorFond)
    s = Label(text="s", font=ft3, fg="white", bg=ColorFond)
    t = Label(text="t", font=ft3, fg="white", bg=ColorFond)
    u = Label(text="u", font=ft3, fg="white", bg=ColorFond)
    v = Label(text="v", font=ft3, fg="white", bg=ColorFond)
    w = Label(text="w", font=ft3, fg="white", bg=ColorFond)
    x = Label(text="x", font=ft3, fg="white", bg=ColorFond)
    y = Label(text="y", font=ft3, fg="white", bg=ColorFond)
    z = Label(text="z", font=ft3, fg="white", bg=ColorFond)
    é = Label(text="é", font=ft3, fg="white", bg=ColorFond)
    è = Label(text="è", font=ft3, fg="white", bg=ColorFond)
    #afficher toutes les lettres
    listLettre1 = [a,b,c,d,e,f,g,h,i,j,k,l,m,n]
    listLettre2 = [o,p,q,r,s,t,u,v,w,x,y,z,é,è]
    for à in range(0,14):
        listLettre1[à].grid(row=à+1, column=16)
        listLettre2[à].grid(row=à+1, column=17)

    #On défini le tableau des scores :
    Score = Label(font=ft3,bg=ColorFond,text="Score : ")
    Vict = Label(bg=ColorFond,font=ft3,fg=ColorVert,text="Victoire : {}".format(VictoireNbr))
    Defaite = Label(bg=ColorFond,font=ft3,fg=ColorRouge,text="Défaites : {}".format(DéfaiteNbr))
    Score.grid(row=4,column=0,sticky=W)
    Vict.grid(row=5,column=0,sticky=W)
    Defaite.grid(row=6,column=0,sticky=W)

    #init bouton (je défini mes boutons OK qui récupère le contenu de l'entrée, Quitter et recommancer )
    boutonOk = Button(ecr, text="OK", command=OK, font=ft2, bg=ColorFond,fg=ColorOrange)
    boutonQuit = Button(ecr, text="Quitter", command=casser, font=ft2, bg=ColorFond,fg=ColorOrange)
    boutonRec = Button(ecr, text="Recommencer", command=rec, font=ft2, bg=ColorFond,fg=ColorOrange)


    #print entrée et bouton (j'affiche mes boutons)
    Elettre.grid(column=3, row=0, columnspan = 11)
    Elettre.focus()
    boutonOk.grid(row=0, column=14, sticky=W)
    boutonQuit.grid(row=16, column=16, columnspan=2)
    boutonRec.grid(row=16, column=0, columnspan=1)


    #print afficheurs 
    Listétoile = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15]
    étoile = 1
    while étoile <= char:
        Listétoile[étoile].grid(row=16, column=étoile)
        étoile += 1

    #print Canvas (j'affiche les deux rectangles en hauts a gauche et en bas a droite 
    # afin d'élargir les colonnes de la méthode d'affichage "grid")
    G1.grid(row=0, column=0)
    G2.grid(row=16,column=16, columnspan=2)

    #init Perdu/Gagné (je defini le label de fin de jeu)
    Perd1 = Label(text = "P E R D U", fg="red", font=ft)
    #Perd1 = Canvas(width=X//1.3, height=Y//10)
    #Perd1.create_text(0,1000,text="P E R D U",fill = "red")
    #Perd1.grid(row=7,column=7,columnspan=7)

    # ici je met les boutons quit et OK actifs contrairement à rec 
    # car ils seront désactivé apres et si on recommence ils faut les réactiver)
    boutonOk.config(state=NORMAL)
    Elettre.config(state=NORMAL)
    boutonRec.config(state=DISABLED)
    ecr.bind("<Return>", OkEvent)
    ecr.bind("<Escape>", CasserEvent)


    #je defini la grosse fonction que je vais mettre dans mon while aprés
    def test_lettre():
        global char
        global etr
        global mot
        global gagné
        global perdu
        global continuer
        global lettre
        global ok
        #si on veut tricher :
        print (mot)
        while continuer == True and Quit == False:
                #bon la j'ai mis deux boucles, une si on gagne, une si on perd
                #Et en dessous j'affiche tous les fonds en fonction de l'état de la variable
                #"perdu" qui retourne le nombre d'échec
            while ok == False and Quit == False:
                #j'affiche les fonds en fonction de perdu
                listFond = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10]
                listFond[perdu].grid(row=0, column=0, rowspan=40, columnspan=40, sticky=W)
                #j'actualise
                ecr.update()
                
            if ok == True:
                global etr
                etr = Elettre.get()
                Elettre.delete(0, END)
            #là je met la lettre entrée dans la variable lettre
            lettre = etr
            #ici je regarde si le mot qu'il à entrer est strictement égal au mot initial
            if lettre == mot and lettre not in listest:
                gagné = (char+1)
                continuer = False
            #si il a rentré tout le mot, il gagne sinon si il a rentrer une seule lettre
            elif lettre not in listest:
                if Quit == False and len(lettre) == 1 :
                    # ici on vérifie que la lettre entrée est bien une lettre et pas un autre caractère en
                    # utilisant la table ascii et les caractères propres aux lettre minuscules qui sont
                    # compris entre 97 et 122 (on omet les é et è)
                    if ord(lettre) < 123 and ord(lettre) > 96 or lettre == "é" or lettre == "è":

                        #et que la lettre est dans le mot il gagne
                        if lettre in mot:
                            hurlement.play()
                            N = mot.index(lettre)
                            #j'affiche juste les caractères au bon endroit en fonction de leur place "N" et je ColorFond le
                            #clavier de droite
                            #je récupère l'ID de la lettre
                            nombrex = ord(lettre)
                            #je défini ma liste de lettre à afficher
                            listGreen = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,é,è]
                            #je change le mot en bas (on met N+1 pcq mets Labels commencent par le
                            # 1 alors que la liste par 0)
                            Listétoile[N+1].config(text=lettre, fg=ColorVert)
                            if lettre != "é" and lettre != "è":
                                listGreen[nombrex-97].config(fg=ColorVert)
                            elif lettre == "é":
                                é.config(fg=ColorVert)
                            elif lettre == "è":
                                è.config(fg=ColorVert)

                            #on augmente gagné de 1
                            
                            gagné += 1
                            #on sort de la boucle
                            continuer = False
                            # j'ajoute la lettre à la liste testé
                            listest.append(lettre)
                        #sinon , si la lettre n'est pas dans le mot je ColorFonde le clavier en rouge
                        elif lettre not in mot:
                            rire.play()
                            #je récupère l'ID de la lettre
                            nombrex = ord(lettre)
                            #je ColorFonde le clavier
                            if lettre != "é" and lettre != "è":
                                listGreen = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,é,è]
                                listGreen[nombrex-97].config(fg=ColorRouge)
                            elif lettre == "é":
                                é.config(fg=ColorRouge)
                            elif lettre == "è":
                                è.config(fg=ColorRouge)
                            #et j'augmente peru de 1 (je rapelle c'est les échecs)
                            perdu += 1
                            #j'ajoute la lettre à la liste testé
                            listest.append(lettre)
                            #je sors de la boucle ok
                            ok = False
                            #je sors de la boucle continuer
                            continuer = False

                        #ca c'est au cas ou il y à un bug et que
                        # l'entré retourne un caractère qui à échappé à la vérif...
                        else:
                            ok = False
                    else :
                        #il a entré un caractère invalide (on va etre sympa on lui compte pas)
                        ok = False

                elif Quit == False and len(lettre) == 0:
                    ok = False
                    #si il a laissé le champs d'entré vide et qu'il à appuyé sur OK on ne lui
                    #enlève pas de point
                else:
                    #et là çà veut dire qu'il à tenté un mot mais que ce n'etait pas le bon
                    #on lui affiche rien sur l'écran ça fait trop (et je suis fatigué)
                    perdu +=1
                    ok = False
                    continuer = False
                    if Quit == False:
                        rire.play()
            else :
                #la ca veut dire qu'il a rentré une lettre déja testé donc on revient juste au départ
                ok = False

    #debut (bon ben ça c'est le début réel de l'algorithme)
    while gagné < (char) and perdu < 9 and Quit == False:
        
        #notre fameuse fonction 
        test_lettre()
        #au sortir de la fonction, continuer est False donc on le remet True pour pouvoir relancer la foction
        continuer = True
    #pour qu'on puisse gagner un jour je vérifie que gagné soit inférieur ou égale au nombre de charactère
    #mais en fait ça marche pas... j'ai essayer plusieurs trucs sans succées, du coup la seule manière de réussir 
    #c'est de marquer le mot entier dans la barre.
    if gagné >= (char):
        VictoireNbr+=1
        Vict = Label(bg=ColorFond,font=ft3,fg=ColorVert,text="Victoire : {}".format(VictoireNbr))
        Vict.grid(row=5,column=0,sticky=W)
        app.play()
        while Quit == False and Rec == False:
            #cool on a gagné, on désactive le bouton OK et l'entrée
            boutonOk.config(state=DISABLED)
            Elettre.config(state=DISABLED)
            boutonOk.grid_forget()
            Elettre.grid_forget()

            #on active le bouton recommencer
            boutonRec.config(state=NORMAL)
            #on change le texte a l'intérieur du Label pour annoncer la victoire
            Perd1.config(text="G A G N É \n c'était bien : {}".format(mot),bg=ColorFond, fg=ColorVert, font=ft4)
            #on affiche ça
            Perd1.grid(row=6, column=1, columnspan=14, rowspan=4, sticky=NSEW)
            #on actualise l'écran
            ecr.update()
    elif perdu == 9:
        #hooo on a perdu
        DéfaiteNbr+=1
        Defaite = Label(bg=ColorFond,font=ft3,fg=ColorRouge,text="Défaites : {}".format(DéfaiteNbr))
        Defaite.grid(row=6,column=0,sticky=W)
        #et maintenant la partie graphique/audio
        pygame.mixer.music.fadeout(400)
        #on minimise la fenetre tk sinon elle passe devant celle de pygame
        ecr.state("withdrawn")
        #on affiche la vidéo (avec moviepy)
        VidéoFin.preview(fullscreen=True)
        pygame.display.quit()
        ecr.state("normal")
        while Quit == False and Rec == False:
            #on désactive le bouton OK et l'entrée
            boutonOk.config(state=DISABLED)
            Elettre.config(state=NORMAL)
            boutonOk.grid_forget()
            Elettre.grid_forget()
            #on active le bouton Recommencer
            boutonRec.config(state=NORMAL)
            #On affiche la dernière image de Maurice le Pendu
            image10.grid(row=0, column=0, rowspan=40, columnspan=40, sticky=W)
            #comme avec gagné voila
            Perd1.config(text="P E R D U \n c'etait : {}".format(mot), fg=ColorRouge,bg=ColorFond, font=ft5)
            Perd1.grid(row=12, column=1, columnspan=14, rowspan=4, sticky=NSEW)
            ecr.update()
    #oublier afficheurs (oui on doit tout remettre à zéro pour un éventuel recommancement)
    listFond = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10]
    #ici je delete tous les objets utilisés
    for à in range(0,14):
        Listétoile[à].grid_forget()
    Perd1.grid_forget()
    for à in range(0,10):
        listFond[à].grid_forget()
    #je réinitialise les variables
    perdu = 0
    gagné =0
    lettre = str
    mot = str
    #je vide la liste
    listest = []
    ecr.update

ecr.quit()
#fin (en fait en théorie on arrivera jamais à cette ligne, car la boucle est infinie
# tant que l'application n'est pas détruite par la fonction casser)
