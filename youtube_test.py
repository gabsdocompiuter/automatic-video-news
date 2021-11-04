from datetime import datetime

from youtube_manager import create_service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'credentials/google-secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']


def main():
    service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    upload_date_time = datetime.now().isoformat() + '.000Z'

    print(upload_date_time)

    request_body = {
        'snippet': {
            'categoryI': 19,
            'title': 'Upload Testing',
            'description': 'Description',
            'tags': ['Travel', 'video test', 'Travel Tips']
        },
        'status': {
            'privacyStatus': 'unlisted',
            # 'publishAt': upload_date_time,
            'selfDeclaredMadeForKids': False,
        },
        'notifySubscribers': False
    }

    mediaFile = MediaFileUpload('outputs/test.mp4')

    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()

    print(response_upload)

    # service.thumbnails().set(
    #     videoId=response_upload.get('id'),
    #     media_body=MediaFileUpload('temp/thumbnail.png')
    # ).execute()


if __name__ == '__main__':
    main()
