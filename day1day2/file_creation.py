import os
from datetime import datetime, timedelta

root_folder = "Folder"

if not os.path.exists(root_folder):
    os.makedirs(root_folder)

def create_date_files(folder_path, year):
    file_name = "new_file.txt"
    start_date = datetime(year, 1, 1)
    end_date = datetime(year + 1, 1, 1)
    current_date = start_date

    with open(file_name, 'r') as file:
        content = file.read()

    while current_date < end_date:
        date_str = current_date.strftime('%Y%m%d')
        file_name = f"{date_str}.txt"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'a') as newfile:
            newfile.write(content)
        current_date += timedelta(days=1)

for city_num in range(1, 101):
    for year in [2023, 2024]:
        folder_path = os.path.join(root_folder, f"city_{city_num}", str(year))
        os.makedirs(folder_path, exist_ok=True)
        create_date_files(folder_path, year)

print("Folders and files created successfully.")