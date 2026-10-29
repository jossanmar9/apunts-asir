"""Genera ZIP descargables por unidad y por asignatura."""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = ROOT / "docs" / "ejercicios"
DOWNLOADS = BASE / "descargas"

UNIDADES = {
    "python": ["ut1", "ut2", "ut3"],
    "aso": ["ut1", "ut2"],
    "iaw": ["ut1", "ut2"],
}


def archivos_de(carpeta):
    return sorted(p for p in carpeta.rglob("*") if p.is_file())


def crear_zip(destino, archivos, base):
    destino.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as zf:
        for archivo in archivos:
            zf.write(archivo, archivo.relative_to(base))


DOWNLOADS.mkdir(parents=True, exist_ok=True)

for asignatura, unidades in UNIDADES.items():
    todos = []
    for unidad in unidades:
        carpeta = BASE / asignatura / unidad
        archivos = archivos_de(carpeta)
        if not archivos:
            raise SystemExit(f"No hay ejercicios en {carpeta}")
        crear_zip(DOWNLOADS / f"{asignatura}-{unidad}.zip", archivos, carpeta)
        todos.extend(archivos)

    crear_zip(
        DOWNLOADS / f"{asignatura}-todos.zip",
        todos,
        BASE / asignatura,
    )

print("ZIP de ejercicios generados correctamente")
