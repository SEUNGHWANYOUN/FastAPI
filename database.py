import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

BASE_DIR= os.path.dirname(os.path.abspath(__file__))
SECRET_FILE= os.path.join(BASE_DIR, 'secrets.json')
secrets = json.load(open(SECRET_FILE).read())
DB = secrets["DB"]

DB_URL = f"mysql+pymsql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

engine = create_engine(
    DB_URL, encoding = 'utf-8'
)

SessionLacal = sesstionmaker(autocomit=False, autoflush=False, bind=engine)

Base= declarative_base()