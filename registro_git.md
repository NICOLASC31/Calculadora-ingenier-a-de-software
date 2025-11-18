# Registro de flujo Git/GitHub

Este documento sirve como guía y bitácora del taller. Incluye la explicación de
los comandos solicitados y un espacio para evidenciar la ejecución (texto o
capturas). Cúbrelo en equipo mientras desarrollan la calculadora.

> **Tip:** Para cada paso, ejecuta `git status` antes y después para
> contextualizar los cambios.

---

## 1. Inicialización del repositorio

- `git init`: crea la carpeta `.git` con el historial vacío.
  - Ejemplo: `git init`
  - Evidencia: _captura de la terminal mostrando el mensaje de inicialización_

## 2. Primer snapshot

- `git add .`: mueve los archivos al área de preparación.
- `git commit -m "chore: initial project structure"`: crea el primer commit.
- `git log --oneline`: confirma que el commit quedó registrado.

Evidencia sugerida:
- Captura de `git status` → `git add .` → `git commit`.
- Fragmento de `git log --oneline`.

## 3. Conectar con GitHub

- Crear el repositorio remoto y copiar la URL.
- `git remote add origin https://github.com/tu-usuario/calculadora.git`
- `git push -u origin master` (o `main`).

Evidencia: salida del primer `git push` y captura del repo en GitHub.

## 4. Trabajo en ramas (pareja A)

- `git checkout -b rama-heroes`: crea la rama de funcionalidad.
- Implementar suma/resta y documentar los cambios.
- `git add .` + `git commit -m "feat: add sum and subtract"`
- `git push -u origin rama-heroes`

Registro: describir qué archivos cambiaron y adjuntar la evidencia del push.

## 5. Revisión de pareja B

- `git checkout rama-heroes`
- Ajustes necesarios (`git commit -am "fix: validate inputs"`)
- `git push`

Anotar brevemente los comentarios/revisiones realizadas en GitHub.

## 6. Volver a la rama principal y fusionar

- `git checkout master`
- `git merge rama-heroes`
- Resolver conflictos si aparecen.
- Guardar el mensaje del merge (si se abre Vim → `ESC :wq!`).
- `git branch -d rama-heroes` para limpiar la rama local.
- `git push` para actualizar el remoto.

Evidencia:
- Captura de la resolución de conflictos (si aplica).
- Salida del merge y eliminación de la rama.

## 7. Uso de `git reset .` y `git checkout -- .`

Describe un escenario breve donde:
- Modifican un archivo, lo agregan a staging y luego usan `git reset .` para
  retirarlo sin perder cambios.
- Usan `git checkout -- .` para descartar cambios locales.

Incluye capturas de cada comando para demostrar su efecto.

## 8. Ejemplo de `git commit --amend`

- Repite un commit pequeño y luego corrige el mensaje o añade un archivo
  olvidado usando: `git commit --amend -m "mensaje nuevo"`.
- Explica por qué lo usaron y adjunta la evidencia.

## 9. Uso de `git switch -c`

- Como alternativa a `git checkout -b`, crea otra rama rápida para una mejora
  menor: `git switch -c mejora-ui`.
- Describe qué cambio se hizo y cómo se integró (merge o eliminación).

## 10. Resumen final

- Lista de commits (mínimo 5) con mensajes claros.
- Historial de merges realizados (`git log --graph --oneline --all` sugerido).
- Enlace al repositorio en GitHub.
- Notas finales del equipo (retos, aprendizajes, pendientes).

---

### Checklist de entregables

- [ ] Código fuente (`calculator.py`) con operaciones básicas.
- [ ] Al menos 5 commits documentados.
- [ ] Evidencias (capturas o referencias) de cada comando clave.
- [ ] Rama de trabajo creada, fusionada y eliminada.
- [ ] Uso de `git commit --amend`, `git reset .`, `git checkout -- .`,
      `git switch -c`.
- [ ] Repositorio en GitHub con README y este registro completado.

---

## Bitácora rápida (ejemplo real)

- `2025-11-18 08:30` – `git init`, primer commit (`chore: initial project setup`) y
  `git push -u origin main`.
- `08:40` – `git checkout -b rama-heroes`, desarrollo del botón `+/-`, uso de
  `git reset .` para deshacer el staging y `git commit --amend` para corregir el
  mensaje; push a la rama y Pull Request.
- `08:50` – `git checkout main`, `git merge rama-heroes`, `git branch -d
  rama-heroes`, `git checkout -- .` para descartar pruebas locales.
- `09:00` – `git switch -c mejora-ui`, actualización de la guía colaborativa,
  `git commit -am "docs: add collaborative workflow"`, push y merge.
- `09:10` – Limpieza (`.gitignore`) y actualización de este registro con las
  evidencias.
