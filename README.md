# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institute adalah institusi pendidikan tinggi yang berdiri sejak tahun 2000 dan menerima mahasiswa dari berbagai latar belakang. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout, hal ini menjadi tantangan utama. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. 

### Permasalahan Bisnis

Permasalahan bisnis utama yang hendak diselesaikan adalah menurunkan tingkat dropout murid yang tinggi di Jaya Jaya Institute. Beberapa pertanyaan utama yang ingin dijawab meliputi:

- Faktor-faktor apa yang paling berpengaruh terhadap murid yang dropout (finansial, akademis, dsb)?
- Apakah dapat dibangun model prediksi sederhana untuk mengidentifikasi murid yang berisiko tinggi akan dropout sehingga dapat dilakukan intervensi dini?
- Tindakan apa yang dapat diambil institusi (terutama oleh HR dan manajemen) agar dapat meningkatkan jumlah graduate kedepannya dan menurunkan jumlah dropout ?

### Cakupan Proyek

Cakupan proyek ini meliputi analisis menyeluruh terhadap data murid Jaya Jaya Institut guna mengidentifikasi pola dropout dan faktor-faktor penyebabnya, pembuatan dashboard bisnis sebagai alat monitoring dan insight, pembangunan model machine learning sederhana untuk memprediksi status(dropout/graduate/enrolled), serta rekomendasi tindakan strategis. Secara spesifik, langkah-langkah proyek mencakup:

- Data understanding & preparation: Mengumpulkan dan membersihkan data murid (informasi demografis seperti usia-jenis kelamin-status pernikahan, kemudian data akademik seperti nilai semester-jurusan-admission grade, dan finansial seperti status beasiswa-pelunasan biaya kuliah-status peminjam, dsb).
- Exploratory data analysis(Univariate & Multivariate): Mengolah data untuk menemukan hubungan antara variabel (usia, gender, nilai, penerima beasiswa atau bukan, dll.) dengan status kelulusan(Dropout/Graduate/Enrolled).
- Business dashboard development: Membuat dashboard yang menyajikan metrik status kelulusan dan visualisasi penting untuk membantu pemangku kepentingan memahami kondisi secara cepat.
- Modeling: Membangun model prediksi sederhana untuk mengidentifikasi kemungkinan dropout berdasarkan faktor-faktor tertentu.
- Evaluation & insight: Mengevaluasi hasil analisis dan model, menginterpretasikan temuan utama.
- Deploy Model: Mendeploy model yang telah dibangun pada streamlit agar dapat digunakan oleh pihak Jaya Jaya Institute dalam memprediksi murid dengan cara menginputkan 15 fitur yang paling berkorelasi dengan status kelulusan.
- Recommendations: Menyusun rekomendasi action items bagi Jaya Jaya Institute untuk menekan jumlah dropout agar dapat berkurang.

Batasan proyek: Analisis difokuskan pada data Murid Jaya Jaya Institute saja, proyek ini fokus pada penyediaan insight data-driven.

### Persiapan

Sumber data : Dataset Student Performance [Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance).

Data terdiri dari 4.424 baris dan 37 kolom (fitur), mencakup atribut demografis (misalnya `gender`, `marital_status`, `age_at_enrollment`), akademik (`admission_grade`, `unit1_semester_grade`, `unit2_semester_grade`), serta variabel finansial (`scholarship`, `tuition_up_to_date`, `is_debtor`), dsb.

Setup environment: Proyek dianalisis menggunakan bahasa Python dalam lingkungan Jupyter Notebook. Untuk mengaksesnya :

- Setup conda environment:

    ```
    conda create --name datascience-human-resources python==3.11.12
    ```
- Install requirements:
    ```
    pip install -r requirements.txt
    ```
- Setup metabase:
    ```
    docker pull metabase/metabase:v0.46.4
    docker run -p 3000:3000 --name metabase metabase/metabase
    ```
    Akses metabase pada http://localhost:3000/setup dan lakukan setup.
- Setup database (supabase):

    - Buat akun dan login https://supabase.com/dashboard/sign-in.
    - Buat project
    - Copy URI pada database setting
    - Kirim dataset menggunakan sqlalchemy 
    ```python
    from sqlalchemy import create_engine
 
    URL = "DATABASE_URL"
    
    engine = create_engine(URL)
    df.to_sql('orders', engine)
    ```

## Business Dashboard

Untuk memudahkan pemantauan dan komunikasi insight, telah dibuat business dashboard yang menampilkan metrik status murid beserta fitur-fiturnya dan visualisasi penting. Dashboard ini dirancang agar Jaya Jaya Institute dapat secara cepat mengidentifikasi pola murid yang potensi akan dropout menurut berbagai dimensi dan melakukan drill-down pada area yang membutuhkan perhatian agar para murid yang diprediksi akan dropout dapat diselesaikan permasalahan yang dihadapinya agar dapat graduate.

<img src="https://raw.githubusercontent.com/mraihanfauzii/student-dropout-prediction/main/images/mraihanfauzi-dashboard.png" width="500">

Dengan adanya business dashboard ini, diharapkan Jaya Jaya Institute dapat memantau dan meningkatkan jumlah graduate pada murid secara berkelanjutan dan melakukan pendekatan kepada murid yang berpotensi akan dropout untuk diberikan bimbingan serta penyelesaian masalah yang mereka alami.

## Prototype Sistem Machine Learning

<img src="https://raw.githubusercontent.com/mraihanfauzii/student-dropout-prediction/main/images/demo_model.png" width="500">

Prototipe hasil pengembangan  sudah di-deploy dengan Streamlit dan dapat diakses secara online melalui [https://student-dropout-prediction-mraihanfauzii.streamlit.app/](https://student-dropout-prediction-mraihanfauzii.streamlit.app/). Cara menggunakannya untuk memprediksi apakah seorang mahasiswa akan dropout yaitu pengguna dapat memasukkan data mahasiswa seperti yang ada pada gambar sebagai input lalu menekan tombol predict, maka model akan memprediksi status mahasiswa (Dropout/Enrolled/Graduated) secara real-time. Atau jika ingin melakukannya di local maka dapat download file-file yang ada pada proyek ini dan letakan pada folder yang sama kemudian buka terminal dan jalankan perintah    ```
        streamlit run app.py
    ```

## Conclusion

Masalah bisnis utama di Jaya Jaya Institute adalah tingginya tingkat dropout mahasiswa. Dropout menyebabkan kerugian finansial bagi institusi (pendapatan berkurang, reputasi menurun) dan berdampak negatif pada masa depan mahasiswa (peluang kerja, penghasilan). Oleh karena itu, pihak manajemen ingin mengidentifikasi faktor penyebab dropout dan mengembangkan solusi tepat guna. Tujuan proyek data science ini adalah menganalisis faktor-faktor yang berkontribusi terhadap dropout, membangun dashboard visualisasi yang intuitif, dan mengembangkan model machine learning untuk memprediksi mahasiswa berisiko dropout. Dengan demikian, institusi dapat melakukan intervensi dini seperti bimbingan khusus bagi mahasiswa berisiko tinggi (strategy pencegahan). Berikut adalah kesimpulan yang ditemukan pada setiap fitur dari hasil analisis yang telah dilakukan yang berkaitan dengan status mahasiswa :

<img src="https://raw.githubusercontent.com/mraihanfauzii/student-dropout-prediction/main/images/status_overall.png" width="500">

- Status Kelulusan Keseluruhan: Visualisasi data keseluruhan menunjukkan bahwa sekitar 32,1% mahasiswa berhenti studi (dropout), sedangkan sekitar 49,9% lulus dan 17,9% masih terdaftar. Proporsi dropout yang cukup besar (sekitar satu per tiga) menyoroti masalah signifikan dalam retensi mahasiswa di institusi ini. Di sisi lain, persentase lulusan di bawah 50% mengindikasikan masih banyak mahasiswa yang belum berhasil menyelesaikan studi. Insight ini menekankan urgensi penerapan strategi kampus untuk menekan angka dropout dan meningkatkan angka kelulusan, misalnya melalui dukungan tambahan bagi mahasiswa rentan.

<img src="https://raw.githubusercontent.com/mraihanfauzii/student-dropout-prediction/main/images/status_by_gender.png" width="500">

- Status berdasarkan Gender: Grafik batang menunjukkan tingkat dropout yang lebih tinggi pada mahasiswa laki-laki dibanding perempuan. Proporsi mahasiswa pria yang putus studi jauh lebih besar secara relatif, meskipun jumlah total mahasiswa wanita lebih banyak. Temuan ini mengindikasikan perlunya intervensi khusus untuk kelompok gender rentan, seperti program pendampingan atau mentoring khusus mahasiswa pria. Institusi dapat menargetkan program bimbingan belajar atau konseling sosial yang disesuaikan untuk meningkatkan retensi di kalangan mahasiswa laki-laki.

<img src="https://raw.githubusercontent.com/mraihanfauzii/student-dropout-prediction/main/images/status_by_age_group.png" width="500">

- Status berdasarkan Kelompok Umur: Diagram kelompok usia mengungkap bahwa mahasiswa usia muda (<20 tahun) dominan lulus, sedangkan kelompok usia lanjut menunjukkan kecenderungan dropout lebih tinggi. Misalnya, persentase dropout meningkat pada mahasiswa usia 30 tahun ke atas, yang kemungkinan besar menghadapi tanggung jawab eksternal (pekerjaan atau keluarga) lebih besar. Sebaliknya, mahasiswa usia <20 lebih sedikit yang putus studi karena umumnya baru memulai dan belum banyak beban tambahan. Insight ini menunjukkan bahwa dukungan pendidikan perlu ditingkatkan khususnya bagi mahasiswa dewasa, seperti fleksibilitas waktu kuliah atau program penggabungan studi–kerja.

<img src="https://raw.githubusercontent.com/mraihanfauzii/student-dropout-prediction/main/images/status_by_admission_grade.png" width="500">

- Status berdasarkan Nilai Masuk: Grafik ini menunjukkan korelasi positif antara prestasi awal dan keberhasilan studi. Mahasiswa dengan admission grade rendah (misalnya di bawah 100) relatif lebih banyak yang dropout, sedangkan mahasiswa dengan nilai masuk tinggi (>140) mayoritas lulus. Kelompok terbesar ada pada nilai 120–139, di mana angka dropout cukup tinggi namun juga terdapat banyak lulusan. Temuan ini mengisyaratkan bahwa prestasi awal berperan penting; institusi sebaiknya memberikan dukungan akademik tambahan (misalnya kelas pendahuluan atau remedial) bagi mahasiswa dengan admission grade rendah agar mereka tidak segera putus studi.

<img src="https://raw.githubusercontent.com/mraihanfauzii/student-dropout-prediction/main/images/status_by_scholarship_holder.png" width="500">

- Status berdasarkan Penerima Beasiswa: Mahasiswa penerima beasiswa menunjukkan tingkat keberhasilan studi yang jauh lebih tinggi. Hampir semua penerima beasiswa berstatus lulus atau masih terdaftar, dengan persentase dropout sangat rendah. Sebaliknya, mahasiswa non-penerima beasiswa memiliki proporsi dropout yang lebih besar. Temuan ini memperkuat bahwa dukungan finansial (beasiswa) sangat membantu retensi; mahasiswa yang mendapat beasiswa termotivasi untuk menyelesaikan kuliah karena beban biaya mereka lebih ringan.

<img src="https://raw.githubusercontent.com/mraihanfauzii/student-dropout-prediction/main/images/status_by_tuition_fee_current.png" width="500">

- Status berdasarkan Pembayaran SPP: Perbandingan antara mahasiswa yang SPP-nya terkini dan tertunggak menunjukkan perbedaan mencolok. Hampir semua mahasiswa yang membayar tepat waktu berstatus lulus atau terdaftar, sementara kelompok yang menunggak sebagian besar mengalami dropout. Bahkan, kelompok tunggakan hampir tidak memiliki lulusan sama sekali. Insight ini jelas menunjukkan faktor finansial sebagai penentu kuat: mahasiswa kesulitan membayar biaya kuliah rentan putus studi karena terbebani tunggakan.

<img src="https://raw.githubusercontent.com/mraihanfauzii/student-dropout-prediction/main/images/status_by_finance_flags_is_debtor.png" width="500">

- Status berdasarkan Flag Debitur: Grafik ini membandingkan mahasiswa berdasarkan status hutang studi. Terlihat bahwa proporsi mahasiswa debitur (memiliki hutang) yang dropout relatif tinggi, bahkan hampir setara dengan yang lulus. Sebaliknya, di kalangan non-debitur jumlah lulusan jauh lebih besar daripada yang dropout. Hal ini menunjukkan beban hutang meningkatkan risiko putus kuliah karena tekanan finansial/mental. Oleh karena itu, mahasiswa yang memiliki hutang studi lebih rentan dan perlu perhatian khusus.

<img src="https://raw.githubusercontent.com/mraihanfauzii/student-dropout-prediction/main/images/status_by_curricular_units_1st_sem_grade.png" width="500">

- Status berdasarkan Prestasi Semester 1: Visualisasi berdasarkan jumlah mata kuliah yang lulus di semester pertama mengindikasikan peran kritis prestasi awal. Mahasiswa yang tidak lulus satu pun mata kuliah (0 unit) mayoritas putus studi, sedangkan yang lulus sebagian besar (misalnya 10–14 unit) tingkat kelulusannya tinggi. Contohnya, kelompok 10–14 unit menunjukkan proporsi lulusan yang dominan. Temuan ini menggarisbawahi bahwa nilai akademik awal sangat menentukan; mahasiswa dengan prestasi rendah di awal perlu intervensi cepat (tutor/remedial) untuk menghindari dropout.

<img src="https://raw.githubusercontent.com/mraihanfauzii/student-dropout-prediction/main/images/status_by_curricular_units_2nd_sem_grade.png" width="500">

- Status berdasarkan Prestasi Semester 2: Tren serupa terlihat di semester kedua. Mahasiswa yang lulus banyak mata kuliah (15–20 unit) hampir semuanya lulus kuliah, sementara mereka dengan jumlah lulus rendah cenderung masih menempuh studi atau drop out. Sebagai contoh, kelompok dengan 0 unit menunjukkan jumlah mahasiswa terdaftar dan dropout yang lebih tinggi dibanding lulusan. Ini menegaskan bahwa peningkatan prestasi akademik dari semester pertama ke kedua penting untuk keberlanjutan studi; mereka yang stagnan di angka rendah lebih berisiko putus.

<img src="https://raw.githubusercontent.com/mraihanfauzii/student-dropout-prediction/main/images/status_by_application_mode.png" width="500">

- Status berdasarkan Jalur Pendaftaran: Grafik jalur pendaftaran menunjukkan variasi keberhasilan. Mahasiswa jalur umum tahap pertama (1st phase general) mendominasi lulusan dan hanya sedikit yang dropout. Sebaliknya, mahasiswa jalur “Over 23” (berusia di atas 23 tahun) memiliki proporsi dropout yang hampir setara dengan lulusan, menandakan risiko tinggi bagi kelompok ini. Jalur seleksi lain (seperti fase 2) berada di tengah-tengah. Insight ini menunjukkan bahwa latar belakang jalur masuk (termasuk faktor usia) memengaruhi retensi, sehingga kelompok tertentu (misalnya mahasiswa dewasa) perlu perhatian khusus.

Berdasarkan analisis di atas, dapat disimpulkan bahwa faktor finansial (tunggakan dan beasiswa) serta akademik (nilai awal dan jumlah mata kuliah yang ditempuh) sangat menentukan tingkat kelulusan mahasiswa. Mahasiswa yang kesulitan membayar biaya kuliah atau yang memiliki prestasi akademik rendah lebih berisiko putus studi. Dengan mengenali karakteristik mahasiswa berisiko dari visualisasi ini dan model prediksi, institusi dapat mengambil langkah pencegahan terarah.

### Rekomendasi Action Items

Berdasarkan temuan di atas, dapat direkomendasikan beberapa langkah tindakan bagi Jaya Jaya Institute untuk menurunkan jumlah dropout dan meningkatkan jumlah graduate:

- Status Kelulusan Keseluruhan, Sistem Pemantauan dan Intervensi Dini: Kembangkan sistem peringatan dini berbasis data untuk mengidentifikasi mahasiswa berisiko dropout secara menyeluruh. Integrasikan pemodelan prediktif dan dashboard pemantauan agar mahasiswa rentan dapat cepat ditindaklanjuti (misalnya melalui konseling akademik/psikologis maupun bantuan finansial). Program Retensi Menyeluruh: Rancang program pendampingan komprehensif meliputi dukungan akademik, psikososial, dan keuangan bagi mahasiswa rentan. Contohnya, perluas subsidi atau beasiswa bagi mereka yang berjuang secara finansial, serta adakan workshop motivasi dan mentoring lintas tingkat untuk menjaga keterlibatan mahasiswa.

- Jenis Kelamin, Program Khusus Mahasiswa Pria: Buat program pendampingan dan workshop yang menargetkan mahasiswa laki-laki, misalnya kelompok belajar khusus atau forum diskusi akademik. Pendampingan ini bisa dipandu oleh dosen atau alumni pria guna meningkatkan motivasi belajar dan mengurangi risiko putus studi pada kelompok ini. Edukasi dan Dukungan Sosial: Adakan sesi diskusi tentang isu-isu sosial dan manajemen stres yang sering dialami mahasiswa pria, serta latih soft skills seperti komunikasi interpersonal. Dengan intervensi berbasis data ini, diharapkan angka dropout di kalangan laki-laki dapat ditekan.

- Kelompok Umur, Pembelajaran Fleksibel: Tawarkan skema kuliah fleksibel seperti kelas malam, pembelajaran daring, atau program hybrid untuk mahasiswa dewasa yang bekerja atau memiliki keluarga. Fleksibilitas waktu ini dapat membantu mereka menyeimbangkan studi dengan tanggung jawab eksternal. Dukungan Khusus Dewasa: Sediakan konseling dan workshop manajemen waktu/keuangan khusus bagi mahasiswa berusia lanjut. Misalnya, program pendampingan karier atau kelompok diskusi rekan sebaya (peer support) agar mereka merasa lebih termotivasi dan terintegrasi dalam lingkungan akademik.

- Nilai Masuk (Admission Grade), Kelas Penyegaran Akademik: Selenggarakan kelas pendahuluan atau remedial untuk mata kuliah dasar bagi mahasiswa dengan admission grade rendah. Dengan pembinaan akademik awal (bridge course) ini, mahasiswa dapat memperkuat landasan akademik sebelum memulai perkuliahan reguler. Mentoring Akademik: Pasangkan mahasiswa berpredikat masuk rendah kepada mentor (dosen atau senior) untuk membimbing kemajuan studi mereka. Pemantauan rutin terhadap performa akademik awal dapat membantu memberikan intervensi segera jika nilai mulai menurun.

- Penerima Beasiswa, Perluasan Skema Beasiswa: Tambah kuota dan jenis beasiswa (prestasi maupun kebutuhan) agar lebih banyak mahasiswa terbantu secara finansial. Karena penerima beasiswa terbukti memiliki risiko dropout rendah, memperluas bantuan ini dapat meningkatkan kelulusan secara keseluruhan. Insentif dan Penghargaan: Berikan penghargaan atau tambahan bantuan (misalnya potongan biaya SPP) bagi mahasiswa yang menunjukkan kemajuan akademik signifikan. Program “beasiswa prestasi lanjutan” dapat memotivasi mahasiswa untuk tetap berprestasi dan menyelesaikan studi.

- Pembayaran Uang Kuliah, Skema Cicilan dan Subsidi: Sediakan opsi pembayaran kuliah dengan cicilan ringan atau subsidi biaya bagi mahasiswa berpenghasilan rendah. Misalnya, keringanan biaya administrasi untuk cicilan, atau potongan SPP bagi mereka yang selalu tepat waktu membayar. Intervensi Dini Tunggakan: Implementasikan sistem pemantauan tunggakan yang memberikan peringatan awal kepada mahasiswa dan orang tua. Berikan bantuan keuangan sementara atau rujukan ke layanan konseling keuangan kampus agar masalah tunggakan tidak memaksa mahasiswa drop out.

- Status Debitur, Konseling Keuangan: Berikan layanan konseling keuangan bagi mahasiswa debitur untuk merencanakan pembayaran yang realistis atau memperoleh alternatif dana. Misalnya, kemitraan dengan lembaga pemberi pinjaman bersyarat ringat bunga atau opsi restrukturisasi utang studi.Dana Darurat Mahasiswa: Bentuk dana darurat atau hibah kecil yang dapat diberikan sementara kepada mahasiswa berisiko gagal membayar SPP. Bantuan ini bisa mengatasi krisis finansial mendadak sehingga mahasiswa tetap bisa fokus menyelesaikan studi.

- Prestasi Semester 1, Pemantauan Awal Akademik: Identifikasi mahasiswa yang gagal lulus banyak mata kuliah di semester pertama (misalnya lulus <5 unit). Berikan mereka pendampingan khusus segera setelah hasil keluar, seperti tutor pendukung atau kelompok belajar intensif agar tidak semakin tertinggal. Program Remedial: Tawarkan kelas tambahan atau kursus remedial selama libur semester (misalnya Summer School) bagi mahasiswa dengan nilai semester pertama rendah. Tujuannya agar mereka dapat mengejar ketertinggalan sebelum melanjutkan semester berikutnya.

- Prestasi Semester 2, Dukungan Berkelanjutan: Lanjutkan intervensi akademik untuk mahasiswa dengan prestasi rendah di semester kedua, meskipun sudah memasuki tahun kedua studi. Tutor khusus atau bimbingan tatap muka tambahan dapat membantu mereka mengembalikan performa dan tertolong menyelesaikan studi. Motivasi dan Konseling: Selenggarakan workshop motivasi dan sesi konseling tambahan di awal tahun akademik berikutnya bagi mahasiswa yang masih tertinggal. Dengan motivasi ekstra dan target realistis, diharapkan mereka termotivasi kembali untuk berprestasi.

- Mode Pendaftaran : Sediakan orientasi atau mentoring khusus bagi mahasiswa dari jalur masuk berisiko tinggi (misalnya mahasiswa “Over 23” atau transfer). Hal ini bisa berupa pendampingan awal oleh alumni serupa atau kegiatan adaptasi agar mereka merasa diterima dan siap berkuliah. Evaluasi Jalur Masuk: Lakukan kajian mendalam terhadap proses seleksi dan dukungan masing-masing jalur pendaftaran. Jika ditemukan jalur tertentu memiliki angka dropout tinggi, cari faktor penyebabnya (misal kesiapan akademik atau motivasi calon) dan sesuaikan program masuk maupun bantuan sehingga retensi meningkat.

Rekomendasi ini diharapkan dapat membantu institusi ini menurunkan tingkat dropout dengan pendekatan baik finansial maupun akademik.
