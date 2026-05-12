from flask import Flask
from db import engine, Base
import model

app = Flask(__name__)

# Create database tables for all registered models.
Base.metadata.create_all(bind=engine)

@app.route("/")
def home():
    return "hello app"

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)
