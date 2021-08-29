import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    #var1 refers to file_from, var2 refers to file_to
    def upload_file(self, var1, var2):
        dbx = dropbox.Dropbox(self.access_token)
        with open(var1, 'rb') as f:
            dbx.files_upload(f.read(), var2)

def main1():
    access_token = 'FvD6XZi72isAAAAAAAAAAQGnSReLn7l-VOSKHJWS1nPVG02NkKm3aV-UkHVLq2lW'
    object1 = TransferData(access_token)

    file_from = input('Enter the file path to transfer: ')
    file_to = input('Enter the full path to upload to dropbox: ')

    object1.upload_file(file_from, file_to)
    print('File transfered!')

if __name__ == '__main__':
    main1()