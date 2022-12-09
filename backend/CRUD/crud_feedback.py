import firebase_admin
from firebase_admin import credentials, firestore, storage
# from .crud_user import user_read
from backend.misc import firebase_init

import datetime
import pytz


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
# CRUD Functions
# --------------------------
def fb_create(request, id_permohonan, status, komentar, berkas, id_pengurus, jenis_permohonan):
    try:
        print(request.session['uid'])
        # user_data = fauth.get_account_info(request.session['uid'])
        # id_user = user_data['users'][0]['localId']
        # user_data2 = user_read(idUser)
        # nama_user = user_data2['nama']
        id_feedback = "fb-" + id_permohonan
        data = {
            'id_feedback': id_feedback,
            'id_pengurus': id_pengurus,
            'status': status,
            'komentar': komentar,
            'berkas': berkas,
            'waktu_pengajuan': datetime.datetime.now(pytz.timezone('Asia/Jakarta')),
            'waktu_pengajuan_str': datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('Asia/Jakarta')), "%d %b %Y, %H:%M")
        }
        db.collection('feedback').document(id_feedback).set(data)

        data = db.collection(jenis_permohonan).document(id_permohonan).get().to_dict()
        data['id_feedback'] = id_feedback
        db.collection(jenis_permohonan).document(id_permohonan).set(data)
        return id_feedback
    except:
        return "terjadi error"

def fb_read(id):
    try:
        data = db.collection('feedback').document(id).get().to_dict()
        return data
    except:
        data = []
    return data

def fb_delete(id):
    try:
        data = db.collection('feedback').document(id).delete()
        return data
    except:
        return

# ---------------------
# Update data per-data
# --------------------

def fb_update_status(request, id, status):
    try:
        db.collection('feedback').document(id).update({
            "status": status,
        })
        return ""
    except:
        return "terjadi error"

def fb_update_berkas(request, id, berkas):
    try:
        db.collection('feedback').document(id).update({
            "berkas": berkas,
        })
        return ""
    except:
        return "terjadi error"

def fb_update_komentar(request, id, komentar):
    try:
        data = db.collection('feedback').document(id).get().to_dict()
        data['komentar'] = data['komentar'].append(komentar)
        db.collection('feedback').document(id).set(data)
        return ""
    except:
        return "terjadi error"
