import firebase_admin
from firebase_admin import credentials, firestore, storage
from backend.misc import firebase_init

# --------------------------
# Initialize Firebase Admin
# --------------------------
if not firebase_admin._apps:
    cred = credentials.Certificate("testing-key.json")
    firebase_admin.initialize_app(cred, {
        'storageBucket' : 'request-management-syste-62a37.appspot.com'
    })

fauth = firebase_init
db = firestore.client()
ds = storage.bucket()


# --------------------------
# CRUD Functions Dashboard
# --------------------------
