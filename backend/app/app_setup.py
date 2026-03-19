import os
from flask import Flask
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

oauth = OAuth(app)
oauth.register(
    name="keycloak",
    client_id=os.getenv("KEYCLOAK_CLIENT_ID"),
    client_secret=os.getenv("KEYCLOAK_CLIENT_SECRET"),
    server_metadata_url=os.getenv("KEYCLOAK_SERVER_METADATA_URL"),
    client_kwargs={"scope": "openid profile email"},    
)

logout_base = os.getenv("KEYCLOAK_LOGOUT_URL")