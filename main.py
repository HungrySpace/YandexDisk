import requests
import urllib.parse


class YandexDisk:
    def __init__(self, TOKEN, url):
        self.TOKEN = TOKEN
        self.header_auth = {"Authorization": "OAuth " + TOKEN}
        self.url = url

    def create_folder(self, path_folder):
        path_folder_quote = urllib.parse.quote(path_folder)
        params = {"path": path_folder_quote}
        print(params)
        req = requests.get(self.url, headers=self.header_auth, params=params)
        return req


req_yandex_disk = YandexDisk("AgAAAAAUHmUAAAbz6NnEX2O9qEdmjTM0DAt8R6U",
                             "https://cloud-api.yandex.net/v1/disk/resources")
massage = req_yandex_disk.create_folder("/puk")
print(massage)
print(massage.url)
print('https://cloud-api.yandex.net/v1/disk/resources?path=%2Fpuk')
print(massage.json())
