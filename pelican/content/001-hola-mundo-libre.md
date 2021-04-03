---
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
---
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

# show metadata of a image file
exiftool myPhoto.jpg

# remove all metadata of all *jpg files in current dir
exiftool -all= -overwrite_original -ext jpg .

# remove all metadata of a image file
exiftool -all= -overwrite_original photo.jpg

# remove all GPS metadata of *jpg files in current dir
exiftool -gps:all= *.jpg

~~~~


_____
##### i. Language

Either choose language as per your preference or press ‘1’ to proceed with default

##### ii. Number of console columns

Either choose number of console columns as per your preference or press ‘1’ to proceed with default

##### iii. Time zone

Either choose time zone as per your preference or press ‘1’ to proceed with default

##### iv. Other Options

<del> Specifically choose ‘5’ – ‘from=usb’ to Finish Booting from a LiveUSB </del>

Aquí, en la versión que yo descargué, estaba en la opción ‘7’

##### v. Persistence Option

<del> Specifically choose ‘2’ – ‘persist_all’ to save root and home </del>

Esta fue la opción que más lata me dio. En la versión más reciente al elegir la opción ‘persist all’ cuando se tiene que crear el `roots file` te dice que no puede hacerlo  x_x. 


![why?]({attach}/images/rootMX.jpg)

 Yo probé varías opciones y de mis pruebas finalmente al elegir la opción ‘persist root’ fue la que me funcionó. Sigo sin entender por qué los archivos se guardan si por el menú yo entendí que los archivos en home se iban a borrar. _Nota mental: revisar en cuanto sea posible con mis amikes._

##### vi. Font Size

Either choose font size as per your preference or press ‘1’ to proceed with default

##### vii. Create rootfs file

<del> Specifically choose ‘1’ – ‘create automatically’. Wait for the rootfs file to be created. </del>

En mis pruebas nunca funcionó, lo que me funcionó fue dar la opción 2, y elegir el valor más alto que me permitía.

##### viii. Create homefs file

<del> Specifically choose ‘1’ – ‘create automatically’. Wait for the homefs file to be created. </del>

Esto nunca ocurrio en la opción de persistencia que elegí.

##### ix. Save these changes

Specifically choose ‘1’ – ‘Yes’ to save the changes made to the boot configuration.

Al guardar me pregunto si quería hacer `swipe`, en dos ocasiones yo di que sí, y el sistema se volvió la cosa más lenta del mundo. En la ocasión que dije que no, eso no ocurrió, leyendo el manual de MX Linux, en una parte mencionan que con esa opción se vuelven más lentos los discos, yo se lo atribuyo, pero no sé explicar por qué. _Nota mental: revisar en cuanto sea posible con mis amikes._
 

##### x. Change ‘root’ user password

Type and re-type a new and secure password to change the default root user password.

##### xi. Change ‘demo’ user password

Type and re-type a new and secure password to change the default demo user password.

##### xii. Auto Save Mode

Specifically choose ‘1’ – ‘Automatic’ to save on shutdown/ reboot automatically without need to ask for saving data every time.

Yo aquí elegí la opción semi-automatica, pero sigo evaluando si mejor lo cambio a automática.

Finally, the MX Linux persistent session will load from Flash Drive.
____

