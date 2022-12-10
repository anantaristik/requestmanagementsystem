import json

from django.http import Http404
from django.shortcuts import render, redirect
from backend.CRUD.crud_surat import surat_create, surat_read,surat_delete
from backend.CRUD.crud_user import user_read
from backend.constant.links import links_surat
from backend.constant.tahapan import tahap_surat_keluar
from backend.misc import firebase_init, getPhoto

# Initialize Firebase Database
fauth = firebase_init


# ---------------------
# Form Request Surat Keluar
# --------------------
def formSurat(request):
    return render(request, 'form_surat.html')

def postFormSurat(request):
    judul = request.POST.get("judul")
    nama_kegiatan = request.POST.get("nama_kegiatan")
    deskripsi = request.POST.get("deskripsi")
    jenis_surat = request.POST.get("jenis")
    link = request.POST.get("linkdocs")
    insidental = request.POST.get("insidental")

    if (insidental == "True"):
        insidental = True
        bukti = request.POST.get("bukti")
    else:
        insidental = False
        bukti = ""

    message = surat_create(request, judul, nama_kegiatan, deskripsi, jenis_surat, link, insidental, bukti)
    print(message)
    if message != "terjadi error":
        return redirect("/surat/detail/" + message)
    else:
        return redirect("user:logout")


# ---------------------
# Detail Surat Keluar
# --------------------
def detail(request, id):
    try:
        if (request.session['uid']):
            user_session = fauth.get_account_info(request.session['uid'])
            if (user_session):
                data_detail = surat_read(id)
                user = user_read(user_session['users'][0]['localId'])
                if (data_detail != []):
                    if (user["id"] == data_detail["idPemohon"] or "surat" in user["admin"]):
                        # Get Dokumen Files
                        if ("surat" in user["admin"]):
                            admin = "true"
                        else:
                            admin = "false"
                        try:
                            url = getPhoto.getPhoto(data_detail["token_dokumen"][0])
                            dokumen = url
                        except:
                            dokumen = ""
                        return render(request, 'surat_details.html', {
                            'data': data_detail,
                            'user': user,
                            'admin': admin,
                            'id': id,
                            'dokumen': dokumen,
                            'tahap': tahap_surat_keluar
                        })
                    else:
                        raise Http404
            else:
                return redirect("/user/logout")
        else:
            return redirect("/user/signin")
    except:
        return redirect("/user/signin")


def delete(request):
    try:
        if (request.session['uid']):
            user_session = fauth.get_account_info(request.session['uid'])
            if (user_session):
                user = user_read(user_session['users'][0]['localId'])
                if ("surat" in user["admin"]):
                    print('masuk')
                    id_request = request.POST.get("id_request")
                    print(id_request)
                    data = surat_delete(id_request)
                    print(data)
                    return redirect('../user/dashboard_pengurus/surat/semua')
            else:
                return redirect('user:logout')
    except:
        return redirect('user:signin')