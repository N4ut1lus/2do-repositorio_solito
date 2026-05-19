# 📘 Guía completa: Crear un repositorio y subirlo a GitHub

Esta guía explica paso a paso cómo:

- Configurar Git por primera vez
- Crear un repositorio local
- Crear un repositorio en GitHub
- Conectar ambos
- Hacer commits
- Subir tu proyecto con `git push`

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

## ✔️ ¡Listo!

Tu repositorio ya está en GitHub.
