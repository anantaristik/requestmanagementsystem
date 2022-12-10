import firebase_admin
from firebase_admin import credentials, firestore, storage
from backend.misc import firebase_init
from .crud_user import user_read
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
# CRUD Functions Publikasi
# --------------------------

# --------------------------
# Create
# --------------------------

def publikasi_create(request, judul_konten, id_feedback, deskripsi_kegiatan, kanal_publikasi, link, insidental):
    try:
        print(request.session['uid'])
        user_data = fauth.get_account_info(request.session['uid'])

        uname = user_data['users'][0]['localId']
        user_data = user_read(uname)['id']

        id_pemohon = user_data

        id_permohonan_pb = "pb-" + judul_konten.replace(" ", "-").lower()
        data = {
            'idPermintaan': id_permohonan_pb,
            'judul_konten': judul_konten,
            'deskripsi': deskripsi_kegiatan,
            'idPemohon': id_pemohon,
            'idFeedback': id_feedback,
            'kanal_publikasi': kanal_publikasi,
            'tautan_konten': link,
            'waktu_pengajuan': datetime.datetime.now(pytz.timezone('Asia/Jakarta')),
            'waktu_pengajuan_str': datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('Asia/Jakarta')),
                                                              "%d %b %Y, %H:%M"),
            'isInsidental': insidental,
        }
        collections = db.collection('InformasiPermohonan').document('publikasi')

        collections.collection('permohonanPublikasi').document(id_permohonan_pb).set(data)
        
        return id_permohonan_pb

    except:
        return "terjadi error"

# --------------------------
# Read
# --------------------------

def publikasi_read(id_permohonan_rb):
    data = db.collection('InformasiPermohonan').document('publikasi')
    data = data.collection('permohonanPublikasi').document(id_permohonan_rb).get().to_dict()
    print(data)
    return data

def publikasi_read_all():
    try:
        data_dict = []
        datas = db.collection('InformasiPermohonan').document('publikasi')
        datas = datas.collection('permohonanPublikasi').get()
        for data in datas:
            data_dict.append(data.to_dict())
        return data_dict
    except:
        data_dict = []
    return data_dict

def publikasi_read_requests(idPemohon):
    try:
        data_dict = []
        datas = db.collection('InformasiPermohonan').document('publikasi')
        datas = datas.collection('permohonanPublikasi').where('idPemohon', '==', idPemohon).get()
        for data in datas:
            data_dict.append(data.to_dict())
        return data_dict
    except:
        data_dict = []
    return data_dict

# --------------------------
# Update
# --------------------------
def publikasi_update(id_permohonan_rb, nama_kegiatan, deskripsi_kegiatan, jumlah_dana, insidental):
    try:
        data = db.collection('InformasiPermohonan').document('publikasi')
        data.collection('permohonanPublikasi').document(id_permohonan_rb).update({
            'nama_kegiatan': nama_kegiatan,
            'deskripsi_kegiatan': deskripsi_kegiatan,
            'jumlah_dana': jumlah_dana,
            'insidental': insidental,
    })
        return ""
    except:
        return "error"

# --------------------------
# Delete
# --------------------------
def publikasi_delete(id_permohonan_rb):
    try:
        data = db.collection('InformasiPermohonan').document('publikasi')
        data.collection('permohonanPublikasi').document(id_permohonan_rb).delete()
        return data
    except:
        return

