import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from django.conf import settings

# 1. Load the "Robot" credentials
creds = service_account.Credentials.from_service_account_file(
    settings.SERVICE_ACCOUNT_FILE, scopes=settings.SCOPES)
# 2. Build the Service
# This is the core service for the google drive API service
DriveService = build('drive', 'v3', credentials=creds)


def test_drive():
    
    # List files in your specific Master Folder
    
    query = f"'{settings.DEFAULT_FOLDER_ID}' in parents"
    
    results = DriveService.files().list(q=query, fields="files(id, name)").execute()
    items = results.get('files', [])
    
    for item in items:
        print(f"Found: {item['name']} (ID: {item['id']})")


def download_file(file_id:str,type=None):
            """
            This function streams a file as bytes and  
            yeilds(generator) it in small chunks.
            """
            request = DriveService.files().get_media(fileId=file_id)
            # Use a small internal buffer for the current chunk
            chunk_buffer = io.BytesIO()
            # 1MB chunks are a good balance for PythonAnywhere
            downloader = MediaIoBaseDownload(chunk_buffer, request, chunksize=1024*1024)
            
            done = False
            while not done:
                status, done = downloader.next_chunk()
                # Yield the data currently in the buffer
                yield chunk_buffer.getvalue()
                # Clear the buffer for the next chunk to save RAM
                chunk_buffer.seek(0)
                chunk_buffer.truncate(0)

def search(query:str,filter=None):
    ...

def search_drive_materials(service, query_text=None, folder_id=None, mime_type=None):
    """
    A logic-only function to query Google Drive.
    Returns a list of dictionaries containing file metadata.
    """
    query_parts = ["trashed = false"]

    # 1. Scope by Folder (if provided)
    if folder_id:
        query_parts.append(f"'{folder_id}' in parents")

    # 2. Filter by Name (Partial match)
    if query_text:
        # Note: 'contains' is case-insensitive for names in Drive API
        query_parts.append(f"name contains '{query_text}'")

    # 3. Filter by MIME Type (e.g., 'application/pdf')
    if mime_type:
        query_parts.append(f"mimeType = '{mime_type}'")

    # Join all parts with AND logic
    final_query = " and ".join(query_parts)

    try:
        results = []
        page_token = None
        
        while True:
            # We use fields to limit the data coming back over the wire
            # 'nextPageToken' handles cases where there are 100+ files
            response = service.files().list(
                q=final_query,
                spaces='drive',
                fields='nextPageToken, files(id, name, mimeType, size, modifiedTime)',
                pageToken=page_token,
                pageSize=100
            ).execute()
            
            results.extend(response.get('files', []))
            page_token = response.get('nextPageToken')
            
            if not page_token:
                break
                
        return results

    except Exception as e:
        # Log the error in your Django logs
        print(f"An error occurred during Drive search: {e}")
        return []
