import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFile(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(fileFrom,'rb')
        dbx.files_upload(f.WriteMode(‘overwrite’),fileTo)

def main():
    access_token=''
    transferData=TransferData(access_token)
    fileFrom=input('Enter the file path to transfer')
    fileTo=input('Enter the full path to upload to dropbox')
    transferData.uploadFile(fileFrom,fileTo)
    print('File has been moved')

main()