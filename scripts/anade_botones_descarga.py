"""Añade o actualiza el botón de descarga ZIP en cada página de unidad."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = ROOT / "docs" / "ejercicios"

UNIDADES = {
    "python": {"ut1": 50, "ut2": 50, "ut3": 120},
    "aso": {"ut1": 120, "ut2": 50},
    "iaw": {"ut1": 60, "ut2": 50},
}

for asignatura, unidades in UNIDADES.items():
    for unidad, total in unidades.items():
        ruta = BASE / asignatura / f"{unidad}.md"
        texto = ruta.read_text(encoding="utf-8")
        texto = re.sub(
            r"\n\[:material-download: Descargar los \d+ ejercicios[^\n]*\n",
            "\n",
            texto,
            count=1,
        )
        lineas = texto.splitlines()
        posicion = 1
        while posicion < len(lineas) and not lineas[posicion].strip():
            posicion += 1
        # Conserva el párrafo introductorio y coloca el botón justo después.
        while posicion < len(lineas) and lineas[posicion].strip():
            posicion += 1
        boton = (
            f"[:material-download: Descargar los {total} ejercicios de {unidad.upper()}]"
            f"(../descargas/{asignatura}-{unidad}.zip)"
            "{ .md-button .md-button--primary }"
        )
        lineas[posicion:posicion] = ["", boton]
        ruta.write_text("\n".join(lineas).rstrip() + "\n", encoding="utf-8")

print("Botones de descarga añadidos a las páginas de unidad")
