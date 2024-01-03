"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""
import json

import google.generativeai as genai

genai.configure(api_key="GOOGLE-API-KEY")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Ouverture du fichier en mode lecture
with open('FIFA_WorldCup2018Men.json', 'r') as fichier_json:
    # Charger le contenu JSON depuis le fichier
    donnees = json.load(fichier_json)

prompt_parts = [
  "Parle moi du football\n"
  " Le football, également connu sous le nom de soccer dans certains pays, est un sport d'équipe joué entre deux équipes de 11 joueurs. "
  "Il se joue sur un terrain rectangulaire avec un but à chaque extrémité. L'objectif du jeu est de marquer plus de buts que l'adversaire"
  " en frappant le ballon dans le but de l'adversaire.\n\nLe football est un sport très populaire dans le monde entier. Il est joué dans plus de"
  " 200 pays et territoires, et la Coupe du Monde de la FIFA est l'événement sportif le plus regardé au monde.\n"
  "\nLe football est un sport qui nécessite de la vitesse, de l'endurance, de la force et de l'agilité. Il est également important d'avoir de "
  "bonnes compétences techniques, telles que la capacité de dribbler, de passer et de tirer.\n\nLe football est un sport d'équipe, et il est "
  "important que les joueurs travaillent ensemble pour atteindre leur objectif. Il est également important de respecter les adversaires et les "
  "arbitres.\n\nLe football est un sport qui peut être joué par des personnes de tous âges et de tous niveaux. Il est un excellent moyen de "
  "faire de l'exercice, de s'amuser et de se faire des amis.\n\nVoici quelques-uns des plus grands joueurs de football de tous les temps :\n\n*"
  " Pelé\n* Diego Maradona\n* Lionel Messi\n* Cristiano Ronaldo\n* Zinedine Zidane\n\nEt voici quelques-uns des plus grands clubs de football"
  " du monde :\n\n* Real Madrid\n* FC Barcelone\n* Manchester United\n* Bayern Munich\n* Juventus \n \n donne moi chaque numéro de 1 à 11 avec "
  "le post qui lui est habituellement attribué\n 1. Gardien de but : le dernier rempart de la défense, chargé d'empêcher le ballon de pénétrer"
  " dans le but.\n2. Arrière droit : un défenseur latéral chargé de couvrir le flanc droit du terrain et de contribuer aux attaques.\n3. "
  "Défenseur central : un défenseur chargé de protéger le but et de repousser les attaques adverses.\n4. Défenseur central : un autre défenseur "
  "chargé de protéger le but et de repousser les attaques adverses.\n5. Arrière gauche : un défenseur latéral chargé de couvrir le flanc"
  " gauche du terrain et de contribuer aux attaques.\n6. Milieu défensif : un milieu de terrain chargé de protéger la défense et de récupérer "
  "le ballon.\n7. Milieu central : un milieu de terrain chargé de contrôler le jeu et de distribuer le ballon.\n8. Milieu offensif : un milieu "
  "de terrain chargé de créer des occasions de but et de marquer des buts.\n9. Ailier droit : un attaquant chargé de jouer sur le côté droit "
  "du terrain et de créer des occasions de but.\n10. Avant-centre : un attaquant chargé de marquer des buts.\n11. Ailier gauche : un attaquant "
  "chargé de jouer sur le côté gauche du terrain et de créer des occasions de but. \n\n\ntu as inversé les rôles du numèro 9 et du numèro 10 "
  "Vous avez raison, j'ai inversé les rôles du numéro 9 et du numéro 10. Voici la correction :\n\n1. Gardien de but : le dernier rempart de la"
  " défense, chargé d'empêcher le ballon de pénétrer dans le but.\n2. Arrière droit : un défenseur latéral chargé de couvrir le flanc droit"
  " du terrain et de contribuer aux attaques.\n3. Défenseur central : un défenseur chargé de protéger le but et de repousser les attaques"
  " adverses.\n4. Défenseur central : un autre défenseur chargé de protéger le but et de repousser les attaques adverses.\n5. "
  "Arrière gauche : un défenseur latéral chargé de couvrir le flanc gauche du terrain et de contribuer aux attaques.\n6. "
  "Milieu défensif : un milieu de terrain chargé de protéger la défense et de récupérer le ballon.\n7. "
  "Milieu central : un milieu de terrain chargé de contrôler le jeu et de distribuer le ballon.\n8. "
  "Milieu offensif : un milieu de terrain chargé de créer des occasions de but et de marquer des buts.\n9. "
  "Avant-centre : un attaquant chargé de marquer des buts.\n10. "
  "Ailier droit : un attaquant chargé de jouer sur le côté droit du terrain et de créer des occasions de but.\n11. "
  "Ailier gauche : un attaquant chargé de jouer sur le côté gauche du terrain et de créer des occasions de but. "
  "\n\ncite moi 3 joueurs célébres pour chacun des numèros \n**1. "
  "Gardien de but**\n\n* Gianluigi Buffon\n* Iker Casillas\n* Manuel Neuer\n\n**2."
  " Arrière droit**\n\n* Dani Alves\n* Philipp Lahm\n* Cafu\n\n**3. Défenseur central**\n\n* "
  "Sergio Ramos\n* Carles Puyol\n* Paolo Maldini\n\n**4. Défenseur central**\n\n* Gerard Piqué\n* "
  "Fabio Cannavaro\n* Rio Ferdinand\n\n**5. Arrière gauche**\n\n* Roberto Carlos\n* Ashley Cole\n* "
  "David Alaba\n\n**6. Milieu défensif**\n\n* Claude Makelele\n* Sergio Busquets\n* Casemiro\n\n**7."
  " Milieu central**\n\n* Xavi Hernandez\n* Andrea Pirlo\n* Tony Kroos\n\n**8. Milieu offensif**\n\n*"
  " Zinédine Zidane\n* Ronaldinho\n* Andrés Iniesta\n\n**9. Avant-centre**\n\n* Lionel Messi\n* "
  "Cristiano Ronaldo\n* Pelé\n\n**10. Ailier droit**\n\n* David Beckham\n* Mohamed Salah\n* "
  "Arjen Robben\n\n**11. Ailier gauche**\n\n* Neymar\n* Eden Hazard\n* Gareth Bale "
  "\n\ncite moi 20 joueurs qui sont considérés comme les meilleurs de tous les temps"
  " \n\n1. Lionel Messi\n2. Cristiano Ronaldo\n3. Pelé\n4. Diego Maradona\n5. "
  "Zinédine Zidane\n6. Ronaldo Nazário\n7. Johan Cruyff\n8. Ferenc Puskás\n9. "
  "Alfredo Di Stéfano\n10. George Best\n11. Eusébio\n12. Michel Platini\n13. "
  "Marco van Basten\n14. Franz Beckenbauer\n15. Paolo Maldini\n16. Cafu\n17."
  " Roberto Carlos\n18. Xavi Hernández\n19. Andrés Iniesta\n20. Raúl González "
  " \n\ndonne moi les 20 dernioers vainqueurs de la ligue des champions 1. "
  "2021-2022 : Real Madrid\n2. 2020-2021 : Chelsea\n3. 2019-2020 :"
  " Bayern Munich\n4. 2018-2019 : Liverpool\n5. 2017-2018 : "
  "Real Madrid\n6. 2016-2017 : Real Madrid\n7. 2015-2016 : "
  "Real Madrid\n8. 2014-2015 : FC Barcelone\n9. 2013-2014 : "
  "Real Madrid\n10. 2012-2013 : Bayern Munich\n11. 2011-2012 : "
  "Chelsea\n12. 2010-2011 : FC Barcelone\n13. 2009-2010 : "
  "Inter Milan\n14. 2008-2009 : FC Barcelone\n15. 2007-2008 : "
  "Manchester United\n16. 2006-2007 : AC Milan\n17. 2005-2006 : "
  "FC Barcelone\n18. 2004-2005 : Liverpool\n19. 2003-2004 : FC Porto\n20. 2002-2003 : AC Milan \n",
]

response = model.generate_content(prompt_parts)
print(response.text)