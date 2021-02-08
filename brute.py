import requests
import itertools as it

count = 0
st ="XXXXX"   #Edit string here

comboList = list(map(''.join, it.product(*zip(st.upper(), st.lower()))))
finalList = list(dict.fromkeys(comboList))

for i in range(0,len(finalList)):

	r = requests.get(f'https://img.youtube.com/vi/{finalList[i]}/mqdefault.jpg')

	if r.status_code == 200:
		print(f"FOUND: {finalList[i]} {r.status_code}")
		break
	else:
		print(f"{count} - Bad request: {r.status_code} {finalList[i]}")
		count += 1
