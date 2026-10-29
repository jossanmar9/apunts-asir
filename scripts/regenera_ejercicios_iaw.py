from pathlib import Path

ROOT = Path('docs/ejercicios/iaw')

ut1 = [
('Estático o dinámico','Clasifica varios recursos web como estáticos, dinámicos o mixtos y justifica cada decisión.'),
('Ruta de una petición','Explica paso a paso qué ocurre desde que el navegador solicita index.php hasta que recibe HTML.'),
('Papel de Nginx','Describe qué peticiones puede resolver Nginx directamente y cuáles debe reenviar a PHP-FPM.'),
('Papel de PHP-FPM','Explica por qué PHP-FPM no sustituye a Nginx y qué devuelve después de ejecutar un script.'),
('Papel de MariaDB','Indica qué información tendría sentido guardar de forma persistente en una aplicación web sencilla.'),
('Código HTTP','Relaciona situaciones habituales con 200, 301/302, 403, 404 y 500.'),
('Petición HTTP','Identifica método, ruta y cabeceras en una petición HTTP de ejemplo.'),
('Respuesta HTTP','Identifica estado, cabeceras y cuerpo en una respuesta HTTP de ejemplo.'),
('GET y POST','Elige GET o POST para cinco situaciones web y justifica la elección.'),
('Diagnóstico 404','Propón una secuencia de comprobaciones cuando Nginx devuelve 404.'),
('Diagnóstico 500','Propón una secuencia de comprobaciones ante un error 500 en una página PHP.'),
('Puerto publicado','Explica qué significa 8080:80 y desde qué URL accederías al servicio.'),
('Conflicto de puerto','Un contenedor no arranca porque 8080 está ocupado. Indica cómo diagnosticarlo y una solución.'),
('Primer contenedor Nginx','Escribe y explica un docker run que publique Nginx en un puerto no estándar.'),
('Ciclo de un contenedor','Practica docker ps, logs, stop, start y rm sobre un contenedor de prueba.'),
('Bind mount','Monta una carpeta local con un index.html dentro de Nginx y comprueba que los cambios se reflejan.'),
('Montaje de solo lectura','Explica y prueba el efecto de :ro en un volumen de Nginx.'),
('Imagen frente a contenedor','Explica con un ejemplo práctico la diferencia entre una imagen y un contenedor.'),
('Dockerfile PHP','Diseña un Dockerfile mínimo basado en PHP-FPM y explica cada instrucción.'),
('Extensión PDO MySQL','Investiga qué necesita una imagen PHP para conectar mediante PDO con MariaDB y documenta la decisión.'),
('Tres servicios','Escribe el esqueleto de un compose.yaml con nginx, php y db.'),
('Dependencias','Añade depends_on donde tenga sentido y explica qué garantiza y qué no garantiza.'),
('Volúmenes Compose','Monta app/ en Nginx y PHP indicando por qué ambos necesitan acceder al código.'),
('Configuración Nginx','Monta default.conf desde el host y explica por qué es útil mantenerlo en el proyecto.'),
('FastCGI','Identifica la directiva de Nginx que permite enviar PHP al servicio PHP-FPM y explica el flujo.'),
('Nombre de servicio','Explica por qué PHP puede usar db como host de MariaDB dentro de Compose.'),
('No usar localhost','Razona por qué localhost desde el contenedor PHP no apunta al contenedor de base de datos.'),
('Variables de entorno','Pasa DB_HOST, DB_NAME, DB_USER y DB_PASSWORD al servicio PHP.'),
('.env.example','Crea una plantilla .env.example sin secretos reales y explica para qué sirve.'),
('.env y Git','Prepara .gitignore para evitar publicar el .env real.'),
('environment y env_file','Compara las dos formas de proporcionar variables a un servicio Compose.'),
('Inicialización SQL','Crea un init.sql que genere una tabla sencilla e inserte un registro inicial.'),
('Volumen de MariaDB','Añade persistencia para la base de datos y comprueba qué ocurre al recrear el contenedor.'),
('Reinicializar base','Explica por qué un init.sql puede no volver a ejecutarse si ya existe el volumen de datos.'),
('Construir y levantar','Practica docker compose up -d --build y explica cuándo necesitas --build.'),
('Estado del stack','Usa docker compose ps para comprobar el estado de los tres servicios.'),
('Logs completos','Obtén los logs del stack e identifica qué líneas pertenecen a cada servicio.'),
('Logs de un servicio','Sigue en tiempo real únicamente los logs de PHP o Nginx.'),
('Entrar en un contenedor','Usa docker compose exec para inspeccionar rutas y archivos dentro de un servicio.'),
('Comprobar variables','Comprueba desde el contenedor PHP que las variables de entorno esperadas existen.'),
('Conexión PHP-MariaDB','Crea una prueba mínima que confirme que PHP puede abrir una conexión PDO con db.'),
('Error de credenciales','Provoca una contraseña incorrecta y utiliza los logs para localizar el problema.'),
('Error de host','Cambia temporalmente DB_HOST por un nombre incorrecto y compara el error con el de credenciales.'),
('Error de Nginx-PHP','Rompe temporalmente el destino FastCGI y determina qué evidencia aparece en los logs.'),
('Servicio no disponible','Detén db y observa cómo se comporta la aplicación; documenta el diagnóstico.'),
('Reproducibilidad','Explica qué archivos necesitaría otra persona para levantar el mismo entorno desde cero.'),
('Seguridad de puertos','Decide qué servicios necesitan publicar puertos al host y cuáles pueden quedar solo en la red interna.'),
('Usuario de base de datos','Explica por qué la aplicación no debería conectarse habitualmente como root.'),
('Secretos','Localiza posibles secretos en una configuración de ejemplo y propón dónde deberían guardarse.'),
('Documentar el stack','Escribe una sección README con requisitos, arranque, comprobación, parada y solución de problemas.'),
('Mapa del stack','Dibuja en texto el recorrido navegador → Nginx → PHP-FPM → MariaDB y anota el protocolo o función de cada salto.'),
('Prueba de estáticos','Añade un archivo CSS y comprueba que Nginx puede servirlo sin ejecutar PHP.'),
('Prueba de PHP','Crea un script PHP mínimo y demuestra que el navegador recibe el resultado, no el código fuente.'),
('Página de estado','Crea una página de diagnóstico que indique si PHP funciona y si puede conectar con la base de datos.'),
('Cambio de puerto','Cambia solo el puerto del host sin modificar el puerto interno de Nginx y comprueba el resultado.'),
('Dos stacks','Plantea cómo ejecutar dos copias del proyecto simultáneamente evitando conflictos de puertos y nombres.'),
('Compose config','Usa docker compose config para revisar la configuración resultante y detectar variables ausentes.'),
('Recrear servicios','Compara restart con down/up y explica en qué situaciones no producen el mismo efecto.'),
('Evidencia técnica','Prepara una lista de comandos y capturas/resultados que demostrarían que el stack funciona correctamente.'),
('Caso final UT1','Monta desde una carpeta vacía un stack Nginx + PHP-FPM + MariaDB que muestre un registro inicial y documenta el diagnóstico de al menos un fallo provocado.'),
]

ut2 = [
('Servidor o cliente','Explica qué código ejecuta el servidor y qué recibe finalmente el navegador en una página PHP.'),
('Primer PHP','Crea un script que genere un título y un párrafo HTML desde PHP.'),
('Variables','Guarda nombre de servicio, precio y unidades en variables y muestra una frase con esos datos.'),
('Tipos','Crea valores int, float, string, bool y null y comprueba sus tipos con var_dump.'),
('Asignación','Sigue manualmente varias asignaciones y predice el valor final antes de ejecutar el script.'),
('Concatenación','Construye el mismo mensaje usando concatenación e interpolación.'),
('Operaciones','Calcula subtotal, IVA y total de un servicio web.'),
('Comparación estricta','Compara valores como 5 y "5" usando == y === y explica la diferencia observada.'),
('Condicional simple','Muestra un aviso si el número de usuarios supera un límite.'),
('if elseif else','Clasifica el uso de disco en normal, aviso o crítico.'),
('switch o match','Selecciona un mensaje según un plan de alojamiento.'),
('Bucle for','Genera una lista HTML numerada con varios servidores.'),
('while','Simula intentos restantes hasta llegar a cero.'),
('Array indexado','Guarda nombres de servicios en un array y recórrelo con foreach.'),
('Array asociativo','Representa un plan con nombre, precio y espacio y muestra sus datos.'),
('Tabla desde array','Genera una tabla HTML a partir de varios planes almacenados en un array.'),
('Función de cálculo','Crea una función que calcule el precio total a partir de precio mensual y meses.'),
('Función tipada','Añade tipos de parámetros y retorno a una función sencilla y prueba entradas válidas.'),
('Separar lógica y HTML','Calcula primero los datos y represéntalos después en una sección HTML.'),
('Escapar salida','Muestra texto que contiene etiquetas usando htmlspecialchars y compara el resultado sin escapar.'),
('Formulario GET','Crea un buscador sencillo que reciba un término mediante GET y lo muestre de forma segura.'),
('Formulario POST','Crea un formulario de contacto mínimo y comprueba REQUEST_METHOD antes de procesarlo.'),
('Leer POST','Recoge varios campos de $_POST usando valores por defecto cuando no existan.'),
('trim','Normaliza nombre y correo eliminando espacios exteriores antes de validar.'),
('Campo obligatorio','Valida que un nombre no esté vacío y muestra un mensaje claro.'),
('Correo válido','Valida un correo con filter_var y prueba varios casos.'),
('Entero en rango','Valida que los meses sean un entero entre 1 y 24.'),
('Opción permitida','Comprueba que el plan recibido pertenezca a una lista cerrada de opciones.'),
('Checkbox','Procesa un extra opcional enviado por checkbox sin generar avisos si no está marcado.'),
('Array de errores','Acumula varios errores de validación y muéstralos con foreach.'),
('Conservar valores','Haz que un formulario vuelva a mostrar los valores válidos introducidos después de un error.'),
('Select persistente','Conserva la opción seleccionada de un select tras una validación fallida.'),
('Presupuesto','Calcula plan + extras + meses solo cuando todos los datos sean válidos.'),
('GET frente a POST','Implementa dos formularios equivalentes y observa dónde aparecen los datos en cada caso.'),
('Depurar entrada','Usa print_r o var_dump para inspeccionar temporalmente $_GET y $_POST.'),
('php -l','Introduce y corrige varios errores de sintaxis utilizando php -l.'),
('Errores en desarrollo','Activa temporalmente error_reporting e ini_set para localizar un fallo y explica por qué no se hace igual en producción.'),
('Sesión básica','Inicia una sesión, guarda un nombre de usuario y recupéralo en otra página.'),
('Contador de sesión','Crea un contador de visitas dentro de la misma sesión.'),
('Cerrar sesión','Elimina correctamente los datos de sesión y redirige al usuario.'),
('Cookie sencilla','Crea una cookie de preferencia y léela en una petición posterior.'),
('Cabeceras','Provoca el error headers already sent y corrígelo moviendo la salida al lugar adecuado.'),
('Redirección','Redirige con header a otra página y utiliza exit después.'),
('Login simulado','Valida usuario y contraseña contra valores de prueba y guarda el usuario en sesión.'),
('Página protegida','Impide acceder a una página si no existe la variable de sesión de autenticación.'),
('Logout','Crea un flujo completo login → panel → logout sin base de datos.'),
('Función de validación','Extrae una validación repetida a una función reutilizable.'),
('Mensajes seguros','Muestra errores y datos del usuario sin insertar HTML externo sin escapar.'),
('Diagnóstico en Docker','Localiza un error PHP usando docker compose logs y docker compose exec.'),
('Miniaplicación final','Crea una miniaplicación de presupuesto con POST, validación, arrays, foreach, función propia y salida HTML segura.'),
]

def write_unit(slug, title, exercises, ext):
    d = ROOT / slug
    d.mkdir(parents=True, exist_ok=True)
    md = [f'# {title}', '', f'Banco de **{len(exercises)} ejercicios adicionales** para practicar. No incluyen solución y están pensados para complementar, no copiar, las actividades de clase.', '']
    for i,(name,text) in enumerate(exercises,1):
        fn=f'ejercicio_{i:03d}.{ext}'
        md += [f'## Ejercicio {i:03d} · {name}', '', text, '', f'[:material-code-tags: Abrir {fn}]({slug}/{fn}){{ .md-button }}', '']
        if ext=='php':
            body=f'''<?php\n/**\n * IAW · {title}\n * Ejercicio {i:03d} · {name}\n *\n * {text}\n */\n\ndeclare(strict_types=1);\n\n// Escribe tu solución a partir de aquí:\n'''
        else:
            body=f'''# IAW · {title}\n# Ejercicio {i:03d} · {name}\n#\n# {text}\n\n# Escribe aquí tus comandos, configuración o explicación.\n'''
        (d/fn).write_text(body,encoding='utf-8')
    (ROOT/f'{slug}.md').write_text('\n'.join(md),encoding='utf-8')

ROOT.mkdir(parents=True, exist_ok=True)
write_unit('ut1','UT1 · Entorno de implantación web',ut1,'txt')
write_unit('ut2','UT2 · Programación web en servidor con PHP',ut2,'php')
(ROOT/'index.md').write_text('''# Ejercicios · IAW\n\nEjercicios adicionales basados en los contenidos trabajados en clase. Los enunciados son nuevos y los archivos están preparados para que escribas tu propia solución.\n\n- [UT1 · Entorno de implantación web · 60 ejercicios](ut1.md)\n- [UT2 · Programación web en servidor con PHP · 50 ejercicios](ut2.md)\n''',encoding='utf-8')
print(f'Generados {len(ut1)+len(ut2)} ejercicios de IAW')
