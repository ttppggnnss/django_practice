from django.shortcuts import render
# Create your views here.

def index(request):
    import datetime
    today=datetime.datetime.now()
    context={
        'today':today
    }
    return render(request, 'index.html',context)

def gallery(request):
    # 1. Access Key 붙여넣기
    client_id = '4Yi9QTOdW2bvZtGa5CPRt-lEqQhyY-OKQz1fk6eo9wY'
    # 2. Form 데이터 가져오기 (설정한 name 속성값 -> search)
    search_data = request.GET.get('search')
    # 3. 요청 보내기
    photo_url=f'https://api.unsplash.com/search/photos?query={search_data}&client_id={client_id}'
    import requests
    response = requests.get(photo_url).json()
    photo_list = []
    for photo in response.get('results'):
        photo_list.append(photo.get('urls').get('regular'))
    context = {
        'search_data':search_data,
        'photo_list':photo_list,
    }
    import pprint
    # pprint(photo_list)
    return render(request, 'gallery.html',context)
