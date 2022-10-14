import googleapiclient.errors
from googleapiclient.discovery import build
import datetime
from .models import VideoDatabase
query = "football"
url = "https://www.googleapis.com/youtube/v3/search"
API_KEYS = ["AIzaSyC1WItkrEre7bROgCRHw_rohVKwe8WHogk", "AIzaSyBfwzGwhPaCH6q14y3_morZOPmWFPYAj3E"]
maxPerPage=25


def populate_db():
    time_now = datetime.datetime.now()
    time_since_last_search = time_now - datetime.timedelta(minutes=1)
    formatted_time = time_since_last_search.replace(microsecond=0).isoformat()+'Z'
    #print(formatted_time)

    for API_KEY in API_KEYS:
        try:
            youtube = build("youtube", "v3", developerKey=API_KEY)
            search_request = youtube.search().list(part='snippet', q=query, type='video', order='date', maxResults=50,
                                                   publishedAfter=formatted_time)
            search_response = search_request.execute()
            #print("Search ", search_response)
            break
        except googleapiclient.errors.HttpError as error:
            if not (error.resp.status == 400 or error.resp.status == 403):
                break

    #print(search_response)
    try:
        for i in range(50):
            video_id = search_response['items'][i]['id']['videoId']
            title = search_response['items'][i]['snippet']['title']
            description = search_response['items'][i]['snippet']['description']
            publishing_datetime = search_response['items'][i]['snippet']['publishedAt']
            thumbnail_url = search_response['items'][i]['snippet']['thumbnails']['default']['url']
            video_id_list = list(VideoDatabase.objects.values_list('video_id'))
            #print(video_id_list)
            if video_id not in video_id_list:
                print("New Video!")
                VideoDatabase.objects.create(
                    video_id=video_id,
                    title=title,
                    description=description,
                    publishing_datetime=publishing_datetime,
                    thumbnail_url=thumbnail_url,
                )
    except:
        print("Buffering database. Requesting again in 60 seconds.")
