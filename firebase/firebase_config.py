import firebase_admin
from firebase_admin import credentials

def initialize_app(credentials_path):
    try:
        cred = credentials.Certificate(credentials_path)
        firebase_admin.initialize_app(cred)
    except ValueError as e:
        print(f"Erro ao inicializar o Firebase: {e}")
        raise