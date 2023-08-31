# ImageAI_Editor
# How to use it
- get your api key from https://deepai.org/
- import request and make a request to the api
```python
r = requests.post(
    "https://api.deepai.org/api/image-editor",
    data={
        'image': img_url,
        'text': text_edit,
    },
    headers={'api-key': 'your_api_key'}
)
```
- you can add some cool stuff too
```python
import requests
img_url = input("Enter img url: ")
text_edit = input("Enter text: ")
r = requests.post(
    "https://api.deepai.org/api/image-editor",
    data={
        'image': img_url,
        'text': text_edit,
    },
    headers={'api-key': 'your_api_key'}
)
data = r.json()
print(data)
```
