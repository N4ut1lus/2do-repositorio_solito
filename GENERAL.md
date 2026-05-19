# 📘 Guía completa: Crear un repositorio y subirlo a GitHub

Esta guía explica paso a paso cómo:

- Configurar Git por primera vez
- Crear un repositorio local
- Crear un repositorio en GitHub
- Conectar ambos
- Hacer commits
- Subir tu proyecto con `git push`
- Solucionar el error “fetch first”

---

## 🔷 1. Configurar Git por primera vez

```bash
git config --global user.name "TU_USUARIO"
git config --global user.email "TU_CORREO"
```

---

## 🔷 2. Crear un repositorio local

```bash
git init
```

![Ejemplo git init](https://user-images.githubusercontent.com/99184393/235310078-4c8a3c8e-9e4f-4b2f-9c7e-1c4b2e3e1f0a.png)

---

## 🔷 3. Añadir archivos y hacer commit

```bash
git add .
git commit -m "Primer commit del proyecto"
```

---

## 🔷 4. Crear un repositorio en GitHub

![Crear repo](https://user-images.githubusercontent.com/99184393/235310210-1f4c3d8e-8e4b-4c7b-9c3b-2c4b1e1f0a7c.png)

GitHub te dará una URL como:

```
https://github.com/TU_USUARIO/TU_REPO.git
```

---

## 🔷 5. Conectar tu repositorio local con GitHub

```bash
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git remote -v
```

---

## 🔷 6. Subir tu proyecto a GitHub

```bash
git push -u origin master
```

---

# 🟥 Solución al error “fetch first”

Si al hacer push aparece:

```
! [rejected] master -> master (fetch first)
error: failed to push some refs
hint: Updates were rejected because the remote contains work that you do not have locally.
```

Significa que **GitHub tiene archivos que tú no tienes localmente**.

---

## 🔷 7.1 Solución recomendada (merge)

### Paso 1 — Indicar a Git que quieres usar merge

```bash
git config pull.rebase false
```

### Paso 2 — Traer los cambios del remoto

```bash
git pull origin master
```

### Paso 3 — Subir tus cambios

```bash
git push -u origin master
```

---

## 🔷 7.2 Solución alternativa (forzar el push)

⚠️ Esto BORRA lo que está en GitHub y lo reemplaza por tu versión local.

```bash
git push -u origin master --force
```

---

## ✔️ ¡Listo!

Tu repositorio ya está en GitHub y sabes cómo resolver el error “fetch first”.
