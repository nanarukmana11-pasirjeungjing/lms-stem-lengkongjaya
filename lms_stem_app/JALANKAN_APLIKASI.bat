@echo off
cd /d "%~dp0"
echo === Memasang dependensi (streamlit, python-docx) ===
pip install -r requirements.txt
echo.
echo === Menjalankan aplikasi LMS STEM ===
echo Browser akan terbuka otomatis. Biarkan jendela ini tetap terbuka selama memakai aplikasi.
echo Tutup jendela ini (atau tekan Ctrl+C) untuk mematikan aplikasi.
echo.
streamlit run app.py
pause
