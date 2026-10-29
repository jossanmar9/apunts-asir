# UT2 · Procesos, servicios y automatización — 50 ejercicios

Basados en la teoría de clase: procesos, systemd, cron/at y seguimiento/diagnóstico. Sin soluciones.

## Procesos y estados
1. Ejecuta `ps` y explica PID, TTY, TIME y CMD observando tu salida.
[🐚 Abrir ejercicio_001.sh](ut2/ejercicio_001.sh){ .md-button }

2. Muestra todos los procesos con formato extendido.
[🐚 Abrir ejercicio_002.sh](ut2/ejercicio_002.sh){ .md-button }

3. Muestra PID, PPID, estado y comando de tus procesos.
[🐚 Abrir ejercicio_003.sh](ut2/ejercicio_003.sh){ .md-button }

4. Muestra procesos de un usuario recibido como argumento.
[🐚 Abrir ejercicio_004.sh](ut2/ejercicio_004.sh){ .md-button }

5. Busca procesos `bash` mostrando PID y comando completo.
[🐚 Abrir ejercicio_005.sh](ut2/ejercicio_005.sh){ .md-button }

6. Usa `pstree` para localizar padre-hijo de tu shell.
[🐚 Abrir ejercicio_006.sh](ut2/ejercicio_006.sh){ .md-button }

7. Localiza procesos en estados S, R, T o Z.
[🐚 Abrir ejercicio_007.sh](ut2/ejercicio_007.sh){ .md-button }

8. Lanza `sleep 300` y averigua PID, PPID y estado.
[🐚 Abrir ejercicio_008.sh](ut2/ejercicio_008.sh){ .md-button }

9. Script que recibe PID e indica si existe usando código de salida.
[🐚 Abrir ejercicio_009.sh](ut2/ejercicio_009.sh){ .md-button }

10. Cinco procesos que más memoria consumen.
[🐚 Abrir ejercicio_010.sh](ut2/ejercicio_010.sh){ .md-button }

11. Diez procesos que más CPU consumen.
[🐚 Abrir ejercicio_011.sh](ut2/ejercicio_011.sh){ .md-button }

12. Genera `PID usuario CPU memoria comando` ordenado por CPU.
[🐚 Abrir ejercicio_012.sh](ut2/ejercicio_012.sh){ .md-button }


## Primer/segundo plano, señales y prioridades
13. Ejecuta dos `sleep` en background y comprueba `jobs`.
[🐚 Abrir ejercicio_013.sh](ut2/ejercicio_013.sh){ .md-button }

14. Suspende un proceso y continúa en background.
[🐚 Abrir ejercicio_014.sh](ut2/ejercicio_014.sh){ .md-button }

15. Recupera al foreground uno de varios trabajos.
[🐚 Abrir ejercicio_015.sh](ut2/ejercicio_015.sh){ .md-button }

16. Lanza proceso en background y muestra `$!`.
[🐚 Abrir ejercicio_016.sh](ut2/ejercicio_016.sh){ .md-button }

17. Envía SIGTERM a un `sleep` propio y comprueba que desaparece.
[🐚 Abrir ejercicio_017.sh](ut2/ejercicio_017.sh){ .md-button }

18. Script: SIGTERM, espera 2 s y comprueba si sigue vivo antes de indicar que requeriría SIGKILL.
[🐚 Abrir ejercicio_018.sh](ut2/ejercicio_018.sh){ .md-button }

19. Compara `kill`, `killall` y `pkill` solo con procesos de prueba propios.
[🐚 Abrir ejercicio_019.sh](ut2/ejercicio_019.sh){ .md-button }

20. Lanza `sleep 300` con nice 10 y comprueba NI.
[🐚 Abrir ejercicio_020.sh](ut2/ejercicio_020.sh){ .md-button }

21. Cambia el nice anterior a 15 y verifica.
[🐚 Abrir ejercicio_021.sh](ut2/ejercicio_021.sh){ .md-button }

22. Intenta reducir nice como usuario normal y documenta el error.
[🐚 Abrir ejercicio_022.sh](ut2/ejercicio_022.sh){ .md-button }

23. Ejecuta tarea con `nohup` y comprueba desde otra terminal que continúa.
[🐚 Abrir ejercicio_023.sh](ut2/ejercicio_023.sh){ .md-button }

24. Usa `lsof` para averiguar qué proceso tiene abierto un fichero temporal propio.
[🐚 Abrir ejercicio_024.sh](ut2/ejercicio_024.sh){ .md-button }


## Servicios y systemd
25. Consulta estado de un servicio sin modificarlo.
[🐚 Abrir ejercicio_025.sh](ut2/ejercicio_025.sh){ .md-button }

26. Lista unidades de tipo servicio cargadas.
[🐚 Abrir ejercicio_026.sh](ut2/ejercicio_026.sh){ .md-button }

27. Distingue si un servicio está activo y habilitado al arranque.
[🐚 Abrir ejercicio_027.sh](ut2/ejercicio_027.sh){ .md-button }

28. Explica con pruebas diferencia entre `start` y `enable`.
[🐚 Abrir ejercicio_028.sh](ut2/ejercicio_028.sh){ .md-button }

29. Diferencia `restart` y `reload` con un servicio que soporte recarga.
[🐚 Abrir ejercicio_029.sh](ut2/ejercicio_029.sh){ .md-button }

30. Consulta si una unidad está `masked` sin enmascarar servicios esenciales.
[🐚 Abrir ejercicio_030.sh](ut2/ejercicio_030.sh){ .md-button }

31. Localiza el fichero de unidad de un servicio y muéstralo sin editar.
[🐚 Abrir ejercicio_031.sh](ut2/ejercicio_031.sh){ .md-button }

32. Script que recibe servicio y muestra active/inactive y enabled/disabled sin cambiar estado.
[🐚 Abrir ejercicio_032.sh](ut2/ejercicio_032.sh){ .md-button }


## cron y at
33. Cron para `/home/alumno/copia.sh` cada día a las 23:30.
[🐚 Abrir ejercicio_033.sh](ut2/ejercicio_033.sh){ .md-button }

34. Expresión cron cada 15 minutos.
[🐚 Abrir ejercicio_034.sh](ut2/ejercicio_034.sh){ .md-button }

35. Tarea de lunes a viernes a las 08:00.
[🐚 Abrir ejercicio_035.sh](ut2/ejercicio_035.sh){ .md-button }

36. Tarea días 1 y 15 de cada mes a las 02:10.
[🐚 Abrir ejercicio_036.sh](ut2/ejercicio_036.sh){ .md-button }

37. Tarea cada dos horas usando `/`.
[🐚 Abrir ejercicio_037.sh](ut2/ejercicio_037.sh){ .md-button }

38. Compara crontab de usuario y `/etc/crontab`; identifica campo adicional.
[🐚 Abrir ejercicio_038.sh](ut2/ejercicio_038.sh){ .md-button }

39. Lista tu crontab sin modificarlo.
[🐚 Abrir ejercicio_039.sh](ut2/ejercicio_039.sh){ .md-button }

40. Con `at`, tarea de prueba dentro de 5 minutos que escriba fecha en fichero temporal.
[🐚 Abrir ejercicio_040.sh](ut2/ejercicio_040.sh){ .md-button }

41. Lista tareas `at` e identifica ID.
[🐚 Abrir ejercicio_041.sh](ut2/ejercicio_041.sh){ .md-button }

42. Elimina solo tu tarea de prueba con `atrm`.
[🐚 Abrir ejercicio_042.sh](ut2/ejercicio_042.sh){ .md-button }


## Seguimiento y diagnóstico
43. Usa `uptime` y compara carga 1/5/15 min con número de núcleos.
[🐚 Abrir ejercicio_043.sh](ut2/ejercicio_043.sh){ .md-button }

44. Consulta memoria/swap con `free -h` y contrasta `/proc/meminfo`.
[🐚 Abrir ejercicio_044.sh](ut2/ejercicio_044.sh){ .md-button }

45. Con `df -h`, localiza mayor ocupación y usa `du` en una carpeta propia.
[🐚 Abrir ejercicio_045.sh](ut2/ejercicio_045.sh){ .md-button }

46. Consulta puertos a la escucha con `ss -tulpn` e identifica campos.
[🐚 Abrir ejercicio_046.sh](ut2/ejercicio_046.sh){ .md-button }

47. Toma cinco muestras CPU con `sar -u 1 5` si sysstat está disponible.
[🐚 Abrir ejercicio_047.sh](ut2/ejercicio_047.sh){ .md-button }

48. `journalctl`: mensajes de un servicio última hora y errores del arranque actual.
[🐚 Abrir ejercicio_048.sh](ut2/ejercicio_048.sh){ .md-button }

49. Examina una configuración `logrotate`: frecuencia, rotaciones, compresión, vacíos/ausentes.
[🐚 Abrir ejercicio_049.sh](ut2/ejercicio_049.sh){ .md-button }

50. **Caso de diagnóstico.** Servidor lento: secuencia con `top`, `vmstat`, `free`, `iostat`, `df`, `ss` y `journalctl`, indicando qué confirmas/descartas.
[🐚 Abrir ejercicio_050.sh](ut2/ejercicio_050.sh){ .md-button }
