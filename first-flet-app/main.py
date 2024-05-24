import flet as ft


def main(page: ft.Page):
    page.title = "Aplicativo"
    page.bgcolor = "brown"
    #lista_tarefas = []

    def altera_contador(e):
        if e.control.text == "-":
            txt_contador.value = int(txt_contador.value) - 1
        else:
            txt_contador.value = int(txt_contador.value) + 1
        if txt_contador.value == 100:
            txt_contador.width = int(txt_contador.width) + 20
        txt_contador.update()
            
    
    def lista_controls(e):
        for i in page.controls:
            if type(i) == ft.Row:
                for j in i.controls:
                    print(j)
            else:
                print(i)
    
    def add_tarefa(e):
        page.add(ft.Checkbox(label=nova_tarefa.value, value=1))
        nova_tarefa.value = ""
        nova_tarefa.focus()
        nova_tarefa.update()
        
    nova_tarefa = ft.TextField(hint_text="O que há para ser feito?", width=400, content_padding=10)
    page.add(ft.Row([nova_tarefa, ft.ElevatedButton("Adicionar", on_click=add_tarefa)]))

    #page.add(ft.ElevatedButton("?", on_click=lista_controls))
    
    btn_menos = ft.ElevatedButton("-", on_click=altera_contador, bgcolor="red")
    txt_contador = ft.TextField(value=0, width=50, input_filter=ft.NumbersOnlyInputFilter(), fill_color="black")
    btn_mais = ft.ElevatedButton("+", on_click=altera_contador, bgcolor="green")
    
    page.add(ft.Row(alignment=ft.MainAxisAlignment.CENTER,
        controls=[btn_menos,
                  txt_contador,
                  btn_mais]
    ))
    



ft.app(main)


    # for i in range(15):
    #     l = ft.Row()
    #     page.add(l)
    #     for j in range(15):
    #         if i > 9:
    #             if j > 9:
    #                 l.controls.append(ft.Text(f"{i}{j}"))
    #             else:
    #                 l.controls.append(ft.Text(f"{i}{j}"))
    #         else:
    #             if j > 9:
    #                 l.controls.append(ft.Text(f"{i} {j}"))
    #             else:
    #                 l.controls.append(ft.Text(f" {i} {j}"))
                
    #         page.update()