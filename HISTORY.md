# Historique du Développement

Ce document résume les étapes de développement et de débogage du prototype "Black Cat Alley".

### 1. Idée Initiale

L'utilisateur a proposé de créer un jeu WebXR pour le concours js13k sur le thème "chat noir". Le concept est de s'échapper d'un labyrinthe de ruelles sombres en utilisant une lampe de poche pour faire fuir des chats, avec une esthétique purement noire et blanche.

### 2. Création du Prototype et Débogage Initial

- **Prototype v1** : Un premier fichier `prototype.html` a été créé pour générer et afficher un labyrinthe en 3D avec Three.js.
- **Bug #1 : Écran Noir** : Le script ne fonctionnait pas sur l'appareil mobile de l'utilisateur. Le chargement de la bibliothèque Three.js depuis le serveur du concours js13k était en cause.
- **Solution** : Remplacement de l'URL du script par un lien CDN fiable (cdnjs). Le labyrinthe est alors devenu visible.

### 3. Améliorations Visuelles et de Contrôles

- **Bug #2 : Position de la Caméra** : Le joueur apparaissait sous le labyrinthe.
- **Solution** : La méthode de dessin a été modifiée pour générer des couloirs en "fil de fer" 3D complets, ce qui a corrigé la position de la caméra.
- **Ajout des déplacements** : Le mouvement au clavier (ZQSD) et un joystick virtuel pour mobile ont été ajoutés.
- **Correction du bouton VR** : Le bouton "Enter VR" a été corrigé en utilisant le script utilitaire `VRButton.js` officiel de Three.js.

### 4. Débogage des Collisions

- **Bug #3 : Collisions Imprécises** : Le joueur restait bloqué dans les murs ou passait à travers.
- **Solution v1** : Une nouvelle logique de "glisse le long des murs" et de vérification de rayon a été implémentée. Elle s'est avérée trop sensible et bloquait tout mouvement.
- **Bug #4 : Décalage des Coordonnées** : Une fois la sensibilité corrigée, le joueur était décalé d'un demi-cube par rapport aux couloirs.
- **Solution v2** : Le système de coordonnées a été entièrement revu pour aligner la grille du labyrinthe avec l'origine du monde (0,0,0). Cela a résolu tous les problèmes de collision et de positionnement.

### 5. État Actuel

Le prototype est maintenant fonctionnel avec un labyrinthe explorable via clavier et joystick, une détection de collision robuste, et une entrée en mode VR fonctionnelle.

### 6. Amélioration du Style Visuel

- **Mise à jour des règles :** Ajout des règles du concours WebXR au fichier `README.md`.
- **Style des bâtiments :**
    - Remplacement des murs en "fil de fer" par des blocs noirs solides avec des arêtes supérieures blanches pour un meilleur effet de silhouette.
    - Ajout de fenêtres blanches (détails négatifs) générées aléatoirement sur les façades pour augmenter le niveau de détail.
    - Implémentation d'une logique pour éviter la superposition des fenêtres.
- **Style des chats :**
    - Remplacement du cube représentant le chat par une paire d'yeux flottants pour un effet plus inquiétant.
    - Ajout d'un corps invisible pour gérer les collisions entre les chats et les empêcher de se superposer.
    - Implémentation d'un système de "Sprites" pour les yeux afin de garantir qu'ils soient toujours visibles et correctement orientés vers le joueur, corrigeant plusieurs bugs visuels.
    - Après expérimentation avec plusieurs formes, la forme des yeux a été standardisée en deux cercles lumineux pour tous les chats pour plus de cohérence.