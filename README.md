# Black Cat Alley (Titre Provisoire)

## Concept du Jeu

Un jeu d'horreur/puzzle en WebXR pour le concours js13k sur le thème "chat noir".

## Objectif

Le joueur doit s'échapper d'un labyrinthe de ruelles sombres et inquiétantes tout en évitant des chats de gouttière hostiles.

## Style Visuel

*   **Palette de couleurs :** Strictement noir et blanc.
*   **Environnement :** Le monde du jeu est rendu en silhouettes de lignes blanches sur un fond entièrement noir, créant une atmosphère de ruelles urbaines angoissantes.
*   **Les Chats :** Les chats sont également représentés par des silhouettes en lignes blanches. Leurs yeux sont deux points blancs scintillants, les rendant visibles dans l'obscurité.

## Mécaniques de Jeu

*   **Navigation :** Le joueur se déplace dans le labyrinthe pour trouver la sortie.
*   **Lampe de Poche :**
    *   Le joueur dispose d'une lampe de poche pour se défendre.
    *   Lorsqu'elle est allumée, elle projette un large cône de lumière blanche.
    *   La lumière de la lampe de poche fait fuir les chats.
*   **Gestion des Ressources :** La batterie de la lampe de poche est limitée, obligeant le joueur à l'utiliser avec parcimonie.

## Conditions

*   **Victoire :** Trouver la sortie du labyrinthe.
*   **Défaite :** Se faire attraper par un chat.

## Regles

*   Le jeu doit être un jeu WebXR utilisant A-Frame, Babylon.js, Three.js ou PlayCanvas.
*   La taille totale du jeu, une fois compressé en zip, ne doit pas dépasser 13 Ko.
*   Une des bibliothèques WebXR autorisées (A-Frame, Babylon.js, Three.js, ou PlayCanvas) peut être utilisée sans que sa taille ne soit comptée dans la limite des 13 Ko.
*   Il est obligatoire d'utiliser la version spécifique de la bibliothèque fournie par le concours via un lien externe et de ne pas l'inclure dans le fichier zip.

## Tests locaux

* openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
* npm i -g http-server
* http-server -S -C cert.pem -o
