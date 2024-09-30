from firebase_admin import db, firestore

def set_data_realtime_db(ref, data):
    try:
        ref.set(data)
    except Exception as e:
        print(f"Erro ao salvar dados no Realtime Database: {e}")
        raise

def set_data_firestore(collection_name, document_id, data):
    try:
        db = firestore.client()
        doc_ref = db.collection(collection_name).document(document_id)
        doc_ref.set(data)
    except Exception as e:
        print(f"Erro ao salvar dados no Cloud Firestore: {e}")
        raise