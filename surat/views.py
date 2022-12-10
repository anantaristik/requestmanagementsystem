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
    try:
        if (request.session['uid']):
            if (fauth.get_account_info(request.session['uid'])):
                return render(request, 'form_surat.html')
            else:
                return redirect("/user/logout")
    except:
        return redirect("/user/login")

def postFormSurat(request):
    judul = request.POST.get("judul")
    nama_kegiatan = request.POST.get("nama_kegiatan")
    deskripsi = request.POST.get("deskripsi")
    jenis_surat = request.POST.get("jenis")
    link = request.POST.get("linkdocs")
    insidental = request.POST.get("insidental")

    message = surat_create(request, judul, nama_kegiatan, deskripsi, jenis_surat, link, insidental)
    print(message)
    if message != "terjadi error":
        return redirect("/surat/detail/" + message)
    else:
        return redirect("/user/logout")


# ---------------------
# Detail Surat Keluar
# --------------------
def detail(request, id):
    try:
        print("masuk")
        if (request.session['uid']):
            print("masuk1")
            user_session = fauth.get_account_info(request.session['uid'])
            if (user_session):
                print("masuk2")
                data_detail = surat_read(id)
                user = user_read(user_session['users'][0]['localId'])
                if (data_detail != []):
                    print("masuk3")
                    if (user["id"] == data_detail["id_pemohon"] or "surat" in user["admin"]):
                        print("masuk4")
                        # Get Dokumen Files
                        if ("surat" in user["admin"]):
                            print("masuk5")
                            admin = "true"
                        else:
                            admin = "false"
                        print("mssuk6")
                        return render(request, 'surat_details.html', {
                            'data': data_detail,
                            'user': user,
                            'admin': admin,
                            'id': id,
                        })
                    else:
                        raise Http404
            else:
                return redirect("/user/logout")
        else:
            return redirect("/user/login")
    except:
        return redirect("/user/login")


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
                    return redirect('home:surat')
            else:
                return redirect('user:logout')
    except:
        return redirect('user:signin')