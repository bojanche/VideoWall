from django.conf import settings
import secrets
import os


class FileUtils:
    UPLOAD_DIR = settings.FILE_UPLOAD_DIR

    @classmethod
    def upload_file(cls, file_name, f):
        file_dest = os.path.join(cls.UPLOAD_DIR, secrets.token_hex(4)+'_'+file_name)
        file_url = os.path.join(file_dest, file_name)
        try:
            os.makedirs(file_dest)
        except OSError as e:
            print("Dir exists, although highly unlikely!!!")
        with open(file_url, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return file_url

