# UT1 · Bash — 120 ejercicios

Ejercicios adicionales para practicar Bash, ajustados al nivel y contenidos de clase y sin soluciones.

## Variables, parámetros y entrada/salida
1. **Ficha del servidor.** Recibe hostname, ubicación y responsable y muestra una ficha en tres líneas.
[🐚 Abrir ejercicio_001.sh](ut1/ejercicio_001.sh){ .md-button }

2. **Ruta de copia.** Recibe usuario y proyecto y construye `/backup/<usuario>/<proyecto>`.
[🐚 Abrir ejercicio_002.sh](ut1/ejercicio_002.sh){ .md-button }

3. **Argumentos recibidos.** Muestra nombre del script, número de argumentos y los tres primeros.
[🐚 Abrir ejercicio_003.sh](ut1/ejercicio_003.sh){ .md-button }

4. **Directorio personal.** Recibe un usuario y muestra `/home/<usuario>/documentos`.
[🐚 Abrir ejercicio_004.sh](ut1/ejercicio_004.sh){ .md-button }

5. **Etiqueta de equipo.** Recibe aula y puesto y genera `AULA-XX-PUESTO-YY`.
[🐚 Abrir ejercicio_005.sh](ut1/ejercicio_005.sh){ .md-button }

6. **Fecha de informe.** Guarda la fecha actual en una variable y la muestra.
[🐚 Abrir ejercicio_006.sh](ut1/ejercicio_006.sh){ .md-button }

7. **PID del script.** Muestra PID del script y PID de la shell padre.
[🐚 Abrir ejercicio_007.sh](ut1/ejercicio_007.sh){ .md-button }

8. **Último proceso.** Lanza `sleep 30` en background y muestra `$!`.
[🐚 Abrir ejercicio_008.sh](ut1/ejercicio_008.sh){ .md-button }

9. **Valor por defecto.** Usa un directorio recibido o `$HOME` si no se indica.
[🐚 Abrir ejercicio_009.sh](ut1/ejercicio_009.sh){ .md-button }

10. **Resumen de argumentos.** Recorre todos los parámetros y los muestra numerados.
[🐚 Abrir ejercicio_010.sh](ut1/ejercicio_010.sh){ .md-button }


## Cálculos y condicionales
11. **Porcentaje de memoria.** Recibe memoria usada/total y calcula porcentaje entero.
[🐚 Abrir ejercicio_011.sh](ut1/ejercicio_011.sh){ .md-button }

12. **Carga aceptable.** Recibe carga y núcleos e indica si la carga los supera.
[🐚 Abrir ejercicio_012.sh](ut1/ejercicio_012.sh){ .md-button }

13. **Puerto válido.** Comprueba que un número esté entre 1 y 65535.
[🐚 Abrir ejercicio_013.sh](ut1/ejercicio_013.sh){ .md-button }

14. **Puerto privilegiado.** Indica si un puerto válido es menor de 1024.
[🐚 Abrir ejercicio_014.sh](ut1/ejercicio_014.sh){ .md-button }

15. **Espacio de copia.** Decide si una copia cabe en el espacio libre indicado.
[🐚 Abrir ejercicio_015.sh](ut1/ejercicio_015.sh){ .md-button }

16. **Umbral de CPU.** NORMAL <70, AVISO 70–89, CRÍTICO >=90.
[🐚 Abrir ejercicio_016.sh](ut1/ejercicio_016.sh){ .md-button }

17. **Umbral de RAM.** Clasifica con límites 75 y 90.
[🐚 Abrir ejercicio_017.sh](ut1/ejercicio_017.sh){ .md-button }

18. **Tres niveles de batería.** Clasifica 0–20, 21–50 y 51–100.
[🐚 Abrir ejercicio_018.sh](ut1/ejercicio_018.sh){ .md-button }

19. **Código de salida.** 0=OK, 1=AVISO, resto=ERROR.
[🐚 Abrir ejercicio_019.sh](ut1/ejercicio_019.sh){ .md-button }

20. **Usuario root.** Comprueba si `$UID` vale 0.
[🐚 Abrir ejercicio_020.sh](ut1/ejercicio_020.sh){ .md-button }

21. **Número de copias.** Calcula cuántas copias completas caben en un disco.
[🐚 Abrir ejercicio_021.sh](ut1/ejercicio_021.sh){ .md-button }

22. **Resto libre.** Calcula espacio restante después de N copias.
[🐚 Abrir ejercicio_022.sh](ut1/ejercicio_022.sh){ .md-button }

23. **Múltiplo de intervalo.** Múltiplo de 5 y entre 10 y 100.
[🐚 Abrir ejercicio_023.sh](ut1/ejercicio_023.sh){ .md-button }

24. **Dos umbrales.** Avisa solo si CPU >80 y RAM >80.
[🐚 Abrir ejercicio_024.sh](ut1/ejercicio_024.sh){ .md-button }

25. **Incidencia parcial.** Avisa si CPU >80 o RAM >80.
[🐚 Abrir ejercicio_025.sh](ut1/ejercicio_025.sh){ .md-button }

26. **Horario nocturno.** Hora 0–23: indica si está entre 22 y 6.
[🐚 Abrir ejercicio_026.sh](ut1/ejercicio_026.sh){ .md-button }

27. **Día de mantenimiento.** Día 1–7: sábado/domingo son mantenimiento.
[🐚 Abrir ejercicio_027.sh](ut1/ejercicio_027.sh){ .md-button }

28. **Tamaño permitido.** Acepta un tamaño entre 1 y 500 MB.
[🐚 Abrir ejercicio_028.sh](ut1/ejercicio_028.sh){ .md-button }

29. **Comparar discos.** Indica cuál de dos porcentajes es mayor o empate.
[🐚 Abrir ejercicio_029.sh](ut1/ejercicio_029.sh){ .md-button }

30. **Validar tres parámetros.** Solo continúa con exactamente tres argumentos.
[🐚 Abrir ejercicio_030.sh](ut1/ejercicio_030.sh){ .md-button }

31. **División segura.** Divide dos enteros solo si divisor != 0.
[🐚 Abrir ejercicio_031.sh](ut1/ejercicio_031.sh){ .md-button }

32. **Rango de nice.** Comprueba entero entre -20 y 19.
[🐚 Abrir ejercicio_032.sh](ut1/ejercicio_032.sh){ .md-button }


## Bucles
33. **Cuenta regresiva.** De N hasta 0.
[🐚 Abrir ejercicio_033.sh](ut1/ejercicio_033.sh){ .md-button }

34. **Pares hasta N.** Números pares entre 0 y N.
[🐚 Abrir ejercicio_034.sh](ut1/ejercicio_034.sh){ .md-button }

35. **Tabla de multiplicar.** Tabla 1–10 del número recibido.
[🐚 Abrir ejercicio_035.sh](ut1/ejercicio_035.sh){ .md-button }

36. **Suma acumulada.** Suma enteros de 1 a N.
[🐚 Abrir ejercicio_036.sh](ut1/ejercicio_036.sh){ .md-button }

37. **Cinco comprobaciones.** Ejecuta `date` cinco veces con pausa de 1 s.
[🐚 Abrir ejercicio_037.sh](ut1/ejercicio_037.sh){ .md-button }

38. **Recorrer argumentos.** Muestra `Procesando:` para cada argumento.
[🐚 Abrir ejercicio_038.sh](ut1/ejercicio_038.sh){ .md-button }

39. **Argumentos largos.** Cuenta argumentos de más de 8 caracteres.
[🐚 Abrir ejercicio_039.sh](ut1/ejercicio_039.sh){ .md-button }

40. **Primer fallo.** Recorre rutas y para en la primera inexistente.
[🐚 Abrir ejercicio_040.sh](ut1/ejercicio_040.sh){ .md-button }

41. **Ignorar vacíos.** Ignora argumentos que sean cadenas vacías.
[🐚 Abrir ejercicio_041.sh](ut1/ejercicio_041.sh){ .md-button }

42. **Intentos.** Pide palabra hasta `salir` o cinco intentos.
[🐚 Abrir ejercicio_042.sh](ut1/ejercicio_042.sh){ .md-button }

43. **Menú simple.** `while` hasta elegir 0.
[🐚 Abrir ejercicio_043.sh](ut1/ejercicio_043.sh){ .md-button }

44. **Menú case.** Estado, fecha, usuario y salir con `case`.
[🐚 Abrir ejercicio_044.sh](ut1/ejercicio_044.sh){ .md-button }

45. **Recorrer home.** Muestra entradas de `$HOME` una por línea.
[🐚 Abrir ejercicio_045.sh](ut1/ejercicio_045.sh){ .md-button }

46. **Contar directorios.** Cuenta directorios inmediatos de una ruta.
[🐚 Abrir ejercicio_046.sh](ut1/ejercicio_046.sh){ .md-button }

47. **Contar ficheros.** Cuenta ficheros regulares inmediatos.
[🐚 Abrir ejercicio_047.sh](ut1/ejercicio_047.sh){ .md-button }

48. **Extensiones.** Recorre `.txt` de una carpeta.
[🐚 Abrir ejercicio_048.sh](ut1/ejercicio_048.sh){ .md-button }

49. **Tamaños.** Muestra nombre y bytes de cada fichero.
[🐚 Abrir ejercicio_049.sh](ut1/ejercicio_049.sh){ .md-button }

50. **Máximo.** Encuentra el mayor de los enteros recibidos.
[🐚 Abrir ejercicio_050.sh](ut1/ejercicio_050.sh){ .md-button }

51. **Mínimo.** Encuentra el menor.
[🐚 Abrir ejercicio_051.sh](ut1/ejercicio_051.sh){ .md-button }

52. **Promedio entero.** Media entera de argumentos numéricos.
[🐚 Abrir ejercicio_052.sh](ut1/ejercicio_052.sh){ .md-button }


## Ficheros, directorios y permisos
53. **Existe ruta.** Distingue inexistente, fichero y directorio.
[🐚 Abrir ejercicio_053.sh](ut1/ejercicio_053.sh){ .md-button }

54. **Legibilidad.** Comprueba existencia y lectura.
[🐚 Abrir ejercicio_054.sh](ut1/ejercicio_054.sh){ .md-button }

55. **Escritura.** Comprueba si un fichero es escribible.
[🐚 Abrir ejercicio_055.sh](ut1/ejercicio_055.sh){ .md-button }

56. **Ejecutable.** Comprueba si es fichero ejecutable.
[🐚 Abrir ejercicio_056.sh](ut1/ejercicio_056.sh){ .md-button }

57. **Crear estructura.** Crea `proyecto/{entrada,proceso,salida,logs}`.
[🐚 Abrir ejercicio_057.sh](ut1/ejercicio_057.sh){ .md-button }

58. **Copia segura.** Copia solo si origen existe y destino no.
[🐚 Abrir ejercicio_058.sh](ut1/ejercicio_058.sh){ .md-button }

59. **Backup con fecha.** Copia con fecha y hora en el nombre.
[🐚 Abrir ejercicio_059.sh](ut1/ejercicio_059.sh){ .md-button }

60. **Mover procesados.** Mueve `.ok` de entrada a procesados.
[🐚 Abrir ejercicio_060.sh](ut1/ejercicio_060.sh){ .md-button }

61. **Directorio vacío.** Indica si no contiene entradas.
[🐚 Abrir ejercicio_061.sh](ut1/ejercicio_061.sh){ .md-button }

62. **Ficheros ocultos.** Cuenta entradas ocultas.
[🐚 Abrir ejercicio_062.sh](ut1/ejercicio_062.sh){ .md-button }

63. **Permisos octales.** Propietario rwx; grupo/otros r-x.
[🐚 Abrir ejercicio_063.sh](ut1/ejercicio_063.sh){ .md-button }

64. **Quitar escritura global.** Quita escritura a grupo y otros.
[🐚 Abrir ejercicio_064.sh](ut1/ejercicio_064.sh){ .md-button }

65. **Añadir ejecución.** Ejecución solo al propietario.
[🐚 Abrir ejercicio_065.sh](ut1/ejercicio_065.sh){ .md-button }

66. **Propietario.** Muestra propietario y grupo con `stat`.
[🐚 Abrir ejercicio_066.sh](ut1/ejercicio_066.sh){ .md-button }

67. **Última modificación.** Muestra fecha de modificación.
[🐚 Abrir ejercicio_067.sh](ut1/ejercicio_067.sh){ .md-button }

68. **Más antiguo.** Compara dos ficheros.
[🐚 Abrir ejercicio_068.sh](ut1/ejercicio_068.sh){ .md-button }

69. **Enlace simbólico.** Crea y comprueba un enlace simbólico.
[🐚 Abrir ejercicio_069.sh](ut1/ejercicio_069.sh){ .md-button }

70. **Ficheros grandes.** Lista inmediatos mayores de 1 MiB.
[🐚 Abrir ejercicio_070.sh](ut1/ejercicio_070.sh){ .md-button }

71. **Borrar vacíos.** Localiza vacíos y pide confirmación antes de borrar.
[🐚 Abrir ejercicio_071.sh](ut1/ejercicio_071.sh){ .md-button }

72. **Inventario.** Genera nombre, tamaño y permisos de una carpeta.
[🐚 Abrir ejercicio_072.sh](ut1/ejercicio_072.sh){ .md-button }


## Redirecciones, tuberías y filtros
73. **Errores a fichero.** Guarda solo stderr de `ls` en `errores.log`.
[🐚 Abrir ejercicio_073.sh](ut1/ejercicio_073.sh){ .md-button }

74. **Salida separada.** stdout a `salida.txt`, stderr a `errores.txt`.
[🐚 Abrir ejercicio_074.sh](ut1/ejercicio_074.sh){ .md-button }

75. **Añadir registro.** Añade fecha y usuario a `actividad.log`.
[🐚 Abrir ejercicio_075.sh](ut1/ejercicio_075.sh){ .md-button }

76. **Primeras líneas.** Primeras 10 líneas de un fichero.
[🐚 Abrir ejercicio_076.sh](ut1/ejercicio_076.sh){ .md-button }

77. **Últimas líneas.** Últimas 15 líneas.
[🐚 Abrir ejercicio_077.sh](ut1/ejercicio_077.sh){ .md-button }

78. **Seguimiento.** Sigue un log en tiempo real.
[🐚 Abrir ejercicio_078.sh](ut1/ejercicio_078.sh){ .md-button }

79. **Contar usuarios.** Cuenta líneas de `/etc/passwd`.
[🐚 Abrir ejercicio_079.sh](ut1/ejercicio_079.sh){ .md-button }

80. **Shells únicas.** Extrae shells de `/etc/passwd`, ordena y elimina duplicados.
[🐚 Abrir ejercicio_080.sh](ut1/ejercicio_080.sh){ .md-button }

81. **Usuarios ordenados.** Extrae usuarios y ordena alfabéticamente.
[🐚 Abrir ejercicio_081.sh](ut1/ejercicio_081.sh){ .md-button }

82. **Top tamaños.** Cinco ficheros más grandes.
[🐚 Abrir ejercicio_082.sh](ut1/ejercicio_082.sh){ .md-button }

83. **Buscar ERROR.** Cuenta `ERROR` sin distinguir mayúsculas.
[🐚 Abrir ejercicio_083.sh](ut1/ejercicio_083.sh){ .md-button }

84. **Excluir comentarios.** Líneas que no empiezan por `#`.
[🐚 Abrir ejercicio_084.sh](ut1/ejercicio_084.sh){ .md-button }

85. **Sin vacíos.** Elimina líneas vacías de la salida.
[🐚 Abrir ejercicio_085.sh](ut1/ejercicio_085.sh){ .md-button }

86. **Dos filtros.** Contienen `ssh` pero no `failed`.
[🐚 Abrir ejercicio_086.sh](ut1/ejercicio_086.sh){ .md-button }

87. **Frecuencias.** Cuenta frecuencia de palabras.
[🐚 Abrir ejercicio_087.sh](ut1/ejercicio_087.sh){ .md-button }

88. **Procesos del usuario.** Cuenta procesos del usuario actual.
[🐚 Abrir ejercicio_088.sh](ut1/ejercicio_088.sh){ .md-button }


## Funciones
89. **Función mensaje.** `info()` antepone `[INFO]`.
[🐚 Abrir ejercicio_089.sh](ut1/ejercicio_089.sh){ .md-button }

90. **Función error.** `error()` escribe `[ERROR]` por stderr.
[🐚 Abrir ejercicio_090.sh](ut1/ejercicio_090.sh){ .md-button }

91. **Función existe.** Éxito si ruta existe; fallo si no.
[🐚 Abrir ejercicio_091.sh](ut1/ejercicio_091.sh){ .md-button }

92. **Función es_numero.** Comprueba solo dígitos.
[🐚 Abrir ejercicio_092.sh](ut1/ejercicio_092.sh){ .md-button }

93. **Función porcentaje.** Devuelve porcentaje entero usado/total.
[🐚 Abrir ejercicio_093.sh](ut1/ejercicio_093.sh){ .md-button }

94. **Función comprobar_directorio.** Valida existencia y tipo.
[🐚 Abrir ejercicio_094.sh](ut1/ejercicio_094.sh){ .md-button }

95. **Función crear_backup.** Crea copia fechada.
[🐚 Abrir ejercicio_095.sh](ut1/ejercicio_095.sh){ .md-button }

96. **Función log.** Añade fecha, nivel y mensaje a un log.
[🐚 Abrir ejercicio_096.sh](ut1/ejercicio_096.sh){ .md-button }

97. **Función uso.** Muestra sintaxis y termina con error.
[🐚 Abrir ejercicio_097.sh](ut1/ejercicio_097.sh){ .md-button }

98. **Funciones de menú.** Cada opción del menú en una función.
[🐚 Abrir ejercicio_098.sh](ut1/ejercicio_098.sh){ .md-button }


## Expresiones regulares básicas
99. **Solo dígitos.** Valida exclusivamente números.
[🐚 Abrir ejercicio_099.sh](ut1/ejercicio_099.sh){ .md-button }

100. **Usuario simple.** 3–12 letras minúsculas.
[🐚 Abrir ejercicio_100.sh](ut1/ejercicio_100.sh){ .md-button }

101. **Código de aula.** `AULA` + dos dígitos.
[🐚 Abrir ejercicio_101.sh](ut1/ejercicio_101.sh){ .md-button }

102. **Identificador.** Una mayúscula + cuatro dígitos.
[🐚 Abrir ejercicio_102.sh](ut1/ejercicio_102.sh){ .md-button }

103. **Hexadecimal simple.** Dígitos y A–F/a–f.
[🐚 Abrir ejercicio_103.sh](ut1/ejercicio_103.sh){ .md-button }

104. **Línea comentada.** Primer carácter `#`.
[🐚 Abrir ejercicio_104.sh](ut1/ejercicio_104.sh){ .md-button }

105. **Final `.log`.** Nombre termina exactamente en `.log`.
[🐚 Abrir ejercicio_105.sh](ut1/ejercicio_105.sh){ .md-button }

106. **Prefijo srv.** Cadena comienza por `srv-`.
[🐚 Abrir ejercicio_106.sh](ut1/ejercicio_106.sh){ .md-button }


## Expresiones regulares extendidas
107. **Hostname.** `srv-` o `pc-` + 2–4 dígitos.
[🐚 Abrir ejercicio_107.sh](ut1/ejercicio_107.sh){ .md-button }

108. **Versión.** Formato como `v2.15`.
[🐚 Abrir ejercicio_108.sh](ut1/ejercicio_108.sh){ .md-button }

109. **Fecha ISO.** Estructura `AAAA-MM-DD`.
[🐚 Abrir ejercicio_109.sh](ut1/ejercicio_109.sh){ .md-button }

110. **Hora.** `HH:MM` entre 00:00 y 23:59.
[🐚 Abrir ejercicio_110.sh](ut1/ejercicio_110.sh){ .md-button }

111. **Código de ticket.** `INC-` + exactamente 6 dígitos.
[🐚 Abrir ejercicio_111.sh](ut1/ejercicio_111.sh){ .md-button }

112. **Ruta home.** `/home/` + usuario sencillo.
[🐚 Abrir ejercicio_112.sh](ut1/ejercicio_112.sh){ .md-button }


## sed
113. **Cambiar puerto.** Sustituye `PORT=8080` por puerto recibido en una copia.
[🐚 Abrir ejercicio_113.sh](ut1/ejercicio_113.sh){ .md-button }

114. **Quitar espacios finales.** Elimina espacios al final de línea.
[🐚 Abrir ejercicio_114.sh](ut1/ejercicio_114.sh){ .md-button }

115. **Filtrar errores.** Con `sed`, muestra solo líneas con `ERROR`.
[🐚 Abrir ejercicio_115.sh](ut1/ejercicio_115.sh){ .md-button }

116. **Ocultar usuario.** Sustituye usuario recibido por `[USUARIO]` globalmente.
[🐚 Abrir ejercicio_116.sh](ut1/ejercicio_116.sh){ .md-button }


## Integradores
117. **Auditor de directorio.** Informe con ficheros, directorios, tamaño total y no legibles.
[🐚 Abrir ejercicio_117.sh](ut1/ejercicio_117.sh){ .md-button }

118. **Comprobador de configuración.** Valida fichero/permisos, ignora comentarios/vacíos y cuenta directivas.
[🐚 Abrir ejercicio_118.sh](ut1/ejercicio_118.sh){ .md-button }

119. **Monitor simulado.** CPU, RAM y disco: valida, clasifica estado global y registra log fechado.
[🐚 Abrir ejercicio_119.sh](ut1/ejercicio_119.sh){ .md-button }

120. **Procesador de logs.** Procesa `.log`, cuenta INFO/WARNING/ERROR y crea resumen ordenado sin modificar originales.
[🐚 Abrir ejercicio_120.sh](ut1/ejercicio_120.sh){ .md-button }
