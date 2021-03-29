Title: Hola mundo libre
Date: 2021-03-21 14:20
Category: Software Libre

Y pues, nada, aquí batallando con reencontrar mi lado libre y todo eso, dejaré una lista de comandos útiles por aquí, la borro pronto, cuando esto este mejor organizado:

 	

~~~~

sudo apt-get update
sudo apt-get upgrade

sudo apt install virtualenv

virtualenv -p python3 try
cd try
source bin/activate
python --version
sudo apt install python-pip
pip install pelican Markdown typogrify
pip install --upgrade pelican Markdown typogrify

sudo apt install git
git clone https://github.com/engirare/engirare.github.io
git config --global user.name "engirare"
git config --global user.email "engirare@tutanota.com"

cd engirare.github.io

git status

cd pelican

pelican content -o ..
pelican --listen -o .. 

http://localhost:8000/

git add --all
git commit -m 'aquí va un mensaje'
git push

cd ..
cd ..
git clone --recursive 
https://github.com/jvanz/pelican-hyde
pelican-themes --install pelican-hyde
pelican-themes --list
~~~~


