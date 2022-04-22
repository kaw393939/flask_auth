import logging
import os

from flask import Blueprint, cli
from flask_sqlalchemy import SQLAlchemy

from app import config

db = SQLAlchemy()

database = Blueprint('database', __name__,)

@database.cli.command('create')
def init_db():
    db.create_all()

@database.before_app_first_request
def create_db_file_if_does_not_exist():
    root = config.Config.BASE_DIR
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root,'..',config.Config.DB_DIR)
    # make a directory if it doesn't exist
    if not os.path.exists(dbdir):
        os.mkdir(dbdir)
    db.create_all()

@database.before_app_first_request
def create_upload_folder():
    root = config.Config.BASE_DIR
    # set the name of the apps log folder to logs
    uploadfolder = os.path.join(root,'..',config.Config.UPLOAD_FOLDER)
    # make a directory if it doesn't exist
    if not os.path.exists(uploadfolder):
        os.mkdir(uploadfolder)
    db.create_all()