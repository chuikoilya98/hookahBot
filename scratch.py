import os.path as pt
import json
from datetime import datetime, timedelta
from db.configuredb import DataBase

userId = '331392389'
userInfo = DataBase.getLastActionByUser(userId)

