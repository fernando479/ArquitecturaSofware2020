
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

![](https://raw.githubusercontent.com/fernando479/ArquitecturaSofware2020/main/Tutorial_6_react/image.png)


Esta es la aplicacion mas sencilla que podemos hacer, notemos que la primera linea que tenemos ahí es javaScript puro, que es una constante que mantiene una referencia mediante el querySelector a un elemento del html que tiene el id 'root'

Luego se tiene un objeto llamado ReactDom que tiene un metodo que se llama render. A ese render le estamos mandando  algo que parece html, que es una etiqueta h1 que es un Hola mundo y luego como segundo argumento, se manda el divRoot, es decir, la referencia al elemento donde queremos renderizar o mostrar en pantalla ese contenido de h1, al ejecutar esto tenemos literalmente el resultado que estabamos pensando, un Hola mundo en nuestro navegador web

![](https://raw.githubusercontent.com/fernando479/ArquitecturaSofware2020/main/Tutorial_6_react/Selection_001.png)


Para comprender mejor,  el codigo que tenemos acá, lo vamos a separar  en una variable  para que lo miremos mejor y lo analicemos

![](https://raw.githubusercontent.com/fernando479/ArquitecturaSofware2020/main/Tutorial_6_react/Selection_002.png)

![](https://raw.githubusercontent.com/fernando479/ArquitecturaSofware2020/main/Tutorial_6_react/Selection_003.png)

Ese h1Tag se lo estamos mandando al metodo render de ReactDom, el cual lo crea en el HTML, lo demas sigue siendo lo mismo, la referencia al html y el metodo que vamos a llamar para renderizar algo, ese "algo" sera un *componente*
Lo interesante aqui es que estamos asignando a nuestra constante el valor de una etiqueta html

![](https://raw.githubusercontent.com/fernando479/ArquitecturaSofware2020/main/Tutorial_6_react/Selection_004.png)

Esta mezcla que tenemos en pantalla es conocida como JSX que no es más que javaScript más XML, perfectamente nosotros podriamos escribir todo el codigo sin usar esa etiqueta usando codigo en javaScript, como lo muestra la siguiete imagen

![](https://raw.githubusercontent.com/fernando479/ArquitecturaSofware2020/main/Tutorial_6_react/Selection_005.png)

Pero toda esa linea de codigo es el equivalente a esa creacion de la etiqueta directamente explicita en JSX, haciendo uso de JSX simplifica el codigo de una manera eficiente al usar simple etiquetas en el lado de JS.
  
Al ejecutar esto se tiene el mismo resultado anterior

**create React App**

Create React App es un ambiente cómodo para aprender React, y es la mejor manera de comenzar a construir una nueva aplicación de página única usando React

Create React App configura nuestro ambiente de desarrollo de forma que se usar las últimas características de Javascript, brindando una buena experiencia de desarrollo, y optimizando tu aplicación para producción. Necesitaremos tener Node >= 8.10 y npm >= 5.6 instalados en la máquina. Para crear un proyecto podemos ejecutar:

```
npx create-react-app my-app
cd my-app
npm start
```

Podemos abrir en nuestro editor de codigo favorito la carpeta creada que contiene los archivos para empezar a trabajar en React! 

![](https://raw.githubusercontent.com/fernando479/ArquitecturaSofware2020/main/Tutorial_6_react/Selection_006.png)
