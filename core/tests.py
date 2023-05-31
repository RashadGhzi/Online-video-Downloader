import youtube_dl
from django.http import JsonResponse

def get_video_details(request):
    url = "https://youtu.be/ud5pjeX-2RU"

    ydl_opts = {
        'format': 'best',
        'simulate': True,
        'quiet': True,
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            video_info = ydl.extract_info(url, download=False)
            
            vid_title = video_info.get('title')
            vid_thumbnail = video_info.get('thumbnail')
            duration = video_info.get('duration')
            resolution_1080p = None

            for format_ in video_info.get('formats', []):
                if format_.get('vcodec') == 'none':
                    continue
                resolution = format_.get('height')
                if resolution == 1080:
                    resolution_1080p = format_.get('url')
                    print(resolution_1080p)
                    break

            context = {
                'vid_title': vid_title,
                'vid_thumbnail': vid_thumbnail,
                'duration': duration,
                'resolution_1080p': resolution_1080p
            }

            return JsonResponse(context)
    except Exception as e:
        return JsonResponse({'msg': 'Error fetching video details.', 'error': str(e)})
