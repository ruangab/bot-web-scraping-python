import requests
import re
import json
r = requests.get("https://g1.globo.com/")
html = r.text



titulos = re.finditer(r'<div class="feed-post-body-title gui-color-primary gui-color-hover "><div class="_ee"><a href="(?:.*?)">(?P<titulo>.*?)<\/a><\/div><\/div>', html, flags=re.DOTALL) 


jsontitulos = []

for titulo in titulos:
	json_noticia = {
		'titulo':titulo.group('titulo')
	}

	jsontitulos.append(json_noticia)

json_final = json.dumps(jsontitulos, indent = 4, sort_keys = False, ensure_ascii=False)

print(json_final)