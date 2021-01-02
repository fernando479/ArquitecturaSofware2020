
# Tutorial React.js
## ¿Que es React?

React es una libreria que nos permite a nosotros crear aplicaciones
Al ser una libreria, se puede poner el el html de tu pagina e inmediatamente  empezar a trabajar.

React está hecho para trabajar con aplicaciones de todo tipo de magnitud, ya sea  aplicacicones sencillas, aplicaciones intermedias o aplicaciones robustas 
con alto nivel de interactividad

Esta libreria, al ser declarativa hace facil seguir patrones de diseño y crear interfaces de usuario interactivas

Es increiblemente eficiente, ya que cuendo se hace un cambio y este cambio impacta en el html y hay que volver a renderizarlo, React unicamente 
hace el cambio solo en ese elemento.

Otro punto fuerte es que React trabaja de manera predecible porque toda la informacion fluye en una sola direccion, y esto ayuda a prevenir mutaciones involuntarias e impredecibles

### componentes

Son pequeñas piezas de codigo encapsuladas que pueden tener estados o no y de esta manera, ocn los componentes, se puede "romper" una aplicacion que sea bastante compleja en pequeños componentes o en pequeñas piezas sencillas y faciles de mantenener que permitan mantener el codigo limpio y sencillo


### ¿Como luce un codigo de React?

![](https://raw.githubusercontent.com/fernando479/ArquitecturaSofware2020/main/Tutorial1/image.png)


Esta es la aplicacion mas sencilla que podemos hacer, notemos que la primera linea que tenemos ahí es javaScript puro, que es una constante que mantiene una referencia mediante el querySelector a un elemento del html que tiene el id 'root'

Luego se tiene un objeto llamado ReactDom que tiene un metodo que se llama render. A ese render le estamos mandando  algo que parece html, que es una etiqueta h1 que es un Hola mundo y luego como segundo argumento, se manda el divRoot, es decir, la referencia al elemento donde queremos renderizar o mostrar en pantalla ese contenido de h1, al ejecutar esto tenemos literalmente el resultado que estabamos pensando, un Hola mundo en nuestro navegador web
