import sqlite3
import shutil
import os

# ตั้งค่าการเชื่อมต่อฐานข้อมูล
db_path = 'Music_Database.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# ตั้งค่าโฟลเดอร์ปลายทาง
destination_folder = 'E:\\Sound'

# อ่านที่อยู่ไฟล์จากฐานข้อมูล
cursor.execute("SELECT filepath FROM tbfiles")
rows = cursor.fetchall()

# วนลูปเพื่อคัดลอกไฟล์
for row in rows:
    file_path = row[0]
    if os.path.exists(file_path):
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.copy(file_path, destination_path)
        print(f"Copied {file_path} to {destination_path}")
    else:
        print(f"File not found: {file_path}")

# ปิดการเชื่อมต่อฐานข้อมูล
conn.close()