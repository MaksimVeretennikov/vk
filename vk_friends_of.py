def friends_of(user_id):
    URL = "https://api.vk.com/method/"
    access_token = 'f941d885056cf62dfdc70b12f7cc67cb2ee92f748267e629ca783041c948f139943605acf59d68f766089'
    #сам запрос
    response = urllib.request.urlopen(URL + 'friends.get?user_id=' + user_id + '&order=hints' + '&fields=nickname' + '&v=5.80&access_token=' + access_token)
    #преобразуем в json формат и в словарь
    json_m = response.read().decode('utf-8')
    data = json.loads(json_m)
    friends_ids = []
    if 'response' in data:
        for i in data['response']['items']:
            friends_ids.append(i['id'])
    elif 'error' in data:
        print(data['error']['error_msg'])
    else:
        print("Что-то пошло не так...")
    return friends_ids
