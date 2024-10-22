from azure.storage.blob import BlobServiceClient


def uploadToBlobStorage(file_path,file_name,container_name):
    try:
     connection_string = 'sua string de conexão'
     blob_service_client = BlobServiceClient.from_connection_string(connection_string)
     blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
     with open(file_path,"rb") as data:
        blob_client.upload_blob(data, overwrite=True)
        print(f"Uploaded {file_name}.")
    except:
     print("Não consegui fazer upload do arquivo", file_name)    
     return False
    return True