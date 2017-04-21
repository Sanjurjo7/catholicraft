import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'BlueHarvestMoon'

MOJANG_API = [{'name': 'Mojang', 'url': 'https://api.mojang.com/users/profiles/minecraft/'}]

