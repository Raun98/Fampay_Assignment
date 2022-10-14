# FAMPAY ASSIGNMENT!

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# Basic Requirements:

- Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of vid eos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.
- Dockerize the project.

# Setup Guide:

- Start by cloning this project to your computer.
- Install dependencies using `pip install -r requirements.txt` in your terminal.
- As the project runs on YouTube's Data v3 API, an API key is required. It can be obtained by [clicking here](https://developers.google.com/youtube/v3/getting-started)
- Navigate to the services.py file, find the settings variable **API_KEYS = [ ... ]**, and adding your __API_KEY__ to this list.
- Open three terminals __parallelly__, on all of them change directory to the YoutubeSearchProject directory. There should be a _manage.py_ file in this folder.
- On one terminal window, run `celery -A YoutubeSearchProject beat -l INFO`
- On the second, run `celery -A YoutubeSearchProject worker -l info -P gevent`
- On the other terminal window, run `python3 manage.py runserver`

Django returns a URL to your local host, follow that to find the dashboard.
# Screenshots:
The Home Page:
![image](https://user-images.githubusercontent.com/71919273/195874880-bc2f9f74-3db0-4cf7-b712-d4bc2d5a28ce.png)
The About Me Page
![image](https://user-images.githubusercontent.com/71919273/195874893-dddde708-f1cd-45e4-b620-6c2a38eb1bfb.png)
The Api with GET + Search
![image](https://user-images.githubusercontent.com/71919273/195874900-c20980c1-c2a9-4091-9f88-6eff827d4bcd.png)
Filters & Ordering
![image](https://user-images.githubusercontent.com/71919273/195874904-31bf066a-0493-4c40-857c-185e5b2f58d8.png)
Search Results for Query - "Neyma"
![image](https://user-images.githubusercontent.com/71919273/195874910-f88708a6-b600-42f0-b8a8-e57c21ec7a92.png)

Thank you for reading! :book: :heart:
