# UT2 · Procesos, servicios y automatización — 50 ejercicios

Basados en la teoría de clase: procesos, systemd, cron/at y seguimiento/diagnóstico. Sin soluciones.

## Procesos y estados
1. Ejecuta `ps` y explica PID, TTY, TIME y CMD observando tu salida.
2. Muestra todos los procesos con formato extendido.
3. Muestra PID, PPID, estado y comando de tus procesos.
4. Muestra procesos de un usuario recibido como argumento.
5. Busca procesos `bash` mostrando PID y comando completo.
6. Usa `pstree` para localizar padre-hijo de tu shell.
7. Localiza procesos en estados S, R, T o Z.
8. Lanza `sleep 300` y averigua PID, PPID y estado.
9. Script que recibe PID e indica si existe usando código de salida.
10. Cinco procesos que más memoria consumen.
11. Diez procesos que más CPU consumen.
12. Genera `PID usuario CPU memoria comando` ordenado por CPU.

## Primer/segundo plano, señales y prioridades
13. Ejecuta dos `sleep` en background y comprueba `jobs`.
14. Suspende un proceso y continúa en background.
15. Recupera al foreground uno de varios trabajos.
16. Lanza proceso en background y muestra `$!`.
17. Envía SIGTERM a un `sleep` propio y comprueba que desaparece.
18. Script: SIGTERM, espera 2 s y comprueba si sigue vivo antes de indicar que requeriría SIGKILL.
19. Compara `kill`, `killall` y `pkill` solo con procesos de prueba propios.
20. Lanza `sleep 300` con nice 10 y comprueba NI.
21. Cambia el nice anterior a 15 y verifica.
22. Intenta reducir nice como usuario normal y documenta el error.
23. Ejecuta tarea con `nohup` y comprueba desde otra terminal que continúa.
24. Usa `lsof` para averiguar qué proceso tiene abierto un fichero temporal propio.

## Servicios y systemd
25. Consulta estado de un servicio sin modificarlo.
26. Lista unidades de tipo servicio cargadas.
27. Distingue si un servicio está activo y habilitado al arranque.
28. Explica con pruebas diferencia entre `start` y `enable`.
29. Diferencia `restart` y `reload` con un servicio que soporte recarga.
30. Consulta si una unidad está `masked` sin enmascarar servicios esenciales.
31. Localiza el fichero de unidad de un servicio y muéstralo sin editar.
32. Script que recibe servicio y muestra active/inactive y enabled/disabled sin cambiar estado.

## cron y at
33. Cron para `/home/alumno/copia.sh` cada día a las 23:30.
34. Expresión cron cada 15 minutos.
35. Tarea de lunes a viernes a las 08:00.
36. Tarea días 1 y 15 de cada mes a las 02:10.
37. Tarea cada dos horas usando `/`.
38. Compara crontab de usuario y `/etc/crontab`; identifica campo adicional.
39. Lista tu crontab sin modificarlo.
40. Con `at`, tarea de prueba dentro de 5 minutos que escriba fecha en fichero temporal.
41. Lista tareas `at` e identifica ID.
42. Elimina solo tu tarea de prueba con `atrm`.

## Seguimiento y diagnóstico
43. Usa `uptime` y compara carga 1/5/15 min con número de núcleos.
44. Consulta memoria/swap con `free -h` y contrasta `/proc/meminfo`.
45. Con `df -h`, localiza mayor ocupación y usa `du` en una carpeta propia.
46. Consulta puertos a la escucha con `ss -tulpn` e identifica campos.
47. Toma cinco muestras CPU con `sar -u 1 5` si sysstat está disponible.
48. `journalctl`: mensajes de un servicio última hora y errores del arranque actual.
49. Examina una configuración `logrotate`: frecuencia, rotaciones, compresión, vacíos/ausentes.
50. **Caso de diagnóstico.** Servidor lento: secuencia con `top`, `vmstat`, `free`, `iostat`, `df`, `ss` y `journalctl`, indicando qué confirmas/descartas.
