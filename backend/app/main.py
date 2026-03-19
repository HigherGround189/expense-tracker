import logging 
from flask import redirect, url_for, session, send_from_directory
from app_setup import app, oauth, logout_base
from logging_setup import logging_setup

logging_setup()
logger = logging.getLogger(__name__)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Login page
@app.route("/login", methods=["POST"])
def login():
    redirect_uri = url_for("auth", _external=True)
    print("Before redirect, session contains:", dict(session))
    return oauth.keycloak.authorize_redirect(redirect_uri)

# Auth callback
@app.route("/auth")
def auth():
    print("At callback, session contains:", dict(session))
    token = oauth.keycloak.authorize_access_token()
    session["id_token"] = token["id_token"]
    session["user"] = oauth.keycloak.userinfo(token=token)
    return redirect("/")

# Logout
@app.route("/logout", methods=["POST"])
def logout():
    id_token = session.pop("id_token", None)
    session.pop("user", None)

    post_logout_redirect_uri = url_for("index", _external=True)

    url = (
        f"{logout_base}"
        f"?post_logout_redirect_uri={post_logout_redirect_uri}"
        f"&id_token_hint={id_token}"
    )
    return redirect(url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)