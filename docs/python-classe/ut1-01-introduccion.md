# UT1 · 1.1 Introducción a la programación y a Python

## Qué debes aprender

En este tema hay que entender **qué significa programar**, por qué utilizamos lenguajes de programación, qué lugar ocupa Python y qué ocurre, de forma simplificada, cuando ejecutamos un programa.

Programar consiste en dar instrucciones a un ordenador para resolver una tarea. Esas instrucciones deben ser precisas: el ordenador no interpreta ambigüedades como una persona.

!!! important "Idea clave"
    Aprender a programar no consiste en memorizar órdenes. Consiste en **aprender a resolver problemas paso a paso**.

## Pensar antes de escribir código

Si queremos calcular el precio final de un producto con IVA, primero podemos expresar el algoritmo:

1. Conocer el precio sin IVA.
2. Calcular el IVA.
3. Sumarlo al precio inicial.
4. Mostrar el resultado.

```python
precio = 100
iva = precio * 0.21
precio_final = precio + iva
print(precio_final)
```

Lo importante no es solo conocer `print()`: debes poder explicar **qué datos tienes, qué operación haces y qué resultado obtienes**.

## Lenguajes de alto y bajo nivel

Los ordenadores ejecutan internamente instrucciones muy cercanas al código máquina. Para las personas resulta mucho más cómodo utilizar lenguajes de programación de nivel superior.

| Tipo | Idea principal |
| --- | --- |
| Código máquina | Lo ejecuta directamente la CPU |
| Ensamblador | Muy cercano al procesador |
| C | Suele considerarse de nivel medio o intermedio |
| Python | Lenguaje de alto nivel, legible y expresivo |

Python permite escribir instrucciones bastante fáciles de entender:

```python
print("Hola, mundo")
```

## Código fuente, bytecode e intérprete

Un programa Python se guarda normalmente en un archivo con extensión `.py`. Ese archivo contiene el **código fuente**.

De forma simplificada, al ejecutarlo ocurre esto:

1. Escribes el código fuente en un archivo `.py`.
2. Python analiza el código.
3. Genera una representación intermedia llamada **bytecode**.
4. La máquina virtual de Python interpreta ese bytecode.

Por eso se suele decir que Python es un lenguaje interpretado, aunque exista ese paso intermedio.

```text
código fuente (.py)
        ↓
     Python
        ↓
     bytecode
        ↓
máquina virtual de Python
        ↓
    ejecución
```

No necesitas memorizar los detalles internos. Para el examen debes distinguir **código fuente**, **bytecode** e **intérprete**.

## Características de Python

Python es:

- legible;
- de propósito general;
- multiplataforma;
- multiparadigma;
- adecuado para scripts pequeños;
- acompañado de una biblioteca estándar muy amplia;
- utilizado tanto para aprender como profesionalmente.

En ASIR nos interesa especialmente para **automatizar tareas de administración**: procesar logs, revisar archivos, consultar rutas, organizar carpetas o comprobar información del sistema.

## Legibilidad y simplicidad

El *Zen de Python* reúne principios de estilo del lenguaje. En este nivel basta con recordar dos ideas:

- lo simple suele ser mejor que lo complicado;
- la legibilidad importa.

Una solución que puedes explicar suele ser mejor que una solución rebuscada que solo funciona porque la has copiado.

## Primer programa

```python
print("Hola, mundo")
```

`print()` muestra información por pantalla. El texto está entre comillas porque es una cadena (`str`).

También podemos mostrar variables:

```python
nombre = "Ana"
edad = 20

print("Nombre:", nombre)
print("Edad:", edad)
```

Salida:

```text
Nombre: Ana
Edad: 20
```

## Comentarios

Los comentarios empiezan por `#` y Python no los ejecuta.

```python
# Precio sin IVA
precio = 100

# Calculamos el precio final aplicando un IVA del 21 %
precio_final = precio * 1.21
print(precio_final)
```

Un comentario debe aportar información. Evita repetir literalmente lo que ya dice una instrucción sencilla.

## Errores frecuentes

### Olvidar las comillas

```python
print(Hola)
```

Python interpreta `Hola` como el nombre de una variable. Si no existe, aparece un error.

```python
print("Hola")
```

### Confundir mayúsculas y minúsculas

Python distingue mayúsculas de minúsculas:

```python
Print("Hola")  # Incorrecto
print("Hola")  # Correcto
```

### No leer el mensaje de error

Cuando Python falla, normalmente indica el archivo, una línea aproximada, el tipo de error y una explicación. El error es información útil para localizar el problema.

## Ejemplo explicado

Queremos calcular cuántos minutos tardaremos en leer 840 palabras a un ritmo de 140 palabras por minuto.

```python
palabras = 840
ritmo = 140
minutos = palabras / ritmo
print(minutos)
```

Resultado:

```text
6.0
```

El razonamiento es:

1. Tenemos 840 palabras.
2. Leemos 140 por minuto.
3. Dividimos `840 / 140`.
4. Obtenemos 6 minutos.

## Comprueba que sabes...

- Explicar qué significa programar.
- Entender que programar es resolver problemas paso a paso.
- Distinguir código fuente, bytecode e intérprete.
- Explicar por qué Python es un lenguaje de alto nivel.
- Reconocer usos de Python relacionados con ASIR.
- Escribir un primer `print()`.
- Utilizar comentarios sencillos.
- Entender que Python distingue mayúsculas y minúsculas.

!!! success "Para el examen"
    Si te dan un problema sencillo, intenta explicar primero **entrada → proceso → salida** y después escribe el código.

---

Fuente principal: material de clase **Introducción a Python 1.1 · Introducción a la programación y a Python**, consultado el 29/10/2026. Los ejemplos adicionales mantienen el nivel del tema.