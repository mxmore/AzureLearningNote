import os
import uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here

except Exception as ex:
    print('Exception:')
    print(ex)


# "NxJHiQw0mYNUoa53Qep/Li2bMalyApOwe/Wwa2k+P47lnbIVTwSEEaUweoFIIb372wcL19mD+8id+AStiYXIdw=="
# azuretestacc03

connection_string = 'DefaultEndpointsProtocol=https;AccountName=azuretestacc03;AccountKey=NxJHiQw0mYNUoa53Qep/Li2bMalyApOwe/Wwa2k+P47lnbIVTwSEEaUweoFIIb372wcL19mD+8id+AStiYXIdw==;EndpointSuffix=core.windows.net'

# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(
    connection_string)


containers = blob_service_client.list_containers()

container_list = list(containers)

container_count = len(container_list)

if container_count == 0:
    print("No containers found, create a container")

    # Create a unique name for the container
    container_name = str(uuid.uuid4())
    # Create the container
    container_client = blob_service_client.create_container(container_name)

    # Create a local directory to hold blob data
    local_path = r'.\data'

    if not os.path.exists(local_path):
        os.makedirs(local_path)

    # Create a file in the local data directory to upload and download
    local_file_name = str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(local_path, local_file_name)

    # Write text to the file
    file = open(upload_file_path, 'w')
    file.write("Hello, World!")
    file.close()

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
    print("--------------------------------")
    print(upload_file_path)
    print("--------------------------------")
    # # Upload the created file
    # with open(upload_file_path, "rb") as data:
    #     blob_client.upload_blob(data)

    # print("\nListing blobs...")

    # List the blobs in the container
    blobs = blob_client.list_blobs()

    blob_list = list(blobs)

    print("\nListing blobs.... length: ", len(blob_list))
    for blob in blobs:
        print("\t" + blob.name)

else:
    print("Containers count: ", container_count)

    for container in container_list:
        print(container.name)
