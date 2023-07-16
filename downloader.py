import requests as rek
import json,os,sys

os.system('clear')
logo = """
         Spam Telepon / Call
  Author   : TierKun
  Github   : https://github.com/TierGans/

          Contoh Penggunaan:
  = https://vt.tiktok.com/ZSJ7CgDUC
«~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~»\n"""

os.system('clear')
print(logo)
target = input(" Link Tiktok : ")
#apikey = input(" Apikey : ")


api_url = "https://api.neoxr.my.id/api/tiktok?url="+target+"&apikey=kyaOnechan"
#respon = rek.get(api_url).text
r = rek.get(api_url)
print(r.json())

#status = json.loads(respon)
#print(status)
"""
if status == "Request misscall berhasil":
     print("\n {✓} Spam Call / Telepon Untuk No "+ target +" Berhasil \n")
else:
     print("\n {×} Spam sudah dilakukan 3x » Gagal \n")
     """