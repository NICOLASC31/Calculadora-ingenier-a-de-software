"""Simple calculator with CLI, interactive prompt, and GUI support."""

from __future__ import annotations

import argparse
import operator
import sys
from typing import Callable, Dict, Tuple


Operation = Callable[[float, float], float]


def safe_divide(a: float, b: float) -> float:
    """Divide ensuring the divisor is not zero."""
    if b == 0:
        raise ValueError("No es posible dividir entre cero.")
    return a / b


OPERATIONS: Dict[str, Tuple[str, Operation]] = {
    "add": ("suma", operator.add),
    "sub": ("resta", operator.sub),
    "mul": ("multiplicacion", operator.mul),
    "div": ("division", safe_divide),
}


def run_calculation(operation_key: str, a: float, b: float) -> float:
    """Runs the requested operation."""
    try:
        _, func = OPERATIONS[operation_key]
    except KeyError as exc:
        raise ValueError(f"Operacion desconocida: {operation_key}") from exc
    return func(a, b)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Calculadora basica (+, -, *, /). "
            "Por defecto abre la interfaz grafica; usa argumentos para el modo CLI "
            "o '--interactive' para responder en consola."
        )
    )
    parser.add_argument(
        "operation",
        nargs="?",
        choices=OPERATIONS.keys(),
        help="Operacion a ejecutar",
    )
    parser.add_argument("a", nargs="?", type=float, help="Primer numero")
    parser.add_argument("b", nargs="?", type=float, help="Segundo numero")
    parser.add_argument(
        "--interactive",
        "-i",
        action="store_true",
        help="Activa el modo interactivo",
    )
    parser.add_argument(
        "--gui",
        "-g",
        action="store_true",
        help="Abre la calculadora con interfaz grafica",
    )
    return parser


def interactive_mode() -> None:
    """Simple text-based interaction when no args are provided."""
    print("=== Calculadora interactiva ===")
    print("Operaciones disponibles:")
    for key, (label, _) in OPERATIONS.items():
        print(f"- {key}: {label}")
    op = input("Elige la operacion: ").strip()
    try:
        a = float(input("Primer numero: ").strip())
        b = float(input("Segundo numero: ").strip())
        result = run_calculation(op, a, b)
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)
    print(f"Resultado: {result}")


def launch_gui() -> None:
    """Starts a Tkinter-based calculator UI."""
    import tkinter as tk
    from tkinter import messagebox

    window = tk.Tk()
    window.title("Calculadora")
    window.resizable(False, False)

    display_var = tk.StringVar(value="0")
    entry = tk.Entry(
        window,
        textvariable=display_var,
        font=("Segoe UI", 22),
        bd=0,
        relief="flat",
        justify="right",
        state="readonly",
    )
    entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=(10, 5))
    entry.configure(readonlybackground="#f7f7f7")

    stored_value: float | None = None
    current_operator: str | None = None
    reset_display = True

    def set_display(value: str) -> None:
        display_var.set(value)

    def append_value(value: str) -> None:
        nonlocal reset_display
        current = display_var.get()
        if reset_display or current == "0":
            set_display(value)
        else:
            set_display(current + value)
        reset_display = False

    def append_decimal() -> None:
        nonlocal reset_display
        current = display_var.get()
        if reset_display:
            set_display("0.")
            reset_display = False
            return
        if "." not in current:
            set_display(current + ".")

    def clear_display() -> None:
        nonlocal stored_value, current_operator, reset_display
        stored_value = None
        current_operator = None
        reset_display = True
        set_display("0")

    def set_operator(op_key: str) -> None:
        nonlocal stored_value, current_operator, reset_display
        try:
            stored_value = float(display_var.get())
        except ValueError:
            messagebox.showerror("Error", "Entrada invalida.")
            clear_display()
            return
        current_operator = op_key
        reset_display = True

    def calculate() -> None:
        nonlocal stored_value, current_operator, reset_display
        if current_operator is None or stored_value is None:
            return
        try:
            second = float(display_var.get())
            result = run_calculation(current_operator, stored_value, second)
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))
            clear_display()
            return
        set_display(str(result))
        stored_value = result
        current_operator = None
        reset_display = True

    button_layout = [
        [
            ("7", lambda value="7": append_value(value), 1),
            ("8", lambda value="8": append_value(value), 1),
            ("9", lambda value="9": append_value(value), 1),
            ("/", lambda op="div": set_operator(op), 1),
        ],
        [
            ("4", lambda value="4": append_value(value), 1),
            ("5", lambda value="5": append_value(value), 1),
            ("6", lambda value="6": append_value(value), 1),
            ("*", lambda op="mul": set_operator(op), 1),
        ],
        [
            ("1", lambda value="1": append_value(value), 1),
            ("2", lambda value="2": append_value(value), 1),
            ("3", lambda value="3": append_value(value), 1),
            ("-", lambda op="sub": set_operator(op), 1),
        ],
        [
            ("C", clear_display, 1),
            ("0", lambda value="0": append_value(value), 1),
            (".", append_decimal, 1),
            ("+", lambda op="add": set_operator(op), 1),
        ],
        [
            ("=", calculate, 4),
        ],
    ]

    for row_index in range(1, len(button_layout) + 1):
        window.rowconfigure(row_index, weight=1)
    for col_index in range(4):
        window.columnconfigure(col_index, weight=1)

    for row_index, row in enumerate(button_layout, start=1):
        col_index = 0
        for text, command, span in row:
            btn = tk.Button(
                window,
                text=text,
                command=command,
                font=("Segoe UI", 16),
                padx=10,
                pady=10,
            )
            btn.grid(
                row=row_index,
                column=col_index,
                columnspan=span,
                sticky="nsew",
                padx=5,
                pady=5,
            )
            col_index += span

    window.mainloop()


def main(args: list[str] | None = None) -> None:
    parser = build_parser()
    namespace = parser.parse_args(args=args)

    if namespace.operation is not None:
        if namespace.a is None or namespace.b is None:
            parser.error("Debes proporcionar dos numeros (a y b).")
        try:
            result = run_calculation(namespace.operation, namespace.a, namespace.b)
        except ValueError as exc:
            parser.error(str(exc))
        print(result)
        return

    if namespace.interactive:
        interactive_mode()
        return

    launch_gui()


if __name__ == "__main__":
    main()
