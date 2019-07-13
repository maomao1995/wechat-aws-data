# coding:utf-8
from django.http import HttpResponse
from wechat import tools
import json

text_path = '/home/ubuntu/wechat/text/'
image_path = '/home/ubuntu/wechat/image/'
secret = 'jd'


def get_text_data(request):
    user_secret = request.GET.get('secret')
    if user_secret == secret:
        file_paths = tools.get_path(text_path)
        text_data = {}
        for file_path in file_paths:
            file_text = tools.get_file_text(text_path + "/" + file_path)
            text_data[file_path] = file_text
        json_str = json.dumps(text_data)
        return HttpResponse(json_str)
    else:
        return HttpResponse('secret不正确')


def del_text_data(request):
    user_secret = request.GET.get('secret')
    file_path_str = request.GET.get('file_path_str')
    if user_secret == secret:
        file_paths = file_path_str.split(",")
        for file_path in file_paths:
            tools.del_file(text_path + "/" + file_path)
