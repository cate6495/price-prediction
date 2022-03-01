import requests

url = 'http://localhost:5000/predict'
r = requests.post(url,json={'Avg. Area Income':79545.4585743167,'Avg. Area House Age':5.68286132161558,'Avg. Area Number of Rooms':7.00918814279223 'Avg. Area Number of Bedrooms':4.09, 'Area Population':23086.8005026864})

print(r.json())