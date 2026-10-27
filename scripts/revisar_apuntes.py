#!/usr/bin/python3
"""Comprueba el código publicado en docs/, sin ejecutar ejemplos sobre datos reales.

Uso: python3 scripts/revisar_apuntes.py [--site-dir RUTA] [--http] [--docker]
Las pruebas crean laboratorios temporales. --http abre un servidor PHP local;
--docker crea y retira un proyecto Compose de prueba con nombre independiente.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
from dataclasses import dataclass
from html.parser import HTMLParser
import http.cookiejar
import json
import os
from pathlib import Path
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
FENCE = re.compile(r'^( *)```([^\n]*)\n(.*?)^\1```', re.M | re.S)
COUNTS = Counter()


@dataclass
class Block:
    path: str
    heading: str
    language: str
    source: str
    line: int


def blocks():
    result = []
    for path in sorted(DOCS.rglob('*.md')):
        text = path.read_text()
        for match in FENCE.finditer(text):
            headings = re.findall(r'^#{1,3} (.+)', text[:match.start()], re.M)
            source = '\n'.join(line[len(match[1]):] if line.startswith(match[1]) else line
                               for line in match[3].splitlines()) + '\n'
            result.append(Block(str(path.relative_to(DOCS)), headings[-1] if headings else '',
                                match[2].split()[0] if match[2].split() else 'text', source,
                                text[:match.start()].count('\n') + 1))
    return result


def run(command, *, cwd, stdin='', expected=None, status=0, env=None):
    completed = subprocess.run(command, cwd=cwd, input=stdin, text=True,
                               capture_output=True, timeout=30, env=env)
    assert completed.returncode == status, (command, completed.stdout, completed.stderr)
    assert not re.search(r'PHP (Warning|Fatal|Parse)', completed.stderr), completed.stderr
    if expected is not None:
        assert completed.stdout == expected, (command, repr(completed.stdout), repr(expected))
    COUNTS['ejecuciones'] += 1
    return completed


def check_sources(all_blocks, work):
    for path in DOCS.rglob('*.md'):
        text = path.read_text()
        masked = FENCE.sub(lambda m: re.sub(r'[^\n]', ' ', m[0]), text)
        for match in re.finditer(r'(?<!`)(`{1,2})(?!`)(.*?)\1(?!`)', masked, re.S):
            assert '\n' not in match[2], (path, 'Código en línea cortado', repr(match[2]))
        if path.parent.name == 'aso':
            assert '#!/usr/bin/env bash' not in text and 'printf' not in text, path
    for number, block in enumerate(all_blocks):
        file = work / f'sintaxis-{number}'
        file.write_text(block.source)
        if block.language == 'python':
            ast.parse(block.source, filename=f'{block.path}:{block.line}')
        elif block.language == 'bash':
            run(['bash', '-n', str(file)], cwd=work)
        elif block.language == 'php':
            run(['php', '-l', str(file)], cwd=work)
            # A short output string should use an explicit escape, not a physical newline.
            program = ('foreach(token_get_all(file_get_contents($argv[1])) as $t){'
                       'if(is_array($t)&&$t[0]===T_CONSTANT_ENCAPSED_STRING&&'
                       'strpos($t[1],"\\n")!==false){exit(1);}}')
            run(['php', '-r', program, str(file)], cwd=work)
        else:
            continue
        COUNTS[f'sintaxis_{block.language}'] += 1


# Each entry corresponds to one complete block, in reading order. Expected
# results are written explicitly; they are not generated from the examples.
PY_CASES = {
'01-entorn.md': [
 ('3\n5\n', []), ('Duración estimada: 6.0 minutos\n', []),
 ('Preparando la revisión\nRevisión preparada\n', [])],
'02-dades.md': [
 ('6 4\n', []), ('Llenos: 3; sobrantes: 5; necesarios: 4\n', []),
 ('12 12 12\n1500.0\nFalse\n', []), ("['rojo', 'azul']\nrojo ROJO\n", []),
 ("['azul', 'gris']\n['azul', 'gris', 'ocre']\n", []), ('Espacio libre: 37\n', []),
 ('True\n', []), ('Taquilla: 007\nLlaves: 5\n', [])],
'03-entrada.md': [
 ('Longitud: 150.0 cm\n', ['1.5']), ('Filamento estimado: 3.00 m\nUnidad: metros\n', ['2.5','1.2']),
 ('666\n18\n18 m\n', []), ("azul / gris -> fin\n'  12  '\n", []),
 ('Documento: guia.pdf -> impresora recepcion\n', ['guia.pdf','recepcion']),
 ('Billetes válidos: 9\n', ['12','3'])],
'04-cadenes.md': [
 ('lam\ninas\nlmns\n', []), ("'  mapa  '\n'mapa'\n", []),
 ('Jazz | directo | FLAC\n2\nTrue True\n', []), ('v n\nvoi\nniloiv\nTrue\n----\n', []),
 ("['azul', '18', 'abierta']\nazul | 18 | abierta\n", []), ('sonido=si\nTrue\n', []),
 ('rojo / verde / azul\n', []), ('borrador - borrador - final\nrevisado - borrador - final\n', [])],
'05-format.md': [
 ('Hay 3 láminas\n4\n', []), ('M-007 | CUARZO | 12.38 g\nmasa=12.375\nEtiqueta literal: {M-007}\n', []),
 ('937\nΩ\nTrue\nFalse\n', []), ('Cuarzo       7\nMica        12\n', []),
 ('Avance: 37.5%\n', []), ('2.72\n2.71828\n', []), ('Caja      4\nSobre    15\n', [])],
'06-control.md': [
 ('Corta\n', []), ('Fragmentos: 3; restante: 2 cm\n', []), ('Material elegido: papel\n', ['vidrio','papel']),
 ('2\n5\n8\n3\n2\n1\n', []), ('1 ocre\n2 azul\n3 gris\n', []),
 ('Hay una nota urgente\n', []), ('Sesiones seleccionadas: 2; minutos: 15\n', []),
 ('Enviar\n', []), ('7\n', []), ('Pendientes antes del bloqueo: 2\n', [])],
'07-errors.md': [
 ('No se ha obtenido una cantidad\nComprobación terminada\n', []),
 ('tarjetas=19, capacidad=6, sobres=4\n', []), ('No se puede interpretar como un entero\n', []),
 ('Escribe un entero\nEl valor está fuera del rango\nPiezas aceptadas: 4\n', ['muchas','0','4']),
 ('9\n', []), ('Turno aceptado\n', ['3']), ('9\n', [])],
'08-biblioteques.md': [
 ('R01 | 26/10/2026\nR02 | 28/10/2026\nR03 | 30/10/2026\n', []),
 ('a.md\nb.md\nDocumentos: 2; bytes: 5\n', []), ('Vitrina revisada\n', []),
 ('Carpeta: fichas; límite: 5\n', []), ('aviso.wav\n.wav\nsonidos\n', []),
 ('Devolución: 03/05/2026\n', []), ('1. revisar batería\n2. guardar cables\n', [])]
}


def check_python(all_blocks, work):
    wrapper = ('import builtins,json,runpy,sys; '
               'path=sys.argv[1]; data=iter(json.loads(sys.argv[2])); '
               'sys.argv=[path]+sys.argv[3:]; '
               'builtins.input=lambda prompt="": next(data); runpy.run_path(path,run_name="__main__")')
    for name, cases in PY_CASES.items():
        selected = [b for b in all_blocks if b.path == 'python-classe/' + name and b.language == 'python']
        assert len(selected) == len(cases), (name, len(selected), len(cases))
        for index, (block, (output, inputs)) in enumerate(zip(selected, cases)):
            folder = work / f'python-{name}-{index}'; folder.mkdir()
            samples = folder / 'muestras'; samples.mkdir()
            (samples/'a.md').write_bytes(b'abc'); (samples/'b.md').write_bytes(b'xy')
            (folder/'recordatorios.txt').write_text('revisar batería\nguardar cables\n')
            file = folder/'ejemplo.py'; file.write_text(block.source)
            args = [str(samples)] if 'sys.argv' in block.source else []
            if 'argparse' in block.source: args = ['fichas','--limite','5']
            run([sys.executable,'-c',wrapper,str(file),json.dumps(inputs),*args], cwd=folder, expected=output)
            if 'Turno: ' in block.source:
                for entry, expected in [('dos','Escribe un entero\n'),('5','Turno fuera de rango\n')]:
                    run([sys.executable,'-c',wrapper,str(file),json.dumps([entry])],cwd=folder,expected=expected)
            if 'sys.argv' in block.source:
                run([sys.executable,'-c',wrapper,str(file),'[]'],cwd=folder,status=1)
                run([sys.executable,'-c',wrapper,str(file),'[]','no-existe'],cwd=folder,status=2)
            if 'argparse' in block.source:
                run([sys.executable,'-c',wrapper,str(file),'[]','fichas','--limite','muchas'],cwd=folder,status=2)
            if 'contacto_disponible = True' in block.source:
                for contact, sent in [(False,False),(False,True),(True,True)]:
                    file.write_text(block.source.replace('contacto_disponible = True',f'contacto_disponible = {contact}')
                                    .replace('aviso_enviado = False',f'aviso_enviado = {sent}'))
                    run([sys.executable,'-c',wrapper,str(file),'[]'],cwd=folder,expected='No enviar\n')
            COUNTS['python_ejecutados'] += 1
    # The other study fragment explicitly contains undefined pseudocode and is syntax-only.
    simple = [b for b in all_blocks if b.path=='estudiar/consells.md' and b.language=='python' and 'numeros = [' in b.source]
    assert len(simple)==1
    file=work/'consejo.py';file.write_text(simple[0].source)
    run([sys.executable,str(file)],cwd=work,expected='[4, 8]\n');COUNTS['python_ejecutados']+=1


BASH_CASES = {
'02-bash-dades.md': [
 ('Carpeta de láminas\nlamina_revisada.txt\n', []), ('Nombre: Láminas grandes\n', []),
 ('Láminas   grandes\nLáminas grandes\nEl contenido de $nombre no se expande aquí\n', []),
 (None, []), ('Muestra: Roca volcánica\nResponsable: Laia Ferrer\nUbicación: Armario azul\n', ['Roca volcánica','Laia Ferrer']),
 ('muestra.version\nmuestra\nSala azul cielo\n2\n', []),
 ('0: Azul cielo\n1: Gris perla\n2: Verde musgo\n', []), ('Argumentos: 2\n<azul>\n<gris claro>\n', ['azul','gris claro']),
 ('lista del club_revisado.csv\n', ['lista del club.csv']), ('Último: jueves\nCantidad: 3\n', [])],
'03-bash-decisions.md': [
 ('Lotes completos: 4; piezas sueltas: 3\n', []), ('La condición se cumple\n', []),
 ('Reserva aceptada. Quedan 7 butacas.\n', ['5']), ('3.50\n', []), ('Opciones: resumen, ayuda\n', []),
 ('Bash está disponible\n', []), ('Documento\n', ['guia.pdf']), ('Preparado\n', ['lleno.txt']),
 ('Hay más unidades disponibles que solicitadas\n', [])],
'04-bash-bucles.md': [
 ('Preparación 1\nPreparación 2\nPreparación 3\nValor al terminar: 4\n', []),
 ('Ficha: Mapa antiguo; zona: Sala azul\nFicha: Plano pequeño; zona: sin_asignar\n', []),
 ('Código recibido: FICHA-AZ\n', []), ('ESTANTERIA-01\nESTANTERIA-02\nESTANTERIA-04\n', []),
 ('Cajas pendientes: 3\nCajas pendientes: 2\nCajas pendientes: 1\nRevisión 1 completada\nRevisión 2 completada\n', []),
 ('CAJA-AB42 es válido\n', []), ('Recibido: [Sala azul]\nRecibido: [Pendiente de revisar]\n', []),
 ('La consulta está preparada\nOpción no reconocida\n', []), ('inicio\nmedio\n', []),
 ('Respuestas afirmativas: 3\n', []), ('Resultado: [Revisión pendiente]\n', [])],
'05-bash-text.md': [
 ('12\n5\n', []), ('17\n', []), (None, []), ('', []), (None, []),
 ('El texto $USER se conserva literalmente.\n', []), ('fichas/sala azul.txt:1:material frágil\n', []),
 ('vista=lista\nsonido=no\n', []), ('hecho hecho listo\n', []), ('documentos/vacio.txt\n', [])],
'06-bash-errors.md': [
 ('Documento: texto corto.txt\nLíneas: 2\n', ['texto corto.txt']), ('', []),
 ('Preparado para revisar: lleno.txt\n', ['lleno.txt']), ('Herramienta disponible\n', []),
 ('Comprobado\nEstado de la prueba: 1\n', [])]
}


def fixture(folder):
    (folder/'notas.txt').write_text('Sala azul\nPendiente de revisar')
    (folder/'piezas.txt').write_text('Azul;12\nGris;3\nAzul;5\nOcre;10\n')
    (folder/'taller.log').write_text('INFO|madera|llegada\nERROR|pintura|falta material\nERROR|madera|pieza rota\nINFO|pintura|revisión\nERROR|pintura|ventilación\n')
    (folder/'lleno.txt').write_text('Texto\n');(folder/'vacio.txt').touch()
    (folder/'texto corto.txt').write_text('primera\nsegunda\n')
    (folder/'opciones.txt').write_text('# preferencias\nvista=lista\n\nsonido=no\n')
    (folder/'fichas').mkdir();(folder/'fichas/sala azul.txt').write_text('material frágil\n')
    (folder/'fichas/sala gris.txt').write_text('material normal\n')
    (folder/'documentos').mkdir();(folder/'documentos/vacio.txt').touch()
    (folder/'documentos/lleno.txt').write_text('texto');(folder/'documentos/vacio.csv').touch()
    (folder/'documentos/carpeta.txt').mkdir()


def check_bash(all_blocks, work):
    for name, cases in BASH_CASES.items():
        selected=[b for b in all_blocks if b.path=='aso/'+name and b.language=='bash']
        assert len(selected)==len(cases),(name,len(selected),len(cases))
        for index,(block,(output,args)) in enumerate(zip(selected,cases)):
            folder=work/f'bash-{name}-{index}';folder.mkdir();fixture(folder)
            file=folder/'ejemplo.sh';file.write_text(block.source)
            stdin=''
            if 'Ubicación de la muestra:' in block.source:stdin='Armario azul\n'
            if 'Escribe ver o salir:' in block.source:stdin='ver\notra\nsalir\n'
            if '| bc' in block.source and not shutil.which('bc'):
                COUNTS['bc_no_disponible']+=1
                continue
            result=run(['bash',str(file),*args],cwd=folder,stdin=stdin,expected=output)
            if 'Fecha del informe:' in block.source:
                assert re.fullmatch(r'Fecha del informe: \d{4}-\d{2}-\d{2}\n',result.stdout)
            if 'uniq -c' in block.source:
                report=(folder/'resumen.txt').read_text() if '> resumen.txt' in block.source else result.stdout
                assert dict((word,int(n)) for n,word in re.findall(r'(\d+) (\S+)',report))=={'madera':1,'pintura':2}
            if 'wc -l < taller.log' in block.source:assert result.stdout.endswith('5\n')
            if 'echo "Argumentos: $#"' in block.source:
                run(['bash',str(file)],cwd=folder,expected='Argumentos: 0\n')
                run(['bash',str(file),''],cwd=folder,expected='Argumentos: 1\n<>\n')
            if 'peticion=${1:-}' in block.source:
                for arg,expected,status in [('12','La sala queda completa.\n',0),('13','No hay suficientes butacas.\n',0),('cero','',1),('0','',1)]:
                    run(['bash',str(file),arg],cwd=folder,expected=expected,status=status)
                run(['bash',str(file)],cwd=folder,status=1)
            if 'if lin' in block.source:
                run(['bash',str(file)],cwd=folder,status=1)
                run(['bash',str(file),'ausente'],cwd=folder,status=2)
            if '[[ -f "$1" && -s' in block.source:
                for arg in ['vacio.txt','documentos']:
                    run(['bash',str(file),arg],cwd=folder,expected='No válido\n')
            if 'command -v wc' in block.source:
                env=os.environ.copy();env['PATH']='/no-existe'
                run(['/bin/bash',str(file)],cwd=folder,env=env,status=2)
            COUNTS['bash_aso_ejecutados']+=1


def check_php(all_blocks,work):
    exact={
      'Leer una asignación de derecha a izquierda':'7\n5\n',
      'Concatenación e interpolación':'Sala: Azul\nSala: Azul\nSala: $sala\n',
      'Texto, tipos y operaciones que conviene distinguir':'SALA AZUL\nsala verde\n',
      '1. Calcula el material que falta':'Faltan 8 hojas\n',
      '2. Comprueba cuándo se calcula un valor':'7\n11\n',
      '3. Une texto sin ejecutar etiquetas':'<p>&lt;em&gt;Rutas del barrio&lt;/em&gt;</p>',
      'Un array reúne datos que vas a tratar de la misma manera':'Azul: 18 plazas\nGris: 12 plazas\n',
      'Crear una función significa poner nombre a una tarea':'7 / 8\n',
      'Problema explicado paso a paso: preparar cajas de libros':'Poesía: 3 cajas\nTeatro: 1 cajas\nEnsayo: 1 cajas\nTotal: 5 cajas\n',
      'Decisiones con ejemplos pequeños':'Hay que continuar\nEscuchar',
      'Repetir con contador o condición':'Turno 1\nTurno 2\nTurno 3\nQuedan 2\nQuedan 1\n',
      'Parámetros opcionales y responsabilidad local':'Sala: Azul\nZona: Azul\n',
      '1. Muestra solo tareas pendientes':'pendiente\npendiente\n',
      '2. Una función que responde una pregunta':'bool(false)\nbool(true)\n',
      '3. Suma solo las cantidades positivas':'7\n',
      'XSS: validar no sustituye escapar':'&lt;b&gt;Revisar vitrina&lt;/b&gt;',
      'Dónde mirar según el síntoma':''}
    for index,block in enumerate(b for b in all_blocks if b.language=='php'):
        folder=work/f'php-{index}';folder.mkdir();file=folder/'ejemplo.php';file.write_text(block.source)
        if block.heading in exact:
            run(['php',str(file)],cwd=folder,expected=exact[block.heading]);COUNTS['php_cli_ejecutados']+=1
        elif block.heading=='2. Valida una opción de formato':
            driver=folder/'driver.php';driver.write_text('<?php $_POST=json_decode($argv[1],true); include $argv[2];')
            for data,expected in [({},'Elige pdf o texto'),({'formato':'pdf'},'Formato aceptado'),({'formato':'texto'},'Formato aceptado'),({'formato':'x'},'Elige pdf o texto'),({'formato':['pdf']},'Elige pdf o texto')]:
                run(['php',str(driver),json.dumps(data),str(file)],cwd=folder,expected=expected)
            COUNTS['php_cli_ejecutados']+=1
        elif block.heading=='3. Conserva una nota después de un error':
            driver=folder/'driver.php';driver.write_text("<?php $nota='<b>Nota</b>'; include $argv[1];")
            run(['php',str(driver),str(file)],cwd=folder,expected='<textarea name="nota">&lt;b&gt;Nota&lt;/b&gt;</textarea>\n')
            COUNTS['php_cli_ejecutados']+=1
        elif block.heading=='2. Por qué falla una redirección':
            driver=folder/'driver.php';driver.write_text('<?php register_shutdown_function(function(){echo http_response_code();}); include $argv[1];')
            run(['php',str(driver),str(file)],cwd=folder,expected='303');COUNTS['php_cli_ejecutados']+=1


def git_env():
    env=os.environ.copy();env.update(GIT_CONFIG_GLOBAL='/dev/null',GIT_CONFIG_NOSYSTEM='1',GIT_TERMINAL_PROMPT='0')
    return env


def check_git(all_blocks,work):
    selected=[b for b in all_blocks if b.path=='git-github/index.md' and b.language=='bash']
    assert len(selected)==5
    env=git_env()
    # First two snippets form a single documented laboratory.
    first=work/'git-inventario';first.mkdir()
    for index,block in enumerate(selected):
        if index<2:folder=first if index==0 else first/'inventario-lab'
        else:
            folder=work/f'git-practica-{index}';folder.mkdir()
            run(['git','init','-b','main'],cwd=folder,env=env)
            run(['git','config','user.name','Estudiante'],cwd=folder,env=env)
            run(['git','config','user.email','estudiante@example.com'],cwd=folder,env=env)
            (folder/'manual.txt').write_text('Inicial\n');(folder/'tareas.txt').write_text('Inicial\n')
            run(['git','add','manual.txt','tareas.txt'],cwd=folder,env=env)
            run(['git','commit','-m','Inicio'],cwd=folder,env=env)
        file=work/f'git-snippet-{index}.sh';file.write_text(block.source)
        if index==3:(folder/'.gitignore').write_text('*.log\n')
        run(['bash',str(file)],cwd=folder,env=env)
        if index==1:assert (folder/'ubicacion.txt').read_text()=='Ubicación: armario azul\n'
        if index==2:
            run(['git','diff','--cached','--name-only'],cwd=folder,env=env,expected='manual.txt\n')
            run(['git','diff','--name-only'],cwd=folder,env=env,expected='tareas.txt\n')
        if index==3:
            assert (folder/'.gitignore').read_text()=='*.log\n*.tmp\n'
            assert (folder/'borrador.tmp').exists()
            run(['git','check-ignore','borrador.tmp'],cwd=folder,env=env,expected='borrador.tmp\n')
        if index==4:
            run(['git','branch','--show-current'],cwd=folder,env=env,expected='main\n')
            assert not (folder/'uso.txt').exists()
            run(['git','show','instrucciones:uso.txt'],cwd=folder,env=env,expected='Leer antes de empezar\n')
        COUNTS['git_laboratorios']+=1


class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=set();self.links=[];self.tables=[];self.table=None;self.row=None
        self.details=[];self.detail=None;self.in_summary=False;self.language=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.language=a.get('lang')
        if 'id' in a:self.ids.add(a['id'])
        if tag=='a' and 'href' in a:self.links.append(a['href'])
        if tag=='table':self.table=[]
        if tag=='tr' and self.table is not None:self.row=0
        if tag in ['td','th'] and self.row is not None:self.row+=1
        if tag=='details':self.detail={'open':'open' in a,'title':''}
        if tag=='summary':self.in_summary=True
    def handle_data(self,data):
        if self.in_summary and self.detail is not None:self.detail['title']+=data
    def handle_endtag(self,tag):
        if tag=='tr' and self.table is not None:self.table.append(self.row);self.row=None
        if tag=='table':self.tables.append(self.table);self.table=None
        if tag=='summary':self.in_summary=False
        if tag=='details' and self.detail is not None:self.details.append(self.detail);self.detail=None


def check_site(site):
    site=site.resolve();pages={}
    for file in site.rglob('*.html'):
        page=Page();page.feed(file.read_text());pages[file.resolve()]=page
        assert page.language=='es',file
        for table in page.tables:
            assert table and all(n==table[0] for n in table),(file,table)
        for detail in page.details:
            if detail['title'].strip() in ['Pista','Solución paso a paso']:
                assert not detail['open'],file
                COUNTS['pistas' if detail['title'].strip()=='Pista' else 'soluciones']+=1
    for file,page in pages.items():
        for link in page.links:
            parsed=urllib.parse.urlsplit(link)
            if parsed.scheme or parsed.netloc:continue
            if parsed.path.startswith('/'):continue  # theme-level links outside this Pages prefix
            target=(file.parent/urllib.parse.unquote(parsed.path)).resolve() if parsed.path else file
            if target.is_dir():target=target/'index.html'
            assert target.exists(),(file,link)
            if parsed.fragment and target in pages:
                assert urllib.parse.unquote(parsed.fragment) in pages[target].ids,(file,link)
    assert COUNTS['soluciones']==84 and COUNTS['pistas']==84,COUNTS
    for old in ['archivo','bash','python','git','docker','php','powershell','xuletes','glossari']:
        assert not (site/old).exists(),old
    search=json.loads((site/'search/search_index.json').read_text())
    assert not any(d['location'].split('/')[0] in ['archivo','bash','python','git','docker','php','powershell','xuletes','glossari'] for d in search['docs'])
    COUNTS['paginas_html']=len(pages)


def select(all_blocks,path,language):
    return [b for b in all_blocks if b.path==path and b.language==language]


def check_http(all_blocks,work):
    folder=work/'servidor';folder.mkdir()
    (folder/'turno.php').write_text(select(all_blocks,'iaw/06-formularis.md','php')[0].source)
    state=select(all_blocks,'iaw/07-estat.md','php')
    hashed=run(['php','-r','echo password_hash("Partitura!47", PASSWORD_DEFAULT);'],cwd=folder).stdout
    for name,block in zip(['vista.php','usuarios.php','acceso.php','archivo.php','salir.php','rol-archivo.php','rol-editor.php'],state):
        (folder/name).write_text(block.source.replace('PEGA_AQUI_EL_HASH_GENERADO',hashed))
    with socket.socket() as probe:
        probe.bind(('127.0.0.1',0));port=probe.getsockname()[1]
    with (folder/'server.log').open('w') as log:
        server=subprocess.Popen(['php','-S',f'127.0.0.1:{port}','-t',str(folder)],stdout=log,stderr=log)
        try:
            for _ in range(50):
                try:
                    with socket.create_connection(('127.0.0.1',port),timeout=.1):break
                except OSError:time.sleep(.1)
            else:raise AssertionError('No arrancó el servidor PHP')
            def client():return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
            a,b=client(),client()
            def get(client,path,data=None):
                encoded=urllib.parse.urlencode(data,doseq=True).encode() if data is not None else None
                try:
                    response=client.open(f'http://127.0.0.1:{port}/'+path,encoded,timeout=5)
                    return response.status,response.url,response.read().decode()
                except urllib.error.HTTPError as error:return error.code,error.url,error.read().decode()
            assert 'Solicitud válida' not in get(a,'turno.php')[2]
            for minutes in ['5','15','40']:
                assert 'Solicitud válida' in get(a,'turno.php',{'equipo':'refractor','minutos':minutes,'recoger':'si'})[2]
            for minutes in ['4','41','muchos','']:
                body=get(a,'turno.php',{'equipo':'reflector','minutos':minutes,'recoger':'si'})[2]
                assert 'La duración debe ser' in body and 'Solicitud válida' not in body
            body=get(a,'turno.php',{'equipo':'inventado','minutos':'20'})[2]
            assert 'value="20"' in body and 'Elige uno de los dos' in body and 'Debes aceptar' in body
            assert 'Solicitud válida' not in get(a,'turno.php',{'equipo[]':'refractor','minutos[]':'15','recoger[]':'si'})[2]
            assert 'Vista: cuadricula' in get(a,'vista.php')[2]
            assert 'Vista: lista' in get(a,'vista.php',{'vista':'lista'})[2]
            assert 'Vista: cuadricula' in get(b,'vista.php')[2]
            assert get(a,'archivo.php')[1].endswith('acceso.php')
            assert 'No se ha podido validar' in get(a,'acceso.php',{'usuario':'archivero','clave':'mal'})[2]
            assert 'Identidad: archivero' in get(a,'acceso.php',{'usuario':'archivero','clave':'Partitura!47'})[2]
            assert get(b,'archivo.php')[1].endswith('acceso.php')
            assert get(a,'rol-editor.php')[0]==403
            assert get(a,'salir.php')[0]==405
            get(a,'salir.php',{})
            assert get(a,'archivo.php')[1].endswith('acceso.php')
            COUNTS['http_formularios_sesiones']=1
        finally:
            server.terminate();server.wait(timeout=5)


def check_docker(all_blocks,work):
    folder=work/'compose';(folder/'public').mkdir(parents=True)
    for language,name in [('yaml','compose.yaml'),('nginx','web.conf'),('php','public/index.php'),('dotenv','.env')]:
        (folder/name).write_text(select(all_blocks,'iaw/03-entorn.md',language)[0].source)
    project='asir-revision-'+uuid.uuid4().hex[:10]
    # Preserve the documented loopback binding, replacing only the host port.
    with socket.socket() as probe:
        probe.bind(('127.0.0.1',0));port=probe.getsockname()[1]
    (folder/'.env').write_text(f'WEB_PORT={port}\n')
    command=['docker','compose','--project-name',project,'--file',str(folder/'compose.yaml')]
    subprocess.run(command+['config','--quiet'],cwd=folder,check=True)
    try:
        subprocess.run(command+['up','-d'],cwd=folder,check=True,timeout=240)
        for _ in range(60):
            try:
                response=urllib.request.urlopen(f'http://127.0.0.1:{port}/',timeout=2)
                assert response.status==200 and 'Sesión de cortometrajes' in response.read().decode()
                break
            except (urllib.error.URLError,AssertionError):time.sleep(.25)
        else:raise AssertionError('El stack no devolvió la cartelera esperada')
        COUNTS['docker_stack_completo']=1
    finally:
        subprocess.run(command+['down','--volumes','--remove-orphans'],cwd=folder,check=True,timeout=60)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site-dir',type=Path)
    parser.add_argument('--http',action='store_true')
    parser.add_argument('--docker',action='store_true')
    args=parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='asir-revision-') as temp:
        work=Path(temp);all_blocks=blocks()
        check_sources(all_blocks,work);check_python(all_blocks,work);check_bash(all_blocks,work)
        check_php(all_blocks,work);check_git(all_blocks,work)
        if args.site_dir:check_site(args.site_dir)
        if args.http:check_http(all_blocks,work)
        if args.docker:check_docker(all_blocks,work)
    print(json.dumps(dict(COUNTS),ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
