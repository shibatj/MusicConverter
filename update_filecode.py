import sqlite3
import os

def update_filecodes(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # ดึงข้อมูลทั้งหมดจากตาราง
    cursor.execute("SELECT filepath FROM tbfiles")
    rows = cursor.fetchall()

    # อัปเดต filecode สำหรับแต่ละแถว
    for row in rows:
        filepath = row[0]
        filecode = os.path.basename(filepath)  # ใช้ os.path.basename เพื่อดึงชื่อไฟล์
        cursor.execute("UPDATE tbfiles SET filecode = ? WHERE filepath = ?", (filecode, filepath))

    conn.commit()
    conn.close()

# ใช้ฟังก์ชัน
db_path = 'Music_Database.db'
update_filecodes(db_path)
