
from .start import start_command

def setup_handlers(app):
    app.add_handler(start_command)
