from datetime import date, timedelta
import flet as ft

def main(page: ft.Page):
    page.title = "Formulario"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    
    txtNombre = ft.TextField(
        label="Nombre del Evento",
        hint_text="Ingresa el nombre del evento",
        prefix_icon=ft.Icons.EVENT,
        max_length=100,
        keyboard_type=ft.KeyboardType.TEXT,
        border=ft.InputBorder.OUTLINE,
        width=450
    )
    
    txtTipo = ft.Dropdown(
        label="Tipo de Evento",
        value="",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunion")
        ],
        border=ft.InputBorder.OUTLINE
    )
    
    today = date.today()
    def on_change_datePicker(e):
        value = e.control.value
        txtFecha.value = value.strftime("%Y/%m/%d")
        page.update()
        
    datePicker = ft.DatePicker(
        first_date=today + timedelta(days=1),
        on_change=lambda e: on_change_datePicker(e)
    )
    
    txtFecha = ft.Text(
        value="YYYY/MM/DD",
        size=20
    )
    
    txtModalidad = ft.RadioGroup(
        value="",
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                ft.Radio(label="Virtual", value="virtual"),
                ft.Radio(label="Presencial", value="presencial")
            ]
        )
    )
    
    txtInscripcion = ft.Checkbox(
        label="¿Requiere inscripción previa?",
        value=False
    )
    
    def on_duracion_change(e):
        txtDuracion.label = f"{int(e.control.value)}h"
        
    txtDuracion = ft.Slider(
        label="1h",
        value=1,
        min=1,
        max=8,
        divisions=7,
        on_change=lambda e: on_duracion_change(e)
    )
    
    def resumen(e):
        page.update()
    
    page.add(txtNombre)
    
    page.add(ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        controls=[
            txtTipo, 
            ft.Row(
                controls=[
                    ft.Button(
                        icon=ft.Icons.CALENDAR_MONTH,
                        content="Fecha",
                        on_click=lambda e: page.show_dialog(datePicker)
                    ),
                    txtFecha
                ]
            )
        ]
    ))
    
    page.add(txtModalidad, ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[txtInscripcion]
    ))
    
    page.add(ft.Text(
        value="Duración del Evento",
        margin=ft.Margin(top=25)
    ))
    
    page.add(txtDuracion)
    
    page.add(ft.Button(
        content="Mostrar Resumen",
        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE,
        on_click=lambda e: resumen(e)
    ))
    
    page.add(ft.Divider(
        color=ft.Colors.GREY,
    ))

ft.run(main)
