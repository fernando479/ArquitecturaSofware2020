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
