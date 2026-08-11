from streamlit.testing.v1 import AppTest
import sys

errors = []

def login(role, name, kelas=None):
    at = AppTest.from_file("app.py")
    at.run(timeout=30)
    at.radio(key="login_role").set_value(role).run()
    at.text_input[0].set_value(name).run()
    if role == "Guru Kelas":
        at.selectbox[0].set_value(kelas).run()
    submit = next(b for b in at.button if "Masuk" in b.label)
    submit.click().run(timeout=30)
    return at

# --- Test 1: Guru Kelas 1 login -> only sees Kelas 1, no kelas-menu buttons ---
for kelas_num in range(1, 7):
    at = login("Guru Kelas", f"Guru Uji {kelas_num}", kelas_num)
    if at.exception:
        errors.append((f"guru-k{kelas_num}", "post-login", str(at.exception)))
        continue
    cta = next((b for b in at.button if b.key == "btn_lanjut_modul"), None)
    if not cta:
        errors.append((f"guru-k{kelas_num}", "no-cta", ""))
        continue
    cta.click().run(timeout=30)
    if at.exception:
        errors.append((f"guru-k{kelas_num}", "post-cta", str(at.exception)))
        continue
    # kelas-menu buttons (btn_kelas_N) should NOT exist for Guru
    kelas_btns = [b for b in at.button if b.key and b.key.startswith("btn_kelas_")]
    if kelas_btns:
        errors.append((f"guru-k{kelas_num}", "kelas-menu-visible-for-guru", str([b.key for b in kelas_btns])))
    md_all = " ".join(m.value for m in at.markdown)
    if f"Kelas {kelas_num}" not in md_all:
        errors.append((f"guru-k{kelas_num}", "own-kelas-not-shown", ""))
    print(f"Guru Kelas {kelas_num}: OK, kelas-menu hidden={not kelas_btns}")

# --- Test 2: Kepala Sekolah login -> full kelas-menu visible ---
at = login("Kepala Sekolah", "Bapak Kepsek Uji")
if at.exception:
    errors.append(("kepsek", "post-login", str(at.exception)))
else:
    cta = next((b for b in at.button if b.key == "btn_lanjut_modul"), None)
    cta.click().run(timeout=30)
    kelas_btns = [b for b in at.button if b.key and b.key.startswith("btn_kelas_")]
    if len(kelas_btns) != 6:
        errors.append(("kepsek", "kelas-menu-not-full", str(len(kelas_btns))))
    print(f"Kepala Sekolah: kelas-menu buttons = {len(kelas_btns)}")

# --- Test 3: Pertemuan menu interaction + badges, for a project with dates (Menara Bentuk, Kelas 2) ---
at = login("Guru Kelas", "Guru Kelas2 Uji", 2)
cta = next((b for b in at.button if b.key == "btn_lanjut_modul"), None)
cta.click().run(timeout=30)
if at.exception:
    errors.append(("k2-pertemuan", "post-cta", str(at.exception)))
else:
    # find and expand the "Uraian Langkah Tiap Pertemuan" expander implicitly rendered; buttons should exist
    pert_btns = [b for b in at.button if b.key and b.key.startswith("btn_pert_")]
    print(f"Kelas 2 pertemuan buttons found: {[b.key for b in pert_btns]}")
    if not pert_btns:
        errors.append(("k2-pertemuan", "no-pert-buttons", ""))
    else:
        # click P2 button for first project card
        p2_btn = next((b for b in pert_btns if b.key.endswith("_2")), None)
        if p2_btn:
            p2_btn.click().run(timeout=30)
            if at.exception:
                errors.append(("k2-pertemuan", "post-p2-click", str(at.exception)))
            else:
                md_all = " ".join(m.value for m in at.markdown)
                checks = {
                    "pert-detail-card": "pert-detail-card" in md_all,
                    "pert-badge (tahap)": "Praktik Pedagogis" in md_all,
                    "Pengalaman Belajar badge": "Pengalaman Belajar:" in md_all,
                    "Prinsip badge": "Prinsip:" in md_all,
                    "Langkah Kegiatan Guru section": "Langkah Kegiatan Guru" in md_all,
                    "Langkah Kegiatan Siswa section": "Langkah Kegiatan Siswa" in md_all,
                }
                print("Checks:", checks)
                if not all(checks.values()):
                    errors.append(("k2-pertemuan", "missing-content", str(checks)))

# --- Test 4: Rumah Cerdas (Kelas 6, project #1) shows 'perkiraan' fallback dates ---
at = login("Guru Kelas", "Guru Kelas6 Uji", 6)
cta = next((b for b in at.button if b.key == "btn_lanjut_modul"), None)
cta.click().run(timeout=30)
if at.exception:
    errors.append(("k6-perkiraan", "post-cta", str(at.exception)))
else:
    md_all = " ".join(m.value for m in at.markdown)
    has_perkiraan = "perkiraan" in md_all.lower()
    print(f"Kelas 6 has 'perkiraan' marker: {has_perkiraan}")
    if not has_perkiraan:
        errors.append(("k6-perkiraan", "no-perkiraan-marker", ""))

if errors:
    print("ERRORS:", errors)
    sys.exit(1)
else:
    print("ALL OK")
