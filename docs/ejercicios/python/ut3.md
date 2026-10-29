# UT3 · Control de flujo y bibliotecas sysadmin

50 ejercicios para practicar esta unidad.

!!! note "Organización"
    **1–20:** básicos · **21–40:** intermedios · **41–50:** repaso tipo examen.

## Ejercicio 01 · Mayor de dos números
Pide dos números e indica si el primero es mayor que el segundo.

## Ejercicio 02 · Positivo, negativo o cero
Pide un número y clasifícalo.

## Ejercicio 03 · Par o impar
Pide un entero e indica si es par o impar.

## Ejercicio 04 · División segura
Divide dos números si el segundo no es cero; si lo es, muestra un aviso.

## Ejercicio 05 · Acceso básico
Pide usuario y contraseña. Acepta 'admin' y 'python123'.

## Ejercicio 06 · Cadena en mayúsculas
Pide una cadena e indica si está completamente en mayúsculas.

## Ejercicio 07 · Mayor de tres
Pide tres números y muestra el mayor.

## Ejercicio 08 · Ordenar tres números
Pide tres números y muéstralos de mayor a menor con condicionales.

## Ejercicio 09 · Nota cualitativa
Clasifica una nota de 0 a 10 como suspenso, aprobado, notable o sobresaliente.

## Ejercicio 10 · Mayoría de edad
Pide la edad e indica si es mayor de edad.

## Ejercicio 11 · Múltiplo de 5
Indica si un entero es múltiplo de 5.

## Ejercicio 12 · Múltiplo de 3 y 5
Indica si un entero es divisible a la vez por 3 y 5.

## Ejercicio 13 · Rango permitido
Indica si un número está entre 10 y 20 incluidos.

## Ejercicio 14 · Año bisiesto
Indica si un año es bisiesto: divisible por 4 y no por 100, salvo que también sea divisible por 400.

## Ejercicio 15 · Mes y días
Pide mes 1-12 e indica sus días. Considera febrero de 28 días.

## Ejercicio 16 · Día de la semana
Pide 1-7 y muestra el día correspondiente; otros valores dan error.

## Ejercicio 17 · Cara opuesta de dado
Pide 1-6 y muestra en letras la cara opuesta: 1-6, 2-5, 3-4.

## Ejercicio 18 · Tipo de triángulo
Clasifica tres lados como equilátero, isósceles o escaleno.

## Ejercicio 19 · Triángulo rectángulo
Pide tres lados y comprueba Pitágoras suponiendo que el tercero es la hipotenusa.

## Ejercicio 20 · Potencia según exponente
Exponente positivo: potencia; cero: 1; negativo: 1/potencia con exponente positivo.

## Ejercicio 21 · Descuento por importe
Aplica 5 % si supera 50 €, 10 % si supera 100 € y 15 % si supera 200 €.

## Ejercicio 22 · Precio de entrada por edad
Menores de 5 gratis, 5-17 pagan 5 €, adultos 10 €.

## Ejercicio 23 · Viaje escolar
100+ alumnos: 65 €/alumno; 50-99: 70 €; 30-49: 95 €; menos de 30: autobús fijo 2850 €. Muestra total y coste por alumno.

## Ejercicio 24 · Tipo y tamaño de producto
Pide precio, tipo A/B, tamaño 1/2 y kilos. Ajustes: A1 +0,20; A2 +0,30; B1 -0,30; B2 -0,50. Calcula ganancia.

## Ejercicio 25 · Admisión por nota
'ACEPTADA' si nota >=5, edad >=18 y sexo F; 'POSIBLE' con los mismos requisitos y sexo M; si no, 'NO ACEPTADA'.

## Ejercicio 26 · Peso de paquete
Rechaza paquetes de más de 5 kg.

## Ejercicio 27 · Zona de transporte
Pide zona 1-5 y gramos. Tarifas: 1=24, 2=20, 3=21, 4=10, 5=18 por gramo. Más de 5000 g se rechaza.

## Ejercicio 28 · Alerta de CPU
>=90: CRÍTICO; >=75: ALTO; resto: NORMAL.

## Ejercicio 29 · Alerta de RAM
>=85: ALERTA; resto: OK.

## Ejercicio 30 · Espacio libre mínimo
Menos de 10 GB: ESPACIO BAJO; resto: OK.

## Ejercicio 31 · Validar puerto
Comprueba si un puerto está entre 1 y 65535.

## Ejercicio 32 · Puerto conocido
22=SSH, 80=HTTP, 443=HTTPS; los demás, Otro puerto.

## Ejercicio 33 · Validar hostname
VÁLIDO si empieza por 'PC-' y tiene al menos 7 caracteres.

## Ejercicio 34 · Validar servidor
Válido si empieza por 'SRV-' y tiene al menos 8 caracteres.

## Ejercicio 35 · Entorno por prefijo
'PROD-' = Producción, 'TEST-' = Pruebas; resto = Entorno desconocido.

## Ejercicio 36 · Umbral de disco por argumento
Recibe un umbral por sys.argv, usa shutil.disk_usage y muestra ALERTA si el porcentaje usado es >= umbral; si no, OK.

## Ejercicio 37 · Turno según hora
Usa datetime: antes de 12 Mañana, 12-19 Tarde, desde 20 Noche.

## Ejercicio 38 · Gestor según sistema
Usa platform: Windows=winget, Linux=apt, Darwin=brew, otros=gestor no definido.

## Ejercicio 39 · Ventana de mantenimiento
Usa datetime. Sábado o domingo: Ventana de mantenimiento; resto: Operación normal.

## Ejercicio 40 · Horario laboral
Con datetime, de 8 a 17 inclusive: Horario laboral; resto: Fuera de horario.

## Ejercicio 41 · Crear carpeta backups
Usa pathlib y os. Si 'backups' no existe, créala; si existe, informa de ello.

## Ejercicio 42 · Crear carpeta temp
Usa pathlib. Crea 'temp' solo si falta e informa del resultado.

## Ejercicio 43 · Config de ejemplo
Con pathlib y shutil: si existe config.ini, informa; si falta y existe config.example.ini, cópialo; si falta el ejemplo, avisa.

## Ejercicio 44 · Archivo por tamaño
Recibe archivo por sys.argv y usa pathlib. >=1_048_576 bytes: GRANDE; resto: PEQUEÑO.

## Ejercicio 45 · Log vacío
Recibe archivo por sys.argv. 0 bytes: VACÍO; resto: CON DATOS.

## Ejercicio 46 · Existe archivo
Recibe una ruta por sys.argv y usa pathlib. Muestra EXISTE o NO EXISTE.

## Ejercicio 47 · Archivo o directorio
Recibe una ruta. Muestra ARCHIVO, DIRECTORIO o NO EXISTE.

## Ejercicio 48 · Extensión permitida
PERMITIDO si termina en '.txt' o '.log'; si no, NO PERMITIDO.

## Ejercicio 49 · Nivel de batería simulado
Menos de 10: CRÍTICA; menos de 25: BAJA; resto: OK.

## Ejercicio 50 · Estado de servicio
'running'=Servicio activo; 'stopped'=Servicio detenido; otros=Estado desconocido.