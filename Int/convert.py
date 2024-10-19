import requests
import json
def Image(k):
  response = requests.request(
    'POST',
    'https://api.pspdfkit.com/build',
    headers = {
      'Authorization': 'Bearer pdf_live_Y2Zw7KuNf90bmQLZxg4mqsayAyu30I7KlUEEqc8R9wx'
    },
    files = {
      'document': k
    },
    data = {
      'instructions': json.dumps({
        'parts': [
          {
            'file': 'document'
          }
        ],
        'output': {
          'type': 'image',
          'format': 'jpg',
          'dpi': 500
        }
      })
    },
    stream = True
  )
  #if response.ok:
  with open("media/"+k.name.split(".")[0]+".jpg", 'wb') as fd:
      for chunk in response.iter_content(chunk_size=8096):
        fd.write(chunk)
  return response.status_code
