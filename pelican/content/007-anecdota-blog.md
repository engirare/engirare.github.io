---
Title: Anécdota del blog
Date: 2021-04-02 20:00
Modified: 2021-04-02 20:00
Tags: Software libre,Blog
Keywords: persistent,usb,mx,linux,domain,github,pelican,pelican-hyde
Category: Cultura y software libre
Author: Engirare
Summary: Estoy lista para contarte sobre las herramientas que le dan vida a este precioso espacio, espero que mi listado te sea de alguna utilidad (:
Lang: es-MX
Translation: false
Status: draft
---
Lo primero que quiero que sepas es que yo me considero una _usuaria tecnológica básica-media_ (si es que eso existe), pues llevo un tiempo rodeada de amikes de ingeniería en computación y me he logrado empapar de algunos de sus saberes, y al mismo tiempo he cultivado los que me han resultado personalmente útiles. Entre ellas, el control de versiones por medio de git, el uso de herramientas que no son WYSIWYG (_en verdad, ¡me sacan de quicio!_) escapando gracias a latex o markdown, y -por ser del módulo de control en mi universidad- he programado en octave a _quite of interesting things_ aunque _debo confesar que en la premura de entrega de proyectos y falta de tiempo he caído en las seductivas garras de matlab y simulink_ para mis clases de control avanzado y sistemas no lineales. 

A lo que voy con esta última confesión es que: __sí, promuevo el uso de licencias permisivas y procuro las herramientas FOSS, pero no me cierro a ellas de forma tajante__. En mi área lo mejor que pude hacer como estudiante fue revisar con calma las herramientas privativas y comprender la teoría que hay en sus resultados y después -con más tiempo- buscar las opciones libres para llegar a los mismos resultados. Me parece que es una cuestión de practicidad, no es como con kdenlive, inkscape o gimp, que intuitivamente aprendí a utilizar (_y que utilizo de manera muy por encimita, y que vaya, no soy exigente con ellas porque no soy diseñadora_) y que no requerían de que yo entendiera desde antes qué esperaba ver para saber si las estaba usando correctamente (como me ocurrió en un software de flujos de potencia eléctrica). Me di cuenta que no me podía poner a desarrollar software para cada necesidad que tenía como ingeniera eléctrica (porque tengo prioridades y no es la línea que decidí seguir) y debo admitir que aunque muchas veces me ha resultado desesperante que las cosas no funcionen _magicamente_ a la primera (una pared con la que topas sí o sí tan pronto empiezas a usar FOSS) __considero que es necesario que entendamos y nos apropiemos de la tecnología tanto como podamos y en la medida que mejor nos funcione para realizar nuestras actividades de manera _fluida_.__ Y claro, con la experiencia crece la _fluidez_, y con esto me refiero a que, para mí fue un obstáculo el estar en el proceso de entender qué requiería del software y por qué y al mismo tiempo intentar migrar, _ni migraba ni me concentraba en lo que tenía que aprender en mis clases_ por eso ahora soy más flexible y creo que se vale empezar como una _begginer_ que busca ser _advanced_ __y poco a poco enmanciparnos de las herramientas privativas y desarrollarnos en entornos cada vez más abiertos y libres__ (que bueno, aquí quiero aclarar que estoy sacando de la ecuación un montón de factores que pienso seguir investigando y reflexionando para abordar en notas posteriores, te prometo que procuro que mis privilegios no dejen ciega y que estoy consciente de que está discusión tiene muchas más ramas).

Una vez hecho mi _disclaimer_ y contextualizando un poco mi situación, estoy lista para contarte sobre las herramientas que le dan vida a este precioso espacio, espero que mi listado te sea de alguna utilidad (:

### Github pages

[GitHub Pages](https://www.alejandrolopezparra.es/post/github_pages/) es un servicio de alojamiento web estático ofrecido por GitHub para alojar blogs de usuarias, documentación de proyectos, o incluso libros enteros creados como una página. Decidí hacerlo por este medio porque llevo siendo usuaria de GitHub hace un tiempo, y la idea me parecia cómoda, de hecho puedes consultar [el repositorio fuente de este blog](https://github.com/engirare/engirare.github.io). Para que se viera más _pro_ mi página, me compré un dominio y seguí las instrucciones que encontré en una página para configurar el dominio que adquirí (voy a buscar el link exacto del tutorial que seguí, pero justo ahora no lo encuentro).

### Pelican y herramientas asociadas

Ahora, necesitaba un generador de sitios web estáticos, y aunque estaba la opción de usar Jekyll, tenía ganas de explorar Pelican por [unos tutoriales que vi](https://penserbjorne.com/pelican-01-creacion-de-un-blog-estatico-con-pelican-es-MX.html), tengo que decir que la parte más tormentosa fue darme cuenta que el entorno de `virtualenv` se creaba por default con una versión de python distinta a la que necesitaba y en [esta nota](https://engirare.com/hola-mundo-libre-es-MX.html) puedes ver el comando que encontré para corregirlo.

Otro _issue_ fue la elección del tema, después de intentar personalizar los colores de dos temas que me gustaron (y que evidentemente fallé en el intento, porque mis conocimientos básicos de css no fueron suficientes) encontré __la joyita__ que estoy usando: [__pelican-hyde__](https://github.com/jvanz/pelican-hyde) y que tiene todo lo que pedí, un espacio hermoso y limpio, y que fue fácil de configurar en el color que yo quería (:

### MX Linux

La historia más larga es la del sistema operativo que utilizo, por la pandemia, me quedé sin computadora personal, pero tengo acceso a múltiples computadores -que no me pertenecen- en el lugar donde me encuentro. La solución fue usar una vieja usb de 4 Gb con un sistema portable, tenía ganas de explorar nuevos SOs y me encontré con [Peppermint OS](https://peppermintos.com/) que me gustó mucho, el detalle fue que cada vez tenía que volver a instalar todo y aunque al principio no me importaba, con los días se volvió incómodo. Así que decidí aventurarme a hacer una usb persistente y me permití otra de 16 Gb en la que animadamente comencé a probar y _la nación del fuego atacó_. Los tutoriales rápidos que encontraba no funcionaban, llegué a ver unos que manejaban terminología que requería ponerse a investigar y honestamente no me sentía con suficiente tiempo para hacerlo en ese momento, finalmente encontré uno con el que tenía mucha esperanza que usaba [Ventoy](https://ostechnix.com/create-persistent-bootable-usb-using-ventoy-in-linux/) y fallé. 

Pero, usar Ventoy me hizo notar algunas cosas en su menu y me pareció que había SOs que tenían ¿mejor adecuación? (_algo así_) para el tema de la persistencia y eso me dio el hint para encontrar el [Top 3 USB Persistent Linux Distros](https://embeddedinventor.com/top-3-usb-persistent-linux-distros-comparison-analysis/), bastó con leer la introducción para tranquilizarme de que las cosas no salían, realmente hasta ese punto, ninguna de las páginas que había consultado mencionaban el tamaño de la usb, incluso vi tutoriales con usbs del mismo tamaño que la mía, _btw_ finalmente me encontré _al avatar_ [aquí](https://www.techsolveprac.com/persistent-portable-mx-linux/) sólo que, en la versión actual de MX Linux en el _Paso 6_ tuve que configurar ligeramente diferente (no te preocupes, lo dejé documentado).

### ExifTool

Es la herramienta que utilizo para manipular metadatos de las imágenes aunque [no sólo es para imagénes](https://exiftool.org/) y mantener mi preciada [privacidad](https://www.xataka.com/basics/que-son-y-como-borrar-los-metadatos-de-una-foto-en-windows-10).

 
Y pues, esa es la historia de las herramientas que utilizo para el blog, como puedes darte cuenta, la elección de mis herramientas está bastante sesgada por lo que a mí en lo personal me resulta útil, es decir, busco utilizar el conocimiento que ya poseo y al mismo tiempo, intento procurar entornos más libres y abiertos, y espero con esta anécdota animarte a ti, mi lectora, a que me acompañes en este _camino ninja_.
