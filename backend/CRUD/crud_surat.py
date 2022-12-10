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
# CRUD Functions Surat
# --------------------------

# --------------------------
# Create
# --------------------------

def surat_create(request, judul, nama_kegiatan, deskripsi, tipe_surat, link, insidental):
    try:
        print(request.session['uid'])
        user_data = fauth.get_account_info(request.session['uid'])
    
        uname = user_data['users'][0]['localId']
        user_data = user_read(uname)['id']

        id_pemohon = user_data

        id_permohonan_sr = "sr-" + nama_kegiatan.replace(" ", "-").lower()
        data = {
            'id_permintaan': id_permohonan_sr,
            'nama_kegiatan': nama_kegiatan,
            'judul': judul,
            'deskripsi': deskripsi,
            'id_pemohon': id_pemohon,
            'idFeedback': "",
            'jenis_surat': tipe_surat,
            'linkdocs': link,
            'waktu_pengajuan': datetime.datetime.now(pytz.timezone('Asia/Jakarta')),
            'waktu_pengajuan_str': datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('Asia/Jakarta')),
                                                              "%d %b %Y, %H:%M"),
            'isInsidental': insidental,
        }
        collections = db.collection('InformasiPermohonan').document('surat')

        collections.collection('PermohonanSurat').document(id_permohonan_sr).set(data)
    
        return id_permohonan_sr

    except:
        return "terjadi error"

# --------------------------
# Read
# --------------------------

def surat_read(id_permohonan_rb):
    data = db.collection('InformasiPermohonan').document('surat')
    data = data.collection('PermohonanSurat').document(id_permohonan_rb).get().to_dict()
    print(data)
    return data

def surat_read_all():
    try:
        data_dict = []
        datas = db.collection('InformasiPermohonan').document('surat')
        datas = datas.collection('PermohonanSurat').get()
        for data in datas:
            data_dict.append(data.to_dict())
        return data_dict
    except:
        data_dict = []
    return data_dict

def surat_read_requests(idPemohon):
    try:
        data_dict = []
        datas = db.collection('InformasiPermohonan').document('surat')
        datas = datas.collection('PermohonanSurat').where('id_pemohon', '==', idPemohon).get()
        for data in datas:
            data_dict.append(data.to_dict())
        return data_dict
    except:
        data_dict = []
    return data_dict
# --------------------------
# Update
# --------------------------
def surat_update(id_permohonan_rb, nama_kegiatan, deskripsi_kegiatan, jumlah_dana, insidental):
    try:
        data = db.collection('InformasiPermohonan').document('surat')
        data = data.collection('PermohonanSurat').document(id_permohonan_rb).update({
            'nama_kegiatan': nama_kegiatan,
            'deskripsi_kegiatan': deskripsi_kegiatan,
            'insidental': insidental,
    })
        return ""
    except:
        return "error"

# --------------------------
# Delete
# --------------------------
def surat_delete(id_permohonan_rb):
    try:
        data = db.collection('InformasiPermohonan').document('surat')
        data = data.collection('PermohonanSurat').document(id_permohonan_rb).delete()
        return data
    except:
        return