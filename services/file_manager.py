import json
from pathlib import Path
from datetime import datetime


class FileManager:
    """Class khusus untuk menyimpan dan membaca data JSON."""

    def __init__(self, folder_data="data"):
        self.folder_data = Path(folder_data)
        self.folder_data.mkdir(exist_ok=True)

    def _path(self, nama_file):
        return self.folder_data / nama_file

    def simpan_json(self, nama_file, data):
        with open(self._path(nama_file), "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def baca_json(self, nama_file, default=None):
        path = self._path(nama_file)
        if not path.exists():
            return default if default is not None else []
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def backup_json(self, nama_file):
        path = self._path(nama_file)
        if not path.exists():
            return None
        backup_folder = self.folder_data / "backup"
        backup_folder.mkdir(exist_ok=True)
        waktu = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = backup_folder / f"{path.stem}_{waktu}{path.suffix}"
        backup_path.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
        return backup_path
