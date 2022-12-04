import firebase_admin
from firebase_admin import credentials, firestore, storage
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
def reimbursement_create(nama_kegiatan, id_permohonan_rb, deskripsi_kegiatan, id_feedback, id_pemohon, jumlah_dana, insidental):
    id_permohonan_rb = "rb-" + nama_kegiatan.replace(" ", "-").lower()

    data = {
        'id_permohonan_rb': id_permohonan_rb,
        'nama_kegiatan': nama_kegiatan,
        'deskripsi_kegiatan': deskripsi_kegiatan,
        'id_feedback': id_feedback,
        'id_pemohon': id_pemohon,
        'jumlah_dana': jumlah_dana,
        'insidental': insidental,
        'waktu_permintaan': datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
    }

    collections = db.collection('InformasiPermohonan').document('keuangan')
    collections.collection('permohonanReimburse').document(id_permohonan_rb).set(data)

    return id_permohonan_rb


# --------------------------
# Read
# --------------------------
def reimbursement_read(id_permohonan_rb):
    data = db.collection('InformasiPermohonan').document('keuangan')
    data.collection('permohonanReimburse').document(id_permohonan_rb).get().to_dict()
    print(data)
    return data

def reimbursement_read_all(tahap):
    try:
        data_dict = []
        if tahap == 'semua':
            datas = db.collection('InformasiPermohonan').document('keuangan')
            data.collection('permohonanReimburse').where('tahapan', '!=', 3).get()
        else:
            datas = db.collection('InformasiPermohonan').document('keuangan')
            data.collection('permohonanReimburse').where('tahapan', '==', int(tahap)).get()
        for data in datas:
            data_dict.append(data.to_dict())
        return data_dict
    except:
        data_dict = []
    return data_dict

def reimbursement_read_all_line():
    try:
        data_dict = []
        datas = db.collection('InformasiPermohonan').document('keuangan')
        data.collection('permohonanReimburse').order_by('waktu_permintaan').limit(10).get()
        for data in datas:
            data_dict.append(data.to_dict())
        return data_dict
    except:
        data_dict = []
    return data_dict