import flet as ft
import time
import requests


def main(page: ft.Page):
    r = ft.Row(controls=[ft.Text("teste", size=20)])
    page.add(r)

    txt_volume_geral = ft.Text(value=50)

    contador = 0

    def altera_volume(e):
        txt_volume_geral.value = f"{int(e.control.value)}"
        txt_volume_geral.update()

    def altera_contador(e):
        

    page.add(txt_volume_geral, ft.Slider(min=0, max=100, divisions=20, label="Volume Geral", width=300, on_change=altera_volume, disabled=False, value=txt_volume_geral.value,))

    page.add(
        ft.Row(
            controls=[
                ft.TextField(label="Seu nome"),
                ft.ElevatedButton(text="Fale meu nome!"),
            ]
        )
    )
    btn_menos = ft.TextButton("+", on_click=altera_contador)
    txt_contador
    btn_mais



ft.app(target=main)


    # tf = ft.TextField(label="Gas", value=0)
    # page.add(tf)

    # for i in range(3):
    #     r.controls.append(ft.Text(i))
    #     page.update()
    #     time.sleep(1)

    # print(time.timezone)
    # for i in range(6001):
    #     tf.value = "{:.3f}".format(i/1000)
    #     page.update()
    #     time.sleep(0.002)
    # print(time.timezone)

    # r.controls.append(ft.Text("denovo"))

    # page.add(
    #     ft.Row(controls=[
    #         ft.Text("0.0"),
    #         ft.Text("0.1"),
    #         ft.Text("0.2"),
    #     ]),
    #     ft.Row(controls=[
    #         ft.Text("1.0"),
    #         ft.Text("1.1"),
    #         ft.Text("1.2"),
    #     ])
    # )

    # for i in range(10):
    #     page.controls.append(ft.Text(f"Line {i}"))
    #     # if i > 4:
    #     #     page.controls.pop(0)
    #     page.update()
    #     time.sleep(0.3)