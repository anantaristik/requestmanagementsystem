from backend.misc import firebase_init
fauth = firebase_init

from django.http import Http404
from django.shortcuts import render, redirect

from backend.CRUD.crud_publikasi import publikasi_read_requests
from backend.CRUD.crud_surat import surat_read_requests
from backend.CRUD.crud_keuangan import reimbursement_read_requests


from backend.CRUD.crud_user import user_read

def dashboard(request, category):
	try:
		user_session = fauth.get_account_info(request.session['uid'])
		if user_session:
			user = user_read(user_session['users'][0]['localId'])
			print(1)
			print(user['id'])
			print(1)
			data = []
			tahapan = []
			judul = "Home Dashboard"
			if user["admin"]:
				if category == 'publikasi' and 'publikasi' in user['admin']:
					data = publikasi_read_requests(user['id'])
					judul = "Publikasi"
				elif category == "surat" and 'surat' in user['admin']:
					data = surat_read_requests(user['id'])
					judul = "Surat Menyurat"
				elif category == "keuangan" and 'keuangan' in user['admin']:
					data = reimbursement_read_requests(user['id'])
					judul = "Keuangan"
				hostname = request.build_absolute_uri("/")
				print(request.get_full_path)
				#
				# def extract_time(json):
				# 	try:
				# 		return json['waktu_pengajuan']
				# 	except KeyError:
				# 		return 0

				# data.sort(key=extract_time, reverse=False)

				return render(request, 'dashboard.html', {
					'datas': data,
					'user': user,
					'judul': judul,
					'hostname': hostname,
					'category': category,
					'tahapan': tahapan,
				})
			else:
				raise Http404
		else:
			redirect("/user/logout")
	except:
		return redirect("/user/login")