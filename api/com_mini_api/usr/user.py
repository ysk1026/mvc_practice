from sqlalchemy import func
import pandas as pd
import json
from com_mini_api.ext.db import db, openSession

class UserDto(db.Model):

    __tablename__ = 'users'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    
    usr_id: str = db.Column(db.Integer, primary_key=True)
    