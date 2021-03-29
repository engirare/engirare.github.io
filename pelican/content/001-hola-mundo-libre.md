Title: Hola mundo libre
Date: 2021-03-21 14:20
Modified: 2021-03-28 21:20
Tags: Software libre
Keywords: blog,engirare,pelican,virtualenv,ghp,github,pages 
Category: Cultura y software libre
Author: Engirare
Summary: Aquí batallando con reencontrar mi lado libre y todo eso.. hice una lista de comandos que uso para mi blog (:
Lang: es-MX
Translation: false
Status: published

Y pues, nada, aquí batallando con reencontrar mi lado libre y todo eso, dejaré una lista de comandos útiles por aquí, la edito pronto, cuando esto este mejor organizado:

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

localhost:8000/

git add --all
git commit -m 'aquí va un mensaje'
git push

cd ..
cd ..
git clone --recursive https://github.com/jvanz/pelican-hyde
pelican-themes --install pelican-hyde
pelican-themes --list

dig WWW.EXAMPLE.COM +nostats +nocomments +nocmd
    > ;WWW.EXAMPLE.COM.                     IN      A
    > WWW.EXAMPLE.COM.              3592    IN      CNAME   YOUR-USERNAME.github.io.
    > YOUR-USERNAME.github.io.      43192   IN      CNAME    GITHUB-PAGES-SERVER .
    >  GITHUB-PAGES-SERVER .         22      IN      A       192.0.2.1

$ dig EXAMPLE.COM +noall +answer
> EXAMPLE.COM     3600    IN A     185.199.108.153
> EXAMPLE.COM     3600    IN A     185.199.109.153
> EXAMPLE.COM     3600    IN A     185.199.110.153
> EXAMPLE.COM     3600    IN A     185.199.111.153
~~~~


