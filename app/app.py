from flask import Flask
from config import Configuration
from posts.about import posts


app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(posts, url_prefix='/blog')