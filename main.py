import flet as ft
def main(page: ft.Page):
    def sumar():
        try:
            num1 = float(numero1.value)
            num2 = float(numero2.value)
            suma = num1 + num2
            resultado.value = f"Resultado: {suma}"
        except ValueError:
            resultado.value = "Ingresa números válidos."
        page.update()
    page.title = "Ejemplo controles flet"
    numero1 = ft.TextField(label="Número 1")
    numero2 = ft.TextField(label="Número 2")
    resultado = ft.Text("Resultado: 0")

    boton_sumar = ft.Button("Sumar", on_click=sumar)
    page.add(numero1,numero2,resultado,boton_sumar)
ft.run(main)
