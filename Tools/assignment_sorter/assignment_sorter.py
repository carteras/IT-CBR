from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
creds = flow.run_local_server(port=8080)
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.