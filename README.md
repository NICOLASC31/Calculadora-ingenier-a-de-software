# Calculadora - Taller de Git y GitHub

Esta carpeta contiene una calculadora de consola escrita en Python y un
registro del flujo de trabajo con Git/GitHub solicitado en el taller.

## Requisitos

- Python 3.10 o superior

## Uso rápido

El comando sin argumentos abre la interfaz gráfica:

```bash
python calculator.py
```

Para ejecutar operaciones desde la terminal se deben pasar los argumentos:

```bash
python calculator.py add 2 3
python calculator.py sub 10 4
python calculator.py mul 3 5
python calculator.py div 10 2
```

Modo interactivo:

```bash
python calculator.py --interactive
```

## Organización

- `calculator.py`: Código fuente con las operaciones básicas.
- `registro_git.md`: Documento que explica el flujo de trabajo paso a paso,
  comandos utilizados, ejemplos y espacio para adjuntar capturas.
- La interfaz gráfica incluye botones de operaciones, limpieza, cambio de signo
  (`+/-`) y evaluación.

## Próximos pasos sugeridos

1. Seguir el guion de `registro_git.md` para generar los commits y capturas.
2. Crear el repositorio en GitHub y vincularlo como remoto `origin`.
3. Compartir el enlace del repositorio como evidencia de la práctica.
