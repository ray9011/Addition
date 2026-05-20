import zipfile
import os

# 資料夾路徑（來源）
src_folder = r"\\GeminiNTUT\Lab412\Dataset\Lithium-ion battery aging dataset based on electric vehicle real-driving profiles"

# 壓縮後儲存位置（目標 ZIP 檔案）
dst_zip = r"D:\Data\battery_dataset.zip"

# 建立 ZIP 檔（不壓縮內容，加快速度）
with zipfile.ZipFile(dst_zip, 'w', compression=zipfile.ZIP_STORED) as zipf:
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, src_folder)  # 相對路徑放入 ZIP
            zipf.write(file_path, arcname)

print("✅ 壓縮完成！儲存在：", dst_zip)
