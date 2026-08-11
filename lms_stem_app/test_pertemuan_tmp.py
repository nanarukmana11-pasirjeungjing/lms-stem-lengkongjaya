from streamlit.testing.v1 import AppTest
import sys

def run_flow(role, name, kelas_list):
    at = AppTest.from_file("app.py")
    at.run(timeout=30)
    assert not at.exception, f"login page exception: {at.exception}"
    # Fill login form
    at.radio(key="login_role").set_value(role).run()
    at.text_input(key="login_nama").set_value(name).run()
    if role == "Guru Kelas":
        at.selectbox(key="login_kelas").set_value(kelas_list[0]).run()
    at.button(key="btn_login").click().run(timeout=30)
    assert not at.exception, f"post-login exception: {at.exception}"
    return at

# Test as Kepala Sekolah (access to all classes via modul kelas page) is not typical;
# instead test as Guru Kelas per kelas, and also try browsing modul_kelas for all classes.
errors = []
for kelas_num in range(1, 7):
    at = AppTest.from_file("app.py")
    at.run(timeout=30)
    try:
        at.radio(key="login_role").set_value("Guru Kelas").run()
        at.text_input(key="login_nama").set_value(f"Guru Uji {kelas_num}").run()
        at.selectbox(key="login_kelas").set_value(f"Kelas {kelas_num}").run()
        at.button(key="btn_login").click().run(timeout=30)
        if at.exception:
            errors.append((kelas_num, "post-login", str(at.exception)))
            continue
        # go to modul kelas
        found = False
        for b in at.button:
            if b.key == "cta_modul_kelas":
                b.click().run(timeout=30)
                found = True
                break
        if not found:
            errors.append((kelas_num, "no-cta-button", ""))
            continue
        if at.exception:
            errors.append((kelas_num, "post-cta", str(at.exception)))
            continue
        # click the specific kelas button
        clicked = False
        for b in at.button:
            if b.key == f"btn_kelas_{kelas_num}":
                b.click().run(timeout=30)
                clicked = True
                break
        if not clicked:
            errors.append((kelas_num, "no-kelas-button", ""))
            continue
        if at.exception:
            errors.append((kelas_num, "post-kelas-click", str(at.exception)))
            continue
        # check markdown for pertemuan-chip or pertemuan-note presence
        md_all = " ".join(m.value for m in at.markdown)
        has_chip = "pertemuan-chip" in md_all
        has_note = "pertemuan-note" in md_all
        print(f"Kelas {kelas_num}: chip={has_chip} note={has_note}")
    except Exception as e:
        errors.append((kelas_num, "test-exception", str(e)))

if errors:
    print("ERRORS:", errors)
    sys.exit(1)
else:
    print("ALL OK")
