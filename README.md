# DETECTION DE SENTIMENTS
![Alt Text](https://media1.giphy.com/media/xTiN0CNHgoRf1Ha7CM/200w.gif)



Ce projet est un projet réalisé dans le cadre d'un MESPI (Mise en Situation pour des Projet Innovant), l'objectif est de mettre en place une intelligence artificiel afin de faire de la détection d'émotions lors d'une conversation entre plusieurs locuteurs.

## Langages utilisés ?

+ Python


## Fonctionnement ?

### 1. Speaker Diarization
Dans un premier temps, nous utilisons la technologie speaker Diarization afin de faire la détection de deux locuteurs différents en utilisant :

- Le fabuleux Resemblyzer
- Google Collab, en effet cette technologie est plutôt gourmande en ressource
- SpectralClusterer
- ffmpeg


https://colab.research.google.com/drive/16HaPT2M485bEhJvhmG1CoiMpo9Etnc1Y?usp=sharing

### 2. Séquencement de l'audio
Une fois que nous connaissons le temps de parole de chacun des locuteurs, nous séquençons l'audio original en plusieurs fichier audio que nous pour analyser de manière indépendante à l'aide du fichier :

Trime_audio.py

### 3. Analyse d'émotions

Dès lors que nous utilisons l'algorithme permettant de transformer les fichiers audios en fichier texte, nous utilisons la bibliothèque TextBlob afin de faire de l'analyse d'émotions et en faire ressortir l'émotions qui prédomine.

Fichier : emotions.py

Finalement une moyenne est faite pour la prise de parole des différents locuteurs afin de savoir l'émotion qui prédomine, on à également à pourcentage de chacune des émotions dans la prise de parole de chaque locuteur 

### ScreenShot

![image](https://user-images.githubusercontent.com/82390826/207567749-b29b6bb5-b062-4a17-a849-026b4d725f46.png)

## Prêt à faire le grand saut et à affronter vos vrais émotions ?

![Alt Text](https://1.bp.blogspot.com/-L0og5fQIpwY/Xqmrg20JvQI/AAAAAAAAtgA/28J070tGT1EP4V4WmA3ez08Dbz3bBsT-QCLcBGAsYHQ/s1600/giphy-7.gif)

