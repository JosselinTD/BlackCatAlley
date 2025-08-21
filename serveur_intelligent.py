
import http.server
import socketserver
import subprocess
import time
import re
import atexit
import os

# --- Configuration ---
LOCAL_PORT = 3001
TUNNEL_DOMAIN = "localhost.run"

# --- Gestionnaires de nettoyage ---
tunnel_process = None
log_file = None

def cleanup():
    print("\n--- Arrêt des processus en arrière-plan ---")
    if tunnel_process:
        tunnel_process.terminate()
    if log_file and not log_file.closed:
        log_file.close()
    print("Nettoyage terminé.")

atexit.register(cleanup)

# --- 1. Démarrer le tunnel ---
print(f"Démarrage du tunnel via {TUNNEL_DOMAIN}...")
log_file = open("tunnel.log", "w")
command = ["ssh", "-R", f"80:localhost:{LOCAL_PORT}", TUNNEL_DOMAIN]
tunnel_process = subprocess.Popen(command, stdout=log_file, stderr=subprocess.STDOUT, preexec_fn=os.setsid)

# --- 2. Trouver l'URL du tunnel ---
print("Attente de l'URL du tunnel...")
tunnel_url = None
for _ in range(15):  # Essayer pendant 15 secondes
    time.sleep(1)
    with open("tunnel.log", "r") as f:
        log_content = f.read()
    
    match = re.search(r'(https://[a-zA-Z0-9-]*\.lhr.life)', log_content)
    if match:
        tunnel_url = match.group(1)
        print(f"URL du tunnel trouvée: {tunnel_url}")
        break

if not tunnel_url:
    print("Impossible de trouver l'URL du tunnel. Voici le log :")
    with open("tunnel.log", "r") as f:
        print(f.read())
    exit(1)

# --- 3. Serveur HTTP personnalisé ---
class RedirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/redirect-to-tunnel':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            redirect_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Redirecting...</title>
                <meta http-equiv="refresh" content="0; url={tunnel_url}/prototype-vr.html">
                <style>body{{font-family:monospace; background:black; color:white; text-align:center; padding-top: 20%;}}</style>
            </head>
            <body>
                <h1>Redirection en cours...</h1>
                <p>vers <a href="{tunnel_url}/prototype-vr.html">{tunnel_url}/prototype-vr.html</a></p>
                <script>window.location.href = "{tunnel_url}/prototype-vr.html";</script>
            </body>
            </html>
            """
            self.wfile.write(redirect_html.encode('utf-8'))
        else:
            # Pour toutes les autres requêtes, servir les fichiers normalement
            super().do_GET()

# --- 4. Démarrer le serveur ---
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", LOCAL_PORT), RedirectHandler) as httpd:
    print("\n" + "="*50)
    print("SERVEUR PRÊT")
    print(f"Dans votre casque, allez sur : http://192.0.0.2:{LOCAL_PORT}/redirect-to-tunnel")
    print(f"(L'URL publique directe est: {tunnel_url}/prototype-vr.html)")
    print("="*50 + "\n")
    print("Utilisez Ctrl+C pour tout arrêter.")
    httpd.serve_forever()
