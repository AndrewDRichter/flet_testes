import flet as ft
import sqlite3

class Conta():
    def __init__(self, titular:str, valor:float=0.0):
        self.titular = titular
        self.valor = valor
        self.ativa = True


def main(page: ft.Page):
    page.title = "Aplicativo"
    page.scroll = "always"
    banco = sqlite3.connect('test_db.db')
    cursor = banco.cursor()
    #cursor.execute("CREATE TABLE IF NOT EXISTS tbl_teste (id INTEGER PRIMARY KEY, nome TEXT, ativo INTEGER)")
    #cursor.execute("INSERT INTO tbl_teste (nome, ativo) VALUES (?, ?)", ("Andrew", 1))
    #banco.commit()
        
    def carrega_dados_teste():
        cursor.execute("SELECT * FROM tbl_teste")
        slct_results = cursor.fetchall()
        lv_teste.controls.append(ft.Row(controls=[
            ft.Text("Id"),  
            ft.Text("Nome"),  
            ft.Text("Ativo"),  
            ]))
        lv_teste.controls.append(ft.Row(controls=[
            ft.Divider()
        ]))
        for row in slct_results:
            (id, nome, ativo) = row
            lv_teste.controls.append(ft.Row(controls=[
                ft.Text(id),
                ft.Text(nome),
                ft.Text(ativo),
            ]))
        lv_teste.update()
    
    def rem_espaco_duplo(e):
        valor = e.control.value.replace("  ", " ")
        nova_tarefa.value = valor
        nova_tarefa.update()
        if valor[-1] == " ":
            valor[-1] = ""
        print(valor + "->" + valor[-1])
    
    def lista_controls(e):
        for i in page.controls:
            if type(i) == ft.Row:
                for j in i.controls:
                    print(j)
            else:
                print(i)
    
    def add_tarefa(e):
        if nova_tarefa.value == "":
            exit
        else:
            cb_tarefa = ft.Checkbox(label=nova_tarefa.value)
            btn_eliminar = ft.ElevatedButton("Excluir", data=nova_tarefa.value, on_click=rem_tarefa)
            lv_tarefas.controls.append(ft.Row(controls=[
                cb_tarefa,
                btn_eliminar
            ]))
            nova_tarefa.value = ""
            nova_tarefa.focus()
            nova_tarefa.update()
            lv_tarefas.update()
    
    def rem_tarefa(e):
        print(e.control)
    
    nova_tarefa = ft.TextField(hint_text="O que há para ser feito?", width=400, content_padding=10, on_change=rem_espaco_duplo)
    page.add(ft.Row([nova_tarefa, ft.ElevatedButton("Adicionar", on_click=add_tarefa)]))

    #page.add(ft.ElevatedButton("?", on_click=lista_controls))
    
    lv_tarefas = ft.ListView(height=100, spacing=0, auto_scroll=True)
    page.add(lv_tarefas)

    lv_teste = ft.ListView(height=200, spacing=0, auto_scroll=True)
    page.add(lv_teste)

    carrega_dados_teste()


ft.app(main)
    # def altera_contador(e):
    #     if e.control.text == "-":
    #         txt_contador.value = int(txt_contador.value) - 1
    #     else:
    #         txt_contador.value = int(txt_contador.value) + 1
    #     if txt_contador.value == 100:
    #         txt_contador.width = int(txt_contador.width) + 20
    #     txt_contador.update()

    # btn_menos = ft.ElevatedButton("-", on_click=altera_contador, bgcolor="red")
    # txt_contador = ft.TextField(value=0, width=50, input_filter=ft.NumbersOnlyInputFilter(), fill_color="black")
    # btn_mais = ft.ElevatedButton("+", on_click=altera_contador, bgcolor="green")
    
    # page.add(ft.Row(alignment=ft.MainAxisAlignment.CENTER,
    #     controls=[btn_menos,
    #               txt_contador,
    #               btn_mais]
    # ))

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