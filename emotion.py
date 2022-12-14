"""
                    ____
                  ;`    `'-._
                 / \        /\
               /`   \      |  ;
              /      \     |  |
             /        `\   |  |
            /           \_ /  |
           ;            / `\  |
          ,|_  __       \__/  |
          _\_o/_(             |_
         /`"=/\==""=="=="=="=="`\
         |   )/                 |
         \                      /
         /';=""==""==""==""==";`\
         |  /`   /~\  /~\   `\  |
         |  \  _ \o/  \o/ _  /  |
         \  ; (_)   __   (_) ;  /
         /  |\_.-""(__)""-._/|  \
        |   \       /\       /   |
       /     '.___.'__'.___.'     \
      |             \/             |
      |                            |
      \                            /
      |                            |
       \                          /
        '.                      .'
          '-.__            __.-'
               '---'--'---'


                                                                            Ce programme permet de faire l'analyse d'émotions d'un fichier texte
                                                                            On vient également créer un fichier texte pour chaque prise de parole
                                                                            on enregistre également les valeurs des émitoins, pour voir celles qui prédominent.  
"""



from speech_recognition import Recognizer, Microphone
import speech_recognition as sr
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

r = sr.Recognizer()
Moyenne_A = [] #On va ici stocker chacune des valeurs des émotions du locuteur A enfin d'en faire la moyenne
Moyenne_B = [] #On va ici stocker chacune des valeurs des émotions du locuteur B enfin d'en faire la moyenne

# Locuteur A

for i in range (1,6):
    harvard = sr.AudioFile('A/'+'output'+str(i)+'A.wav')
    with harvard as source:
      audio = r.record(source)
    
    try:    
            text = r.recognize_google(
                    audio, 
                    language="fr-FR"
                )
                
            with open("A\TextA\data"+str(i)+"txt", "w") as txtfile:
                print("{}".format(text), file=txtfile)  

            #print("Le texte a été bien enregistré dans le fichier data.txt")
    except Exception as ex:
            print(ex)

        #Partie emotion

    with open("A\TextA\data"+str(i)+"txt") as d:
            lines = d.read() ##Assume the sample file has 3 lines
            first = lines.split('\n', 1)[0]

    #a= print("vous dites:{}".format(first))

    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

    blob1 = tb(u"{}".format(first))
    phrase = blob1.sentiment
    emotion = phrase[0]
    #print(emotion)
    """if emotion > 0:
            print("La phrase indiqué est une phrase joyeuse")
    elif emotion < 0:
            print("La phrase indiqué est une phrase triste")
    else:
            print("La phrase indiqué est une phrase sans emotion")"""
    Moyenne_A.append(emotion)



#Locuteur_B 
for i in range (1,6):
    harvard = sr.AudioFile('B/'+'output'+str(i)+'B.wav')
#harvard = sr.AudioFile('A\output7outputA.wav')
    with harvard as source:
        audio = r.record(source)

    try:
        
        text = r.recognize_google(
                audio, 
                language="fr-FR"
            )
            
        with open("B/TextB/data"+str(i)+"txt", "w") as txtfile:
            print("{}".format(text), file=txtfile)  

        #print("Le texte a été bien enregistré dans le fichier data.txt")
    except Exception as ex:
        print(ex)

    #Partie emotion

    with open("B/TextB/data"+str(i)+"txt") as d:
        linesB = d.read() ##Assume the sample file has 3 lines
        firstB = linesB.split('\n', 1)[0]

    #b= print("vous dites:{}".format(first))

    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

    blob2 = tb(u"{}".format(first))
    phraseB = blob2.sentiment
    emotionB = phrase[0]
    #print(emotionB)
    """if emotionB > 0:
        print("La phrase indiqué est une phrase joyeuse")
    elif emotionB < 0:
        print("La phrase indiqué est une phrase triste")
    else:
        print("La phrase indiqué est une phrase sans emotion")"""
    Moyenne_B.append(emotionB)

#print(Moyenne_A)
#print(Moyenne_B)

moyenne = sum(Moyenne_A)/len(Moyenne_A)
moyenneB = sum(Moyenne_B)/len(Moyenne_B)

print("Concernant A : ")
if moyenne > 0:
        print("La Moyenne des émotions est de "+ str(moyenne) +" c'est donc une prise de parole majoritairement joyeuse")
elif moyenne < 0:
        print("La Moyenne des émotions est de "+ str(moyenne) +" c'est donc une prise de parole majoritairement triste")
else:
        print("La Moyenne des émotions est de "+ str(moyenne) +" c'est donc une prise de parole majoritairement sans emotion")

print("Concernant B : ")
if moyenneB > 0:
        print("La Moyenne des émotions est de "+ str(moyenneB) +" c'est donc une prise de parole majoritairement joyeuse")
elif moyenneB < 0:
        print("La Moyenne des émotions est de "+ str(moyenneB) +" c'est donc une prise de parole majoritairement triste")
else:
        print("La Moyenne des émotions est de "+ str(moyenneB) +" c'est donc une prise de parole majoritairement sans emotion")

