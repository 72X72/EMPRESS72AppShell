from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials

def upload_monetize(video_path, title, description, tags):
    print("[EMPRESS72] 🎬 Uploading cinematic override to Empress72 channel")

    # Authenticate with YouTube Data API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'empress72_youtube_credentials.json',
        scopes=['https://www.googleapis.com/auth/youtube.upload']
    )
    youtube = build('youtube', 'v3', credentials=credentials)

    # Upload video
    request = youtube.videos().insert(
        part='snippet,status',
        body={
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags,
                'categoryId': '24'  # Entertainment
            },
            'status': {
                'privacyStatus': 'public',
                'license': 'youtube',
                'embeddable': True
            }
        },
        media_body=MediaFileUpload(video_path)
    )
    response = request.execute()

    print(f"[EMPRESS72] ✅ Uploaded and published: {response['id']}")
