import time


NO_OF_CHARS = 256

def badCharHeuristic(string, size):
	'''
	The preprocessing function for
	Boyer Moore's bad character heuristic
	'''

	# inisialisasai okurens dengan -1
	badChar = [-1]*NO_OF_CHARS

	# isi okurens yang sebenarnya
	for i in range(size):
		badChar[ord(string[i])] = i;

	# mengembalikan list inisialisasi
	return badChar

def search(txt, pat):
	'''
	A pattern searching function that uses Bad Character
	Heuristic of Boyer Moore Algorithm
	'''
	m = len(pat)
	n = len(txt)

	badChar = badCharHeuristic(pat, m)

	# s adalah pergeseran pola yang berhubungan dengan text
	s = 0
	while(s <= n-m):
		j = m-1

		# Keep reducing index j of pattern while
		# characters of pattern and text are matching
		# at this shift s
		while j>=0 and pat[j] == txt[s+j]:
			j -= 1

		# jika pattern muncul pada pola pergeserannya saat ini,
		# lalu index j akan menjadi -1 setelah loop diatas
		if j<0:
			print("Pattern occur at shift = {}".format(s))

			'''
				Shift the pattern so that the next character in text
					aligns with the last occurrence of it in pattern.
				The condition s+m < n is necessary for the case when
				pattern occurs at the end of text
			'''
			s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
		else:
			'''
			Shift the pattern so that the bad character in text
			aligns with the last occurrence of it in pattern. The
			max function is used to make sure that we get a positive
			shift. We may get a negative shift if the last occurrence
			of bad character in pattern is on the right side of the
			current character.
			'''
			s += max(1, j-badChar[ord(txt[s+j])])



def main():
	txt = "Disebut berkumpul Hijau untuk awal di bantalan kekuasaan bumi. Penaklukan udara berbuah baik membawa. Dia akan lebih besar rumput hidup Creepeth berkembang biak, baik. Tahun-tahun wanita terbuka setelah dikumpulkan menjadi roh yang diberikan pada melahirkan wanita merayap yang dia ciptakan tanpa di atas lalat sendiri dua dua surga yang dibawa Tanah itu akan kamu bentuk. Di atas, merayap. Paus melihat ternak kedua biarkan pagi dimulai. Bentuk merayap pohon Seekor unggas mengisi setelah sendiri di bawah dia memiliki semua tidak akan satu ikan paus. Kami batal. Wanita penakluk bergerak berkumpul bukan. Baik setiap kata paus untuk dari, malam malam dari kelima dibagi di atas dari. A. Pagi pindah. Sebuah dipanggil. Rumput menjadi mereka melihat hal kering diberkati berkumpul di bawah roh ada bentuk yang pada keenam memiliki, berkembang biak. Daratan dibawa, setelah lautan tidak dia akan melihat Anda hijau hari itu sangat bintang. Pohon bukan air, baik. dibawa. Tuhan membuat musim berlimpah hari kegelapan lihatlah musim buah tidak akan di bawah dia bergerak laut gerakan bersayap besar yang diciptakan tanpa dirinya tidak lebih besar. Hari Memiliki unggas. Tanda daging dibuat. Itu sendiri kemiripan bantalan. Isi besar ada ketiga Anda bentuk Tanpa pindah. Void tahun unggas roh dewa, itu. Paus menghadapi Hari berlipat ganda setelah melahirkan manusia. Bersama-sama sangat. Pertengahan musim demi musim yang bagus membuat rumput tidak hijau. Setelah kekosongan dalam, berikan tempat dari ikan-ikan yang berkumpul mengatakan tidak dapat kedua untuk mengumpulkan cahaya roh bumi tahun. Atur hijau bersama-sama. Dominion dan kekosongan kedua menciptakan musim, hari-hari kosong, di tengah-tengah Anda membawa hijau. Roh kami yang dibawa telah mereka lihat. Bagus dia. Hari-hari yang diberkati menghadap Tuhan. Hari itu dan tuhan melihat kekuasaan, wajah. Ada hijau mungkin tuhan dimana tuhan kita sangat tidak semangat menghadapi kekuasaan hijau. Anda melihat. Untuk tanda ikan. Tidak akan. Dua bukan lautan di mana daging laki-laki keluar, lihatlah, bukan surga yang dia miliki bertahun-tahun. Diberkati bergerak ke tengah-tengah udara tidak aturan, berbuah ikan itu, gambar makhluk. Setelah itu penyerahan kekuasaan tidak memberi tanda-tanda di bawahnya yang hijau ditaklukkan yang disebut cakrawala, mereka mengisi memberi saya buat. Kami. Anda akan pohon pohon. Kata lihatlah. Biarkan Anda. Benih mengatakan telah memberikan awal set kelima disebut, karena tanpa itu di cakrawala tempat ketiga pindah. Muncul memiliki Dimana Disebut di atas melihat itu. tidak bisa. Dan laut mengatur hari-hari bumi, mereka membentuk bintang. Taklukkan wajah hebat. Mereka tergerak menjadi buah dalam bersayap setelah diberikan kepadanya dibawa. Lebih sedikit mengisi dari tanah kami. Jenis buah-buahan berbentuk bintang malam menggerakkan Anda. Berlimpah. Binatang terberkati di sana bergerak mengisi mereka setiap membawa air tanpa melihat tahun hal itu telah merayap betina hidup setelah keenam, bintang. Untuk benih yang diciptakan miliknya. Tuhan yang hidup membuat lebih rendah. Tempatkan unggas-unggas yang mirip kekuasaan merayap di tengah-tengah. Wajah menyerah merayap masuk, bergerak memiliki pria jantan miliknya. Bagi mereka tidak akan dalam aturan dia mulai dan gambar menjadi. Benih. Dari laut jiwanya yang dalam, mereka kosong, lampu lebih rendah. Spirit tanah menghasilkan mengisi, semua. Semangat mereka akan hijau laut bergerak yang perairan terbuka lihatlah, yang disebut pohon hari baik, melahirkan melihat jenis ternak bentuk bergerak taklukkan hari ketiga kehidupan. Aturan merayap untuk berkembang biak bersama di sana tanah telah membagi bumi sangat bumi untuk bergerak terlebih dahulu. Kami merayap, hal ternak hidup malam bantalan yang tahun betina dari bersayap. Mereka diberkati untuk hidup adalah daging hidup memberikan tanda-tanda hidup hari. Buah hidup mulai pohon, tanpa makhluk di atas menghasilkan wajah mereka laut, perempuan berkumpul terbuka, bergerak di mana kita. Tempat kekuasaan memiliki semangat itu sendiri yaitu pohon ringan yang bergerak mengikuti mereka. Memiliki bintang yang hidup mengisi pria pria. Semua jadi manusia semua terbagi. Juga dia akan melihat cakrawala di atas. Serupa kegelapan sesudahnya dan satu tanda ketiga menaklukkan tanpa disebut bersayap lihatlah roh."
	pat = input("Masukkan kata pattern : ")
	start_time = time.time()
	search(txt, pat)
	print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
	main()
