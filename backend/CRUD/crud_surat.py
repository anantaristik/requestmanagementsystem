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
# CRUD Functions Surat
# --------------------------

def create(id_pemohon, judul, nama_kegiatan, id_feedback, deskripsi, tipe_surat, link, insidental):
    try:
        id_permohonan_sr = "sr-" + nama_kegiatan.replace(" ", "-").lower()
        data = {
            'idPermintaan': id_permohonan_sr,
            'nama_kegiatan': nama_kegiatan,
            'judul': judul,
            'deskripsi': deskripsi,
            'idPemohon': id_pemohon,
            'idFeedback': id_feedback,
            'jenis_surat': tipe_surat,
            'link_docs': link,
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

def reimbursement_read(id_permohonan_rb):
    data = db.collection('InformasiPermohonan').document('surat')
    data.collection('PermohonanSurat').document(id_permohonan_rb).get().to_dict()
    print(data)
    return data

def surat_read_all(tahap):
    try:
        data_dict = []
        if tahap == 'semua':
            datas = db.collection('InformasiPermohonan').document('surat')
            data.collection('PermohonanSurat').where('tahapan', '!=', 3).get()
        else:
            datas = db.collection('InformasiPermohonan').document('surat')
            data.collection('PermohonanSurat').where('tahapan', '==', int(tahap)).get()
        for data in datas:
            data_dict.append(data.to_dict())
        return data_dict
    except:
        data_dict = []
    return data_dict

def reimbursement_read_all_line():
    try:
        data_dict = []
        datas = db.collection('InformasiPermohonan').document('surat')
        data.collection('PermohonanSurat').order_by('waktu_pengajuan').limit(10).get()
        for data in datas:
            data_dict.append(data.to_dict())
        return data_dict
    except:
        data_dict = []
    return data_dict
