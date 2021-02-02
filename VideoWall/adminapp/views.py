from django.shortcuts import render
from django.http import HttpResponse
import logging
from adminapp.forms import FileUpload
from .utils.fileutils import FileUtils
from adminapp.models import Asset

logger = logging.getLogger(__name__)


# Create your views here.


def index(request):
    # logger.error('Something went wrong')
    return render(request, 'adminapp/index.html', {'header': 'Info', 'title': 'Home'})


def video_mgmt(request):
    asset_list = Asset.objects.order_by('created')
    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            creator = "Bojan"
            asset_name = request.POST['title']
            file_name = request.FILES['file'].name
            file_url = FileUtils.upload_file(file_name, request.FILES['file'])
            new_entry = Asset(name=asset_name, path=file_url, creator=creator)
            new_entry.save()
            return render(request, 'adminapp/video_mgmt.html', {'header': 'Video Management',
                                                                'title': 'Video Mangement',
                                                                'form': form,
                                                                'asset_list': asset_list,
                                                                'successful_submit': True})
    else:
        form = FileUpload()
    return render(request, 'adminapp/video_mgmt.html', {'header': 'Video Management', 'title': 'Video Mangement',
                                                        'form': form, 'asset_list': asset_list})

def test_player(request):
    # logger.error('Something went wrong')
    return render(request, 'adminapp/TestPlayer.html', {'header': 'Test Player'})
