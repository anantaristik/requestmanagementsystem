# from backend.misc import firebase_init
# fauth = firebase_init
#
#
# def dashboard_pengurus(request, category, sort):
#     try:
# 		if (request.session['uid']):
# 			user_session = fauth.get_account_info(request.session['uid'])
# 			if (user_session):
# 				user = user_read(user_session['users'][0]['localId'])
# 				print(user['id'])
# 				data = []
# 				tahapan = []
# 				judul = "Home Dashboard"
# 				if user["admin"]:
# 					if category == 'dana' and 'dana' in user['admin']:
# 						data = kr_read_all(sort)
# 						judul = "Dana"
# 						tahapan = tahap_dana
# 					elif category == "surat" and 'surat' in user['admin']:
# 						data = sk_read_all(sort)
# 						judul = "Surat Menyurat"
# 						tahapan = tahap_surat
# 					elif category == "publikasi" and 'publikasi' in user['admin']:
# 						data = sb_read_all(sort)
# 						judul = "Publikasi"
# 						tahapan = tahap_publikasi
# 					hostname = request.build_absolute_uri("/")
# 					print(request.get_full_path)
#
# 					def extract_time(json):
# 						try:
# 							# Also convert to int since update_time will be string.  When comparing
# 							# strings, "10" is smaller than "2".
# 							return json['waktu_pengajuan']
# 						except KeyError:
# 							return 0
#
# 					# lines.sort() is more efficient than lines = lines.sorted()
# 					data.sort(key=extract_time, reverse=False)
#
# 					return render(request, 'dashboard_pengurus.html', {
# 						'datas': data,
# 						'user': user,
# 						'judul': judul,
# 						'hostname': hostname,
# 						'category': category,
# 						'tahapan': tahapan,
# 					})
# 				else:
# 					raise Http404
# 			else:
# 				return redirect("/user/logout")
# 	except:
# 		return redirect("/user/signin")