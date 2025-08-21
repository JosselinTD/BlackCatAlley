#!/bin/bash

# Script pour lancer un serveur local et créer un tunnel HTTPS public

# Lancer le serveur python sur le port 3001 en arrière-plan
echo "Lancement du serveur HTTP sur le port 3001..."
python -m http.server 3001 &

# Récupérer le PID (Process ID) du serveur lancé
SERVER_PID=$!

# Laisser un court instant au serveur pour démarrer
sleep 2

echo "Serveur démarré avec le PID: $SERVER_PID"
echo "Création du tunnel sécurisé... Attendez l'URL publique ci-dessous."
echo "-----------------------------------------------------------------"

# Lancer le tunnel avec localhost.run. La commande restera active.
# Elle affichera une URL https://*.lhr.life que vous devrez utiliser.
ssh -R 80:localhost:3001 localhost.run

# Le script attend ici jusqu'à ce que l'utilisateur arrête la commande ssh (Ctrl+C)

echo "-----------------------------------------------------------------"
echo "Tunnel fermé. Arrêt du serveur Python (PID: $SERVER_PID)..."
kill $SERVER_PID
echo "Serveur arrêté. Script terminé."
