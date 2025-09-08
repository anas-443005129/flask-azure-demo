from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def home():
    return "🎉 Hello from Flask on Azure App Service!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    # Bind to 0.0.0.0 so Azure can reach it
    app.run(host="0.0.0.0", port=port)
