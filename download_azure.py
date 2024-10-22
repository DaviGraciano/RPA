from azure.storage.blob import BlobServiceClient
import os

def downloadFromBlobStorage(file_name, file_path, container_name):
    try:
    
     connection_string = 'Sua string de conexão'
     
     blob_service_client = BlobServiceClient.from_connection_string(connection_string)
     blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
     with open(file=os.path.join(file_path, file_name), mode="wb") as data:
        download_stream = blob_client.download_blob()
        data.write(download_stream.readall())
     print(f"Downloaded {file_name}.")   
    except:
    
     print("Não consegui baixar o arquivo ou arquivo não encontrado", file_name)    
     return False
    return True