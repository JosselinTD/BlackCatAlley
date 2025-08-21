import http.server
import ssl
import os

# Change directory to the script's location to serve files from there
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir:
    os.chdir(script_dir)

# Server settings
server_address = ('0.0.0.0', 3001) # Listen on all network interfaces
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Create a modern SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# Load the certificate and key
try:
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
except FileNotFoundError:
    print("Erreur : Les fichiers 'cert.pem' et/ou 'key.pem' sont introuvables.")
    print("Veuillez les générer avant de lancer le serveur.")
    exit(1)

# Wrap the server socket with the SSL context
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serveur HTTPS lancé.")
print("Ouvrez https://<votre-ip-locale>:3001 dans le navigateur de votre casque VR.")
print("Utilisez Ctrl+C pour arrêter le serveur.")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServeur arrêté.")
    httpd.server_close()