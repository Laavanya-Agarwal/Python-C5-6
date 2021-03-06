import os
import dropbox 
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                # local path
                local_path = os.path.join(root, filename)
                # dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main1():
    access_token = 'eIXp5m3ylqMAAAAAAAAAAR_0jwpVSC0Cdrk7r7K6ppmz4kpze_JRnDCm9BXNcsfm'
    object1 = TransferData(access_token)

    file_from = input('Enter the file path to transfer: ')
    file_to = input('Enter the full path to upload to dropbox: ')

    object1.upload_file(file_from, file_to)
    print('File transfered!')

if __name__ == '__main__':
    main1()
