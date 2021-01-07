## Redis

### ¿Que es Redis?


Redis(Remote Dictionary Serve) es un rapido alamacen de dato clave-valor en memoria de código abierto que se puede utilizar como base de datos, caché, agente de mensajes y cola. Redis ofrece tiempos de respuesta inferiores al milisegundo, lo que permite que se realicen millones de solicitudes por segundo para aplicaciones en tiempo real de videojuegos, tecnología publicitaria, servicios financieros, sanidad e IoT. Redis es una opción muy habitual en aplicaciones de almacenamiento en caché, administración de sesiones, videojuegos, tablas de clasificación, análisis en tiempo real, datos geoespaciales, servicios de vehículos compartidos, chat/mensajería, streaming de contenido multimedia y publicación/suscripción.


### ¿como funciona Redis? 

Todos los datos de Redis residen en la memoria, a diferencia de las bases de datos que almacenan datos en discos o SSD. Como no hay ninguna necesidad de obtener acceso al disco, los almacenes de datos en memoria, como Redis, evitan los retrasos y pueden obtener acceso a los datos en cuestión de milisegundos. Redis incluye estructuras de datos versátiles, alta disponibilidad, datos geoespaciales, scripts Lua, transacciones, persistencia en disco y soporte de clúster, lo que simplifica la creación de aplicaciones a escala de Internet en tiempo real.

### beneficios de redis

**Almacén de datos en memoria**

Todos los datos de Redis residen en la memoria principal del servidor, a diferencia de bases de datos como PostgreSQL, Cassandra, MongoDB, entre otras, que almacenan la mayor parte de los datos en discos o SSD. En comparación con las bases de datos tradicionales basadas en disco, donde la mayoría de las operaciones implican ir y volver al disco, los almacenes de datos en memoria como Redis no se ven afectados de la misma manera. Por lo tanto, pueden admitir una orden de magnitud, más operaciones y tiempos de respuesta más rápidos. El resultado es rendimiento increíblemente rápido con operaciones de lectura o escritura promedio que se ejecutan en menos de un milisegundo y capacidad para procesar millones de operaciones por segundo.


**Estructuras de datos flexibles**
  
A diferencia de los almacenes de datos de clave valor simplistas que ofrecen estructuras de datos limitadas, Redis cuenta con una amplia variedad de estructuras de datos para satisfacer los requisitos de sus aplicaciones. Los tipos de datos de Redis incluyen:

  - Cadenas: datos de texto o binarios de hasta 512 MB de tamaño
  - Listas: una colección de cadenas en el orden en que se agregaron
  - Conjuntos: una colección desordenada de cadenas con la capacidad para intercalarse, unirse y diferenciarse de otros tipos de conjuntos
  Conjuntos ordenados: conjuntos ordenados por un valor
  - Hashes: una estructura de datos para almacenar una lista de campos y valores
  - Mapas de bits: un tipo de datos que ofrece operaciones a nivel de bits
  - HyperLogLogs: una estructura de datos probabilísticos para estimar los elementos únicos en un conjunto de datos
 
 **Simplicidad y facilidad de uso**
  
Redis simplifica el código porque le permite escribir menos líneas de código para almacenar, obtener acceso y utilizar datos en sus aplicaciones. Por ejemplo, si su aplicación tiene datos almacenados en un hashmap y desea almacenarlos en un almacén, puede usar la estructura de datos hash de Redis para hacerlo. Una tarea de similares características en un almacén de datos sin estructuras de datos hash necesitaría muchas líneas de código para realizar la conversión de un formato a otro. Redis incluye estructuras de datos originales y muchas opciones para trabajar e interactuar con ellos. Los desarrolladores de Redis tienen a su disposición más de cien clientes de código abierto. Entre los lenguajes admitidos se encuentran Java, Python, PHP, C, C++, C#, JavaScript, Node.js, Ruby, R, Go y muchos otros.

**Replicación y persistencia**

Redis utiliza una arquitectura con servidor principal y réplica y admite la replicación asíncrona en la que los datos se replican en numerosos servidores de réplicas. De este modo, se logra un mejor nivel de rendimiento de lectura (ya que las solicitudes se pueden repartir entre varios servidores) y menores tiempos de recuperación cuando el servidor principal sufre un corte. Por una cuestión de persistencia, Redis admite copias de seguridad puntuales (copia el conjunto de datos Redis en el disco).

**Alto nivel de disponibilidad y escalabilidad**
  
Redis ofrece una arquitectura con servidor principal y réplica en una topología en clústeres o principal con un único nodo. Esto permite crear soluciones con un alto nivel de disponibilidad, lo que ofrece fiabilidad y rendimiento estables. Cuando se necesita ajustar el tamaño de un clúster, se encuentran disponibles diferentes opciones de escalado. Esto permite que el tamaño del clúster se ajuste a sus necesidades.

**Extensibilidad**

Redis es un proyecto de código abierto que cuenta con el apoyo de una comunidad activa. No hay limitaciones de proveedores ni tecnología porque Redis está basado en estándares abiertos, admite formatos de datos abiertos y cuenta con una completa base de clientes.

### instalar Redis

Como Redis es open source, es decir, de código abierto, así que cualquiera puede descargar, usar y editar el sistema.

El primer paso consiste en descargar Redis. Para ello, usamos el gestor de paquetes de Ubuntu, que tendremos que actualizar primero a la versión más reciente.

```sudo apt-get update```

```sudo apt-get install redis-server```

Para comprobar si Redis funciona correctamente, iniciamos la interfaz de comunicación con la base de datos:

```redis-cli```

La interfaz debería mostrar entonces ladirección IP y el puerto a través del cual se ejecuta Redis, a los que se puede enviar un ping de comprobación.

```
127.0.0.1:6379> ping
PONG
```

Si Redis responde, queda demostrado que el sistema de bases de datos se ha instalado correctamente. Ahora también se puede comprobar si se puede escribir texto.

```
127.0.0.1:6379> set test "OK!"
127.0.0.1:6379> get test
"OK!"
```

### crear entradas

Una vez hayas configurado Redis, ya puedes trabajar con la base de datos. Dispones para ello de varios tipos distintos de datos y de comandos.

**Strings**

Lo más fácil es crear una string, es decir, una cadena o secuencia de elementos. Para ello, utiliza el comando **set**.

```
127.0.0.1:6379> set foo "bar"
127.0.0.1:6379> set value 1
```

Si se solicitan ahora las entradas foo y value mediante el comando get, se mostrarán los valores correspondientes.

```
127.0.0.1:6379> get foo
"bar"
127.0.0.1:6379> get value
"1"
```

El comando para borrar una entrada es **del**.

```
127.0.0.1:6379> del foo
(integer) 1
127.0.0.1:6379> get foo
(nil)
```

Si no queremos crear muchas entradas usando una fila nueva cada vez, puedes usar la función avanzada mset. Para solicitar los valores de varios campos a la vez, también existe el comando mget.

```
127.0.0.1:6379> mset foo1 "bar1" foo2 "bar2" foo3 "bar3"
OK
127.0.0.1:6379> mget foo1 foo2 foo3
1) "bar1"
2) "bar2"
3) "bar3"
```

**Listas**

Con Redis se pueden usar, además, otros tipos de datos. Algunos de los más populares para trabajar con la base de datos son, por ejemplo, las listas y los sets. Ambos son conjuntos de valores, pero, mientras que los sets no tienen un orden concreto, los valores de las listas están numerados. En una lista se pueden añadir, solicitar o borrar entradas.

```
127.0.0.1:6379> lpush mylist foo
(integer) 1
127.0.0.1:6379> lpush mylist bar
(integer) 2
127.0.0.1:6379> lrange mylist 0 10
1) "foo"
2) "bar"
127.0.0.1:6379> linsert mylist before "bar" "test"
(integer) 3
127.0.0.1:6379> lrange mylist 0 10
1) "foo"
2) "test"
3) "bar"
127.0.0.1:6379> lrem mylist 0 foo
(integer) 1
127.0.0.1:6379> lrange mylist 0 10
1) "test"
2) "bar"
```

En este ejemplo hemos añadido en primer lugar dos elementos a una lista (lpush) y luego hemos solicitado que se muestren. Con el comando lrange se indica qué segmento debe mostrarse (aquí del 0 al 10, pero pueden usarse también números negativos). A continuación, mediante el comando linsert hemos añadido un valor nuevo delante de uno que ya existía (también podría usarse after), con lo cual hemos cambiado la numeración. El comando lrem permite borrar de la lista entradas con un valor específico.

**Sets**

Para los sets, Redis utiliza otros comandos, pero con resultados muy similares:

```
127.0.0.1:6379> sadd myset "foo"
(integer) 1
127.0.0.1:6379> sadd myset "bar"
(integer) 1
127.0.0.1:6379> smembers myset
1) "bar"
2) "foo"
127.0.0.1:6379> sismember myset "bar"
(integer) 1
127.0.0.1:6379> srem myset "bar"
(integer) 1
127.0.0.1:6379> smembers myset
1) "foo"
```

Con el comando sadd también se pueden integrar varios elementos en el set si se introducen en el comando uno detrás de otro. Para visualizar el set, basta con usar el comando smembers y el nombre del set en cuestión. El comando sismember permite, además, buscar una entrada concreta. De manera análoga a la lista, con srem se pueden borrar entradas sueltas.

Sin embargo, Redis también ofrece a los usuarios la posibilidad de utilizar sets en un formato ordenado.

```
127.0.0.1:6379> zadd mysortedset 1 "foo"
(integer) 1
127.0.0.1:6379> zadd mysortedset 2 "bar"
(integer) 1
127.0.0.1:6379> zadd mysortedset 2 "foobar"
(integer) 1
127.0.0.1:6379> zrange mysortedset 0 10
1) "foo"
2) "bar"
3) "foobar"

```

Para añadir elementos se utiliza, en este caso, el comando zadd y un score o puntaje. Mientras que los valores propiamente dichos no pueden aparecer más de una vez, con un score se puede indicar un mismo valor varias veces. El score no es, por lo tanto, una numeración directa dentro del set, sino una ponderación, de manera que todas las entradas con el puntaje o score2 aparecerán tras los que tengan el score1. Con el comando zrange se pueden visualizar todos los elementos o los que se seleccionen.

**Hashes**

Un tipo especial de datos son los hashes: entradas individuales compuestas de varios valores, de manera similar a los sets y las listas, pero en los que cada valor va acompañado de una clave, formando así los llamados pares clave-valor o key-value.

```
127.0.0.1:6379> zadd mysortedset 1 "foo"
(integer) 1
127.0.0.1:6379> zadd mysortedset 2 "bar"
(integer) 1
127.0.0.1:6379> zadd mysortedset 2 "foobar"
(integer) 1
127.0.0.1:6379> zrange mysortedset 0 10
1) "foo"
2) "bar"
3) "foobar"
```

En este ejemplo, hemos usado hset para crear un hash con el nombre user1 y tres campos. Mediante el comando hget podemos solicitar el valor de cada campo. Para que se muestren todos, se puede usar hgetall. Otras opciones para visualizar valores son hvals (muestra todos los valores guardados en el hash) y hkeys (muestra todas las claves guardadas en el hash). Con hdel se pueden borrar valores sueltos, mientras que con del, como ya hemos visto, se borra el hash entero.
