import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
"""@TODO change the database name and password"""
DB_NAME = 'pasquo1'
DB_PASSWORD = 'Liukangs240'


# IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://pasquo_user:mf7vKphODwSEAUSkJKQT3hEDHjeX0fbr@dpg-cfl3rgla49903fj1bh8g-a.oregon-postgres.render.com/pasquo'
# SQLALCHEMY_DATABASE_URI = 'postgres://zdhildnqsmdqpf:dc677944694cc881e333f723cd45907656436264ab1f610d288ca1b8641e9545@ec2-54-163-34-107.compute-1.amazonaws.com:5432/dckdou76bps9ho'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SESSION_COOKIE_DOMAIN = False
