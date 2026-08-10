# -*- coding: utf-8 -*-
"""
Konten Landing Page LMS STEM Gugus Lengkongjaya.
Sumber:
- Gambaran Umum Pelatihan  -> "Panduan Pembelajaran STEM" (Kemendikdasmen, 2025)
- Lini Masa Acara Hari Ini -> "Skenario Kegiatan KKG Gugus Lengkongjaya" (STEM, Kelas 1-6)

Memisahkan konten ke modul ini supaya mudah diperbarui tanpa menyentuh app.py,
dan supaya modul-modul berikutnya (Modul Kelas, dst.) bisa memakai data yang sama.
"""

OVERVIEW = {
    "judul": "Pembelajaran STEM Berbasis Proyek",
    "subjudul": "Kelas 1 s.d. Kelas 6 — KKG Gugus Lengkongjaya",
    "definisi": (
        "STEM (Sains, Teknologi, Enjinering, Matematika) adalah pendekatan "
        "pembelajaran lintas disiplin yang mendorong murid berpikir kritis, "
        "kreatif, berkolaborasi, dan memecahkan masalah dunia nyata melalui "
        "praktik saintifik dan enjinering."
    ),
    "pendekatan": (
        "Sebagai praktik pedagogis pembelajaran mendalam, pembelajaran STEM "
        "dijalankan melalui Siklus 3M: **Memahami → Mengaplikasi → Merefleksi**, "
        "dengan tiga prinsip pembelajaran mendalam: **Berkesadaran, Bermakna, "
        "dan Menggembirakan**."
    ),
    "tujuan": [
        "Menyamakan pemahaman guru terhadap 6 modul proyek STEM Kelas 1–6",
        "Memberi pengalaman langsung menjalani siklus 3M sebelum diterapkan ke siswa",
        "Menguatkan prinsip pembelajaran mendalam dalam praktik pedagogis guru",
        "Menyusun Rencana Tindak Lanjut (RTL) penerapan proyek STEM di sekolah masing-masing",
    ],
    "referensi": "Panduan Pembelajaran STEM, Kemendikdasmen 2025",
}

EVENT = {
    "nama": "Pertemuan KKG Gugus Lengkongjaya — Pembelajaran STEM Berbasis Proyek",
    "tema": "Penerapan Modul Proyek STEM Kelas 1–6 dengan Siklus 3M dan Prinsip Pembelajaran Mendalam",
    "waktu": "07.30 – 12.10 WIB",
    "sasaran": "Guru Kelas 1 s.d. Kelas 6 anggota KKG Gugus Lengkongjaya",
    "kelompok": "6 kelompok, dikelompokkan berdasarkan jenjang kelas",
    "referensi": "Skenario Kegiatan KKG Gugus Lengkongjaya — STEM",
}

# Prinsip pembelajaran mendalam per segmen (untuk pewarnaan lini masa di UI)
PRINSIP_WARNA = {
    "Berkesadaran": "#2563EB",   # biru
    "Bermakna": "#16A34A",       # hijau
    "Menggembirakan": "#F59E0B",  # kuning/oranye
    "3M Lengkap": "#7C3AED",     # ungu
    "—": "#9CA3AF",         # abu (transisi)
}

# Warna tahap Pengalaman Belajar (Siklus 3M) per pertemuan pada Modul Proyek
# STEM, dipakai untuk badge di menu "Uraian Langkah Tiap Pertemuan".
PENGALAMAN_WARNA = {
    "Memahami": "#0EA5E9",     # biru langit
    "Mengaplikasi": "#7C3AED",  # ungu
    "Merefleksi": "#DB2777",   # pink
}

AGENDA = [
    {"waktu": "07.30–08.00", "kegiatan": "Registrasi & Pembukaan",
     "bentuk": "Pleno", "penanggung_jawab": "Koordinator KKG", "prinsip": "Berkesadaran"},
    {"waktu": "08.00–08.20", "kegiatan": "Paparan Umum: STEM PjBL, Kalender Pendidikan, Daftar Alat & Bahan",
     "bentuk": "Pleno", "penanggung_jawab": "Koordinator KKG / Narasumber", "prinsip": "Bermakna"},
    {"waktu": "08.20–08.30", "kegiatan": "Pembentukan Kelompok Kelas & Mobilisasi ke Ruang",
     "bentuk": "Transisi", "penanggung_jawab": "Panitia", "prinsip": "—"},
    {"waktu": "08.30–11.15", "kegiatan": "Sesi Kelompok Kelas — Siklus 3M (6 kelas paralel)",
     "bentuk": "Kelompok (6 kelas)", "penanggung_jawab": "Fasilitator per kelas", "prinsip": "3M Lengkap"},
    {"waktu": "11.15–11.45", "kegiatan": "Berbagi Hasil Antarkelompok (Gallery Walk)",
     "bentuk": "Pleno", "penanggung_jawab": "Perwakilan tiap kelompok", "prinsip": "Bermakna"},
    {"waktu": "11.45–12.00", "kegiatan": "Refleksi Bersama & Rencana Tindak Lanjut (RTL)",
     "bentuk": "Pleno", "penanggung_jawab": "Koordinator KKG", "prinsip": "Berkesadaran"},
    {"waktu": "12.00–12.10", "kegiatan": "Penutup",
     "bentuk": "Pleno", "penanggung_jawab": "Koordinator KKG", "prinsip": "Menggembirakan"},
]

KELOMPOK_KELAS = [
    {"kelas": "Kelas 1", "modul": "Berhitung Asyik dengan Benda Kesayangan", "fase": "Fase A"},
    {"kelas": "Kelas 2", "modul": "Menara Bentuk: Membangun dari Bangun Ruang", "fase": "Fase A"},
    {"kelas": "Kelas 3", "modul": "Es Krim Kantong Ajaib: Mengamati Perubahan Wujud", "fase": "Fase B"},
    {"kelas": "Kelas 4", "modul": "Zat Ajaib: Mengamati Perubahan Wujud di Sekitar Kita", "fase": "Fase B"},
    {"kelas": "Kelas 5", "modul": "Detektif Zat: Memisahkan Campuran di Sekitar Kita", "fase": "Fase C"},
    {"kelas": "Kelas 6", "modul": "Kompas dan Peta Harta Karun", "fase": "Fase C"},
]

# Peta nomor kelas -> nama berkas "Daftar Proyek STEM" yang dibaca dinamis
# saat guru memilih kelas di halaman Modul Kelas. Berkas ini berada satu
# tingkat di atas folder aplikasi (folder Cowork utama).
CLASS_FILES = {
    1: "Daftar_Proyek_STEM_Kelas1.docx",
    2: "Daftar_Proyek_STEM_Kelas2.docx",
    3: "Daftar_Proyek_STEM_Kelas3.docx",
    4: "Daftar_Proyek_STEM_Kelas4.docx",
    5: "Daftar_Proyek_STEM_Kelas5.docx",
    6: "Daftar_Proyek_STEM_Kelas6_Lintas_Mapel_v2.docx",
}

# Berkas Program Supervisi Kepala Sekolah (dibaca dinamis di Portal Supervisi)
SUPERVISI_FILE = "Program_Supervisi_Kepala_Sekolah_STEM.docx"

# Peta Judul Proyek (persis seperti tertulis di kolom "Judul Proyek" pada
# Daftar_Proyek_STEM_Kelas*.docx) -> berkas Modul Proyek STEM lengkap
# dan/atau Panduan Guru Pembuatan Produk pendampingnya. Hanya proyek yang
# memang sudah memiliki modul & panduan tersusun yang dicantumkan di sini;
# proyek lain di Daftar Proyek tetap tampil ringkas tanpa detail tambahan.
PROJECT_DOCS = {
    "Berhitung Asyik dengan Benda Kesayangan": {
        "modul": "Modul_Proyek_STEM_Berhitung_Asyik.docx",
        "panduan": None,
    },
    "Menara Bentuk: Membangun dari Bangun Ruang": {
        "modul": "Modul_Proyek_STEM_Menara_Bentuk.docx",
        "panduan": "Panduan_Guru_Pembuatan_Produk_Menara_Bentuk.docx",
    },
    "Es Krim Kantong Ajaib: Mengamati Perubahan Wujud": {
        "modul": "Modul_Proyek_STEM_Es_Krim_Kantong_Ajaib.docx",
        "panduan": "Panduan_Guru_Pembuatan_Produk_Es_Krim_Kantong_Ajaib.docx",
    },
    "Zat Ajaib: Mengamati Perubahan Wujud di Sekitar Kita": {
        "modul": "Modul_Proyek_STEM_Zat_Ajaib.docx",
        "panduan": "Panduan_Guru_Pembuatan_Produk_Zat_Ajaib.docx",
    },
    "Detektif Zat: Memisahkan Campuran di Sekitar Kita": {
        "modul": "Modul_Proyek_STEM_Detektif_Zat.docx",
        "panduan": "Panduan_Guru_Pembuatan_Produk_Detektif_Zat.docx",
    },
    "Rumah Cerdas Hemat Energi": {
        "modul": "Modul_Proyek_STEM_Rumah_Cerdas_Kelas6_v2.docx",
        "panduan": "Panduan_Guru_Pembuatan_Produk_Rumah_Cerdas.docx",
    },
    "Kompas dan Peta Harta Karun": {
        "modul": "Modul_Proyek_STEM_Kompas_Peta_Harta_Karun_v2.docx",
        "panduan": "Panduan_Guru_Pembuatan_Produk_Kompas_Peta.docx",
    },
    "Ekosistem Mini dalam Botol (Ekobotol)": {
        "modul": "Modul_Proyek_STEM_Ekobotol.docx",
        "panduan": None,
    },
}

# Menu navigasi utama aplikasi (label tampilan -> kunci halaman internal)
NAV_PAGES = {
    "🏠 Beranda": "landing",
    "🏫 Modul Kelas": "modul_kelas",
    "👨‍💼 Portal Supervisi": "supervisi",
}

# Peran pengguna untuk halaman login sederhana (pilih peran + nama, tanpa kata sandi)
ROLES = ["Guru Kelas", "Kepala Sekolah"]

# Sub-halaman (Lampiran) di dalam Portal Supervisi Kepala Sekolah
LAMPIRAN_TABS = {
    "📋 Observasi Kelas": "lampiran1",
    "✅ Telaah Dokumen": "lampiran2",
    "🤝 Tindak Lanjut": "lampiran3",
    "📊 Rekap Tahunan": "lampiran4",
}
