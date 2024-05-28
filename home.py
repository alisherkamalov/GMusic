import flet as ft


def click_photo(event):
    
    photo.scale=ft.transform.Scale(1.5)
    photo.update()

field = ft.CupertinoTextField(
        bgcolor=ft.colors.GREY_600,
        width=160,
        
        border=ft.border.all(color=ft.colors.GREY_600),
        placeholder_text='Поиск песни', placeholder_style=ft.TextStyle(color=ft.colors.WHITE, weight=ft.FontWeight.W_500),
        color=ft.colors.WHITE
        )

find_btn = ft.IconButton(icon=ft.icons.SEARCH,icon_color=ft.colors.WHITE, opacity=1)

entry = ft.Container(
    animate=ft.animation.Animation(300,'ease'),
    content=ft.Row([
        field,
        find_btn
    ],spacing=0
                   )
)

cont_entry = ft.Container (
    width=220,
    height=40,
    padding=ft.padding.only(10,0),
    bgcolor=ft.colors.GREY_600,
    border_radius=3,
    animate=ft.animation.Animation(300,'ease'),
    offset=ft.transform.Offset(0.050,0),
    shadow=ft.BoxShadow(
        1,
        100
    ),
    content=ft.Stack([
        entry
    ])
)
        
exit = ft.Container(
    content=ft.Column([
        cont_entry
    ]),
    
    height=175,
    
    
    )

photo_img = ft.Image(src=f'assets/none photo.jpg')

photo = ft.Container (
    width=150,
    height=150,
    animate_opacity=500,
    alignment=ft.alignment.top_center,
    content=ft.Stack([
        photo_img
    ]),
    shadow=ft.BoxShadow(
        1,
        100
    ),
    animate_scale=ft.animation.Animation(300, ft.AnimationCurve.BOUNCE_OUT),
    on_click=click_photo
)

desc = ft.Text(
    '',
    color=ft.colors.WHITE,
    size=30,
    animate_opacity=500,
    weight=ft.FontWeight.W_700
    
)

desc_music = ft.Container (
    height=100,
    animate_opacity=500,
    alignment=ft.alignment.bottom_left,
    content=ft.Stack([
        desc
    ])
)

av_photo = ft.Image(src=f'assets/none photo.jpg')

avatar = ft.Container(
    content=av_photo,
    border_radius=50,
    width=25,
    height=25,
    animate_opacity=500,
    shadow=ft.BoxShadow(
        1,
        1000
    ),
)

author_music = ft.Text(
    '',
    color=ft.colors.WHITE,
    size=15,
    animate_opacity=500,
    weight=ft.FontWeight.W_700
    
)

single = ft.Text(
    'Сингл ● 2024',
    color=ft.colors.GREY_500,
    size=15,
    weight=ft.FontWeight.W_600,
    opacity=0,
    animate_opacity=500
    
)

audio = ft.Audio(
        src=f'assets/none sound.mp3', 
        autoplay=False,
        volume=100,
        balance=0,
        on_loaded=lambda _: print("Loaded"),
        on_duration_changed=lambda e: print("Duration changed:", e.data),
        on_position_changed=lambda e: print("Position changed:", e.data),
        on_state_changed=lambda e: print("State changed:", e.data),
        on_seek_complete=lambda _: print("Seek complete"),
        
    )

autoplay = ft.IconButton(icon=ft.icons.AUTORENEW, width=50,height=50, bgcolor=ft.colors.BLACK, icon_color=ft.colors.WHITE, icon_size=30)

autoplay_mus = ft.Container (
    content=ft.Stack([
        autoplay
    ])
)


    

play_mus_btn = ft.IconButton(icon=ft.icons.PLAY_ARROW, icon_color=ft.colors.BLACK, bgcolor='#35BE30',width=50,height=50, icon_size=35)



bottombar = ft.CupertinoNavigationBar(
    bgcolor=ft.colors.BLACK,
    inactive_color=ft.colors.GREY,
    active_color=ft.colors.WHITE,
    opacity=0.9,
    destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Главная"),
            ft.NavigationDestination(icon=ft.icons.SEARCH, label="Поиск"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Моя медиатека",
            ),
        ]
        )
    
        
        
    
    