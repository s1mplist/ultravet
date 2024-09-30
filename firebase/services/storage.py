from firebase_admin import storage

def upload_file(file_path, destination_path):
    try:
        bucket = storage.bucket()
        blob = bucket.blob(destination_path)
        blob.upload_from_filename(file_path)
    except Exception as e:
        print(f"Erro ao fazer upload do arquivo: {e}")
        raise