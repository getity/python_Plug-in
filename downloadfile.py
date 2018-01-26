import requests

def downloadfile(name,url):
	name=name+".mp4"
	r=requests.get(url)
	f=open(name,'wb');
	iter = r.iter_content(chunk_size=255)
	i=0
	while i<5000:
		f.write(next(iter))
		i+=1	
	f.close()

downloadfile('ffff','https://file.tvsou.com/f/b2fa5238166d')
