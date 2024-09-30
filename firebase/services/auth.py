from firebase_admin import auth

def create_user(email, password):
    try:
        return auth.create_user(
            email=email,
            password=password
        )
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        raise

def sign_in_with_email_and_password(email, password):
    try:
        return auth.sign_in_with_email_and_password(email, password)
    except Exception as e:
        print(f"Erro ao fazer login: {e}")
        raise