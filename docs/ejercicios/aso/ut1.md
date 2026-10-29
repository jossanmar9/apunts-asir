# UT1 · Bash — 120 ejercicios

Ejercicios adicionales para practicar Bash, ajustados al nivel y contenidos de clase y sin soluciones.

## Variables, parámetros y entrada/salida
1. **Ficha del servidor.** Recibe hostname, ubicación y responsable y muestra una ficha en tres líneas.
2. **Ruta de copia.** Recibe usuario y proyecto y construye `/backup/<usuario>/<proyecto>`.
3. **Argumentos recibidos.** Muestra nombre del script, número de argumentos y los tres primeros.
4. **Directorio personal.** Recibe un usuario y muestra `/home/<usuario>/documentos`.
5. **Etiqueta de equipo.** Recibe aula y puesto y genera `AULA-XX-PUESTO-YY`.
6. **Fecha de informe.** Guarda la fecha actual en una variable y la muestra.
7. **PID del script.** Muestra PID del script y PID de la shell padre.
8. **Último proceso.** Lanza `sleep 30` en background y muestra `$!`.
9. **Valor por defecto.** Usa un directorio recibido o `$HOME` si no se indica.
10. **Resumen de argumentos.** Recorre todos los parámetros y los muestra numerados.

## Cálculos y condicionales
11. **Porcentaje de memoria.** Recibe memoria usada/total y calcula porcentaje entero.
12. **Carga aceptable.** Recibe carga y núcleos e indica si la carga los supera.
13. **Puerto válido.** Comprueba que un número esté entre 1 y 65535.
14. **Puerto privilegiado.** Indica si un puerto válido es menor de 1024.
15. **Espacio de copia.** Decide si una copia cabe en el espacio libre indicado.
16. **Umbral de CPU.** NORMAL <70, AVISO 70–89, CRÍTICO >=90.
17. **Umbral de RAM.** Clasifica con límites 75 y 90.
18. **Tres niveles de batería.** Clasifica 0–20, 21–50 y 51–100.
19. **Código de salida.** 0=OK, 1=AVISO, resto=ERROR.
20. **Usuario root.** Comprueba si `$UID` vale 0.
21. **Número de copias.** Calcula cuántas copias completas caben en un disco.
22. **Resto libre.** Calcula espacio restante después de N copias.
23. **Múltiplo de intervalo.** Múltiplo de 5 y entre 10 y 100.
24. **Dos umbrales.** Avisa solo si CPU >80 y RAM >80.
25. **Incidencia parcial.** Avisa si CPU >80 o RAM >80.
26. **Horario nocturno.** Hora 0–23: indica si está entre 22 y 6.
27. **Día de mantenimiento.** Día 1–7: sábado/domingo son mantenimiento.
28. **Tamaño permitido.** Acepta un tamaño entre 1 y 500 MB.
29. **Comparar discos.** Indica cuál de dos porcentajes es mayor o empate.
30. **Validar tres parámetros.** Solo continúa con exactamente tres argumentos.
31. **División segura.** Divide dos enteros solo si divisor != 0.
32. **Rango de nice.** Comprueba entero entre -20 y 19.

## Bucles
33. **Cuenta regresiva.** De N hasta 0.
34. **Pares hasta N.** Números pares entre 0 y N.
35. **Tabla de multiplicar.** Tabla 1–10 del número recibido.
36. **Suma acumulada.** Suma enteros de 1 a N.
37. **Cinco comprobaciones.** Ejecuta `date` cinco veces con pausa de 1 s.
38. **Recorrer argumentos.** Muestra `Procesando:` para cada argumento.
39. **Argumentos largos.** Cuenta argumentos de más de 8 caracteres.
40. **Primer fallo.** Recorre rutas y para en la primera inexistente.
41. **Ignorar vacíos.** Ignora argumentos que sean cadenas vacías.
42. **Intentos.** Pide palabra hasta `salir` o cinco intentos.
43. **Menú simple.** `while` hasta elegir 0.
44. **Menú case.** Estado, fecha, usuario y salir con `case`.
45. **Recorrer home.** Muestra entradas de `$HOME` una por línea.
46. **Contar directorios.** Cuenta directorios inmediatos de una ruta.
47. **Contar ficheros.** Cuenta ficheros regulares inmediatos.
48. **Extensiones.** Recorre `.txt` de una carpeta.
49. **Tamaños.** Muestra nombre y bytes de cada fichero.
50. **Máximo.** Encuentra el mayor de los enteros recibidos.
51. **Mínimo.** Encuentra el menor.
52. **Promedio entero.** Media entera de argumentos numéricos.

## Ficheros, directorios y permisos
53. **Existe ruta.** Distingue inexistente, fichero y directorio.
54. **Legibilidad.** Comprueba existencia y lectura.
55. **Escritura.** Comprueba si un fichero es escribible.
56. **Ejecutable.** Comprueba si es fichero ejecutable.
57. **Crear estructura.** Crea `proyecto/{entrada,proceso,salida,logs}`.
58. **Copia segura.** Copia solo si origen existe y destino no.
59. **Backup con fecha.** Copia con fecha y hora en el nombre.
60. **Mover procesados.** Mueve `.ok` de entrada a procesados.
61. **Directorio vacío.** Indica si no contiene entradas.
62. **Ficheros ocultos.** Cuenta entradas ocultas.
63. **Permisos octales.** Propietario rwx; grupo/otros r-x.
64. **Quitar escritura global.** Quita escritura a grupo y otros.
65. **Añadir ejecución.** Ejecución solo al propietario.
66. **Propietario.** Muestra propietario y grupo con `stat`.
67. **Última modificación.** Muestra fecha de modificación.
68. **Más antiguo.** Compara dos ficheros.
69. **Enlace simbólico.** Crea y comprueba un enlace simbólico.
70. **Ficheros grandes.** Lista inmediatos mayores de 1 MiB.
71. **Borrar vacíos.** Localiza vacíos y pide confirmación antes de borrar.
72. **Inventario.** Genera nombre, tamaño y permisos de una carpeta.

## Redirecciones, tuberías y filtros
73. **Errores a fichero.** Guarda solo stderr de `ls` en `errores.log`.
74. **Salida separada.** stdout a `salida.txt`, stderr a `errores.txt`.
75. **Añadir registro.** Añade fecha y usuario a `actividad.log`.
76. **Primeras líneas.** Primeras 10 líneas de un fichero.
77. **Últimas líneas.** Últimas 15 líneas.
78. **Seguimiento.** Sigue un log en tiempo real.
79. **Contar usuarios.** Cuenta líneas de `/etc/passwd`.
80. **Shells únicas.** Extrae shells de `/etc/passwd`, ordena y elimina duplicados.
81. **Usuarios ordenados.** Extrae usuarios y ordena alfabéticamente.
82. **Top tamaños.** Cinco ficheros más grandes.
83. **Buscar ERROR.** Cuenta `ERROR` sin distinguir mayúsculas.
84. **Excluir comentarios.** Líneas que no empiezan por `#`.
85. **Sin vacíos.** Elimina líneas vacías de la salida.
86. **Dos filtros.** Contienen `ssh` pero no `failed`.
87. **Frecuencias.** Cuenta frecuencia de palabras.
88. **Procesos del usuario.** Cuenta procesos del usuario actual.

## Funciones
89. **Función mensaje.** `info()` antepone `[INFO]`.
90. **Función error.** `error()` escribe `[ERROR]` por stderr.
91. **Función existe.** Éxito si ruta existe; fallo si no.
92. **Función es_numero.** Comprueba solo dígitos.
93. **Función porcentaje.** Devuelve porcentaje entero usado/total.
94. **Función comprobar_directorio.** Valida existencia y tipo.
95. **Función crear_backup.** Crea copia fechada.
96. **Función log.** Añade fecha, nivel y mensaje a un log.
97. **Función uso.** Muestra sintaxis y termina con error.
98. **Funciones de menú.** Cada opción del menú en una función.

## Expresiones regulares básicas
99. **Solo dígitos.** Valida exclusivamente números.
100. **Usuario simple.** 3–12 letras minúsculas.
101. **Código de aula.** `AULA` + dos dígitos.
102. **Identificador.** Una mayúscula + cuatro dígitos.
103. **Hexadecimal simple.** Dígitos y A–F/a–f.
104. **Línea comentada.** Primer carácter `#`.
105. **Final `.log`.** Nombre termina exactamente en `.log`.
106. **Prefijo srv.** Cadena comienza por `srv-`.

## Expresiones regulares extendidas
107. **Hostname.** `srv-` o `pc-` + 2–4 dígitos.
108. **Versión.** Formato como `v2.15`.
109. **Fecha ISO.** Estructura `AAAA-MM-DD`.
110. **Hora.** `HH:MM` entre 00:00 y 23:59.
111. **Código de ticket.** `INC-` + exactamente 6 dígitos.
112. **Ruta home.** `/home/` + usuario sencillo.

## sed
113. **Cambiar puerto.** Sustituye `PORT=8080` por puerto recibido en una copia.
114. **Quitar espacios finales.** Elimina espacios al final de línea.
115. **Filtrar errores.** Con `sed`, muestra solo líneas con `ERROR`.
116. **Ocultar usuario.** Sustituye usuario recibido por `[USUARIO]` globalmente.

## Integradores
117. **Auditor de directorio.** Informe con ficheros, directorios, tamaño total y no legibles.
118. **Comprobador de configuración.** Valida fichero/permisos, ignora comentarios/vacíos y cuenta directivas.
119. **Monitor simulado.** CPU, RAM y disco: valida, clasifica estado global y registra log fechado.
120. **Procesador de logs.** Procesa `.log`, cuenta INFO/WARNING/ERROR y crea resumen ordenado sin modificar originales.
