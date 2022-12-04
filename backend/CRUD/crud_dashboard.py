import firebase_admin
from firebase_admin import credentials, firestore, storage

# --------------------------
# Initialize Firebase Admin
# --------------------------
if not firebase_admin._apps:
    cred = credentials.Certificate("testing-key.json")
    firebase_admin.initialize_app(cred, {
        'storageBucket' : 'sit-bemui.appspot.com'
    })

fauth = firebase_init
db = firestore.client()
ds = storage.bucket()


# --------------------------
# CRUD Functions Dashboard
# --------------------------
def read_requests(idBirdep):
    data_dict = {
        'kr': crud_kr.kr_read_requests(idBirdep),
        'ka': crud_ka.ka_read_requests(idBirdep),
        'ks': crud_ks.ks_read_requests(idBirdep),
        'sk': crud_sk.sk_read_requests(idBirdep),
        'sb': crud_sb.sb_read_requests(idBirdep),
    }
    return data_dict