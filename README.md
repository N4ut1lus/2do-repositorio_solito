"""
Este archivo explica paso a paso cómo crear un repositorio en Git,
configurar Git por primera vez, enlazarlo con GitHub y subir tus archivos.

──────────────────────────────────────────────────────────────
1. CONFIGURAR GIT POR PRIMERA VEZ
──────────────────────────────────────────────────────────────

Solo se hace una vez en tu vida (o cuando reinstalas Git).

    git config --global user.name "TU_USUARIO"
    git config --global user.email "TU_CORREO"

Ejemplo real:
    git config --global user.name "N4ut1lus"
    git config --global user.email "tucorreo@ejemplo.com"

Puedes verificarlo con:
    git config --list


──────────────────────────────────────────────────────────────
2. CREAR UN REPOSITORIO LOCAL
──────────────────────────────────────────────────────────────

En la carpeta donde quieras trabajar:

    git init

Esto crea un repositorio vacío.


──────────────────────────────────────────────────────────────
3. AÑADIR ARCHIVOS AL REPOSITORIO
──────────────────────────────────────────────────────────────

Cuando tengas archivos listos:

    git add .

Esto añade todos los archivos al "stage".

Luego haces el commit:

    git commit -m "Primer commit del proyecto"


──────────────────────────────────────────────────────────────
4. CREAR EL REPOSITORIO EN GITHUB
──────────────────────────────────────────────────────────────

En GitHub:
- Clic en "New repository"
- Le pones un nombre (ej: 2do-repositorio_solito)
- NO añadas README (para evitar conflictos)
- Crear repositorio

GitHub te mostrará una URL como:

    https://github.com/N4ut1lus/2do-repositorio_solito.git


──────────────────────────────────────────────────────────────
5. CONECTAR TU REPO LOCAL CON GITHUB
──────────────────────────────────────────────────────────────

En tu terminal, dentro del proyecto:

    git remote add origin https://github.com/N4ut1lus/2do-repositorio_solito.git

Puedes verificarlo con:

    git remote -v


──────────────────────────────────────────────────────────────
6. HACER PUSH POR PRIMERA VEZ
──────────────────────────────────────────────────────────────

Si tu rama principal se llama "master":

    git push -u origin master

Si se llama "main":

    git push -u origin main

Git te pedirá:

    Username: tu usuario de GitHub (ej: N4ut1lus)
    Password: tu TOKEN de GitHub (NO tu contraseña)

──────────────────────────────────────────────────────────────
7. LISTO: TU REPOSITORIO YA ESTÁ EN GITHUB
──────────────────────────────────────────────────────────────

Cada vez que hagas cambios:

    git add .
    git commit -m "Descripción del cambio"
    git push

──────────────────────────────────────────────────────────────

Este archivo es solo una guía dentro de Python para recordarte
todo el proceso de creación y subida de un repositorio a GitHub.
"""
