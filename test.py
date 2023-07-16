import requests as rek
import json,os,sys

os.system('clear')
logo = """
         Tiktok Downloader
  Author   : TierKun
  Github   : https://github.com/TierGans/
«~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~»\n"""

os.system('clear')
print(logo)
target = input("Link : ")

respon = rek.get('https://api.neoxr.my.id/api/tiktok?url='+target+'&apikey=kyaOnechan')

status = json.loads(respon)["data"]
print(status)
