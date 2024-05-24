import flet as ft
import time
import requests


def main(page: ft.Page):

    page.window_height = 800
    page.window_width = 340
    page.scroll = "always"
    def altera_contador(e):
        if e.control.text == "+":
            txt_contador.value += 1
            lv.controls.insert(0, ft.Row(controls=[ft.Text(f"Adicionado 1"), ft.Text("+", color="green")]))
        else:
            txt_contador.value -= 1
            lv.controls.insert(0, ft.Row(controls=[ft.Text(f"Removido 1"), ft.Text("-", color="red")]))
        txt_contador.update()
        lv.update()

    btn_mais = ft.TextButton(text="+", on_click=altera_contador)
    txt_contador = ft.Text(value=0)
    btn_menos = ft.TextButton(text="-", on_click=altera_contador)
    lv = ft.ListView(height=200, spacing=10)
    page.add(
        ft.Row(
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            controls=[
                btn_menos,
                txt_contador,
                btn_mais,
            ],
            height=200,
            width=500,
        ),
        ft.Row(
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            controls=[
                lv
            ]
        )
    )



ft.app(target=main)

    # r = ft.Row(controls=[ft.Text("teste", size=20)])
    # page.add(r)

    # txt_volume_geral = ft.Text(value=50)

    # def altera_volume(e):
    #     txt_volume_geral.value = f"{int(e.control.value)}"
    #     txt_volume_geral.update()
    # page.add(txt_volume_geral, ft.Slider(min=0, max=100, divisions=20, label="Volume Geral", width=300, on_change=altera_volume, disabled=False, value=txt_volume_geral.value,))

    # page.add(
    #     ft.Row(
    #         controls=[
    #             ft.TextField(label="Seu nome"),
    #             ft.ElevatedButton(text="Fale meu nome!"),
    #         ]
    #     )
    # )

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