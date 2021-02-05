import requests
import time
import random

encontrado = 0
count = 0
while encontrado == 0:

	s = 'AHO95BWZYWW'
	u =''.join(random.random() > 0.5 and x.lower() or x for x in s)
	r = requests.get(f'https://img.youtube.com/vi/{u}/mqdefault.jpg')

	if r.status_code != 404:
		print(f"FOUND: {u} {r.status_code}")
		break
	else:
		print(f"{count} - Bad request: {r.status_code} {u}")
		count += 1