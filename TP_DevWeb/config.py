#>>>import random, string, os
#>>>"".join([random.choice(string.printable) for _ in os.urandom(24) ] )
SECRET_KEY = "2lzUl{$*D6#`8uXqlU."
ABOUT = "Rien"
CONTACT = "Contactez-moi! Non je rigole, pas envie de recevoir des mails"
BOOTSTRAP_SERVE_LOCAL = True

import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'monApp.db')