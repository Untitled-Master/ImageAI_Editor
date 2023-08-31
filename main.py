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
