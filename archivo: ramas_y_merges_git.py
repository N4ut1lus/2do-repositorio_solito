"""
Este archivo explica cómo funcionan las ramas (branches) en Git,
cómo crearlas, cambiar entre ellas, fusionarlas (merge) y subirlas
a GitHub.

──────────────────────────────────────────────────────────────
1. ¿QUÉ ES UNA RAMA?
──────────────────────────────────────────────────────────────

Una rama es una línea de trabajo independiente.
Sirve para trabajar en nuevas funciones sin romper el código principal.

La rama principal suele llamarse:
    master
o
    main

──────────────────────────────────────────────────────────────
2. VER LAS RAMAS EXISTENTES
──────────────────────────────────────────────────────────────

    git branch

Muestra todas las ramas locales.
La rama con * es la que estás usando.


──────────────────────────────────────────────────────────────
3. CREAR UNA RAMA NUEVA
──────────────────────────────────────────────────────────────

    git branch nombre-de-la-rama

Ejemplo:
    git branch rama-01


──────────────────────────────────────────────────────────────
4. CAMBIAR A UNA RAMA
──────────────────────────────────────────────────────────────

    git checkout nombre-de-la-rama

Ejemplo:
    git checkout rama-01


──────────────────────────────────────────────────────────────
5. CREAR Y CAMBIAR A LA RAMA EN UN SOLO PASO
──────────────────────────────────────────────────────────────

    git checkout -b rama-02


──────────────────────────────────────────────────────────────
6. HACER CAMBIOS Y GUARDARLOS EN LA RAMA
──────────────────────────────────────────────────────────────

Después de editar archivos:

    git add .
    git commit -m "Descripción del cambio en esta rama"


──────────────────────────────────────────────────────────────
7. VOLVER A LA RAMA PRINCIPAL
──────────────────────────────────────────────────────────────

    git checkout master
o
    git checkout main


──────────────────────────────────────────────────────────────
8. FUSIONAR UNA RAMA (MERGE)
──────────────────────────────────────────────────────────────

Desde la rama principal:

    git merge rama-01

Esto trae los cambios de rama-01 a master/main.


──────────────────────────────────────────────────────────────
9. ELIMINAR UNA RAMA QUE YA SE USÓ
──────────────────────────────────────────────────────────────

    git branch -d rama-01


──────────────────────────────────────────────────────────────
10. SUBIR UNA RAMA A GITHUB
──────────────────────────────────────────────────────────────

Si la rama es nueva:

    git push -u origin nombre-de-la-rama

Ejemplo:
    git push -u origin rama-01


──────────────────────────────────────────────────────────────
11. VER EL HISTORIAL DE TODAS LAS RAMAS
──────────────────────────────────────────────────────────────

    git log --oneline --graph --all --decorate

Este comando muestra un gráfico visual de todas las ramas
y cómo se conectan entre sí.


──────────────────────────────────────────────────────────────

Este archivo sirve como guía rápida para recordar cómo trabajar
con ramas y merges en Git y GitHub.
"""
