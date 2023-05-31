from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import Vid_Url
from pytube import YouTube
import json
# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/home.html')

class Facebook(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/facebook.html')
    
    
url_obj = {}
class Youtube(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/youtube.html')

    def post(self, request):
        url = request.POST['url']
        url_obj['url'] = url
        # print(url)
        try:
            video = YouTube(url)
            vid_title = video.title
            video_length = video.length
            duration_formatted = str(video.length // 60) + ':' + str(video.length % 60)  # Formatted duration as mm:ss
            # print(vid_title)
            vid_thumbnail = video.thumbnail_url
            quality = []

            for vid in video.streams.filter(progressive=True):
                quality.append(vid.resolution)
            
            context = {'vid_title':vid_title, 'vid_thumbnail':vid_thumbnail,'quality':quality, 'duration_formatted':duration_formatted}
            return JsonResponse(context)
        except Exception as e:
            print(e)
            return JsonResponse({'msg': 'error', 'error': str(e)})

def vid_download(request):
    # print(url_obj)
    # print(request.GET)
    id = request.GET.get('id')
    # print(id)
    video = YouTube(url_obj['url'])
    stream = video.streams[int(id)]
    stream.download(output_path='./Downloads')
    return JsonResponse({'msg':'video downloading'})