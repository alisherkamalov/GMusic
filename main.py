import flet as ft
from home import exit, entry, photo, desc_music,avatar,author_music,single,play_mus_btn, audio, autoplay_mus, autoplay,bottombar, field, cont_entry, find_btn, desc, photo_img, av_photo
import asyncio
import os
import requests
import yt_dlp
class Main():
    def main(page: ft.Page):
        page.padding=ft.padding.only(15,30)
        page.bgcolor = '#B9D7FF'
        page.window_width = 430
        page.window_height = 900
        entry.width=350
        
        page.add(exit)
        photo.opacity = 0
        avatar.opacity = 0
        field.value = ''
        page.route = '/home'
        
        page.add(audio)
        
        with open('requirements.txt', 'w', encoding='utf-8') as fl:
            fl.write('requests\nasyncio\nyt-dlp')
        
        def search_youtube(name):
            name = field.value
            with yt_dlp.YoutubeDL() as ydl:
                try:
                    search_results = ydl.extract_info(f"ytsearch1:{name} official audio", download=False)
                    if search_results['entries']:
                        video_url = search_results['entries'][0]['webpage_url']
                        return video_url
                    else:
                        print("Песня не найдена")
                        return None
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
                    return None

        def download_audio(url, output_folder, filename_mus):
        # Создаем объект ydl с настройками
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(output_folder, f"{filename_mus}.mp3"),
            }
    
            # Создаем объект ydl
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    ydl.download([url])
                except Exception as e:
                    print(f"Произошла ошибка при скачивании аудио: {e}")

                
                
        def create_images_folder():
            if not os.path.exists("assets/songs"):
                os.makedirs("assets/songs")
                print("Папка 'assets/songs' создана.")

        # Функция для выполнения запроса к API Unsplash и получения URL изображения
        def search_images(query):
            url = "https://api.unsplash.com/search/photos"
            headers = {
                "Accept-Version": "v1",
                "Authorization": "Client-ID Your client ID"  # Замените на ваш ключ доступа
            }
            params = {
                "query": query,
                "per_page": 1  # Количество изображений для загрузки
            }

            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                if data["results"]:
                    image_url = data["results"][0]["urls"]["regular"]
                    return image_url
                else:
                    print("Изображения не найдены.")
            else:
                print("Ошибка при выполнении запроса:", response.status_code)

            
        
        
        
        async def find_music_and_photo_in_internet(event):
            path_forder = 'assets/songs'
            files = os.listdir(path_forder)
            for file in files:
                file_path = os.path.join(path_forder, file)
                os.remove(file_path)
            await asyncio.sleep(1)
            search = ft.Text('Поиск', animate_offset=ft.animation.Animation(500,'ease'), offset=ft.transform.Offset(0,5), bottom=50, left=20, size=25, color=ft.colors.WHITE)
            page.overlay.append(search)
            page.update()
            await asyncio.sleep(0.1)
            search.offset=ft.transform.Offset(0,0)
            page.update()
            await asyncio.sleep(0.5)
            video_url = search_youtube(name=field.value)
            if video_url:
                filename_mus = f"{field.value}"
                download_audio(video_url, "assets/songs", filename_mus)
                print(f"Аудиофайл успешно скачан: assets/songs/{filename_mus}")

            image_url = search_images(field.value)
            if image_url:
                filename = field.value.replace(" ", "_") + ".jpg"  # Имя файла на основе названия песни
                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(os.path.join("assets/songs", filename), 'wb') as f:
                        f.write(response.content)
                        print("Изображение успешно сохранено как", filename)
                        
                        
                else:
                    print("Ошибка при загрузке изображения:", response.status_code)
                    
                field.value = f'{filename_mus}'

                if field.value == filename_mus:
                    print(True)
                    photo.opacity = 1
                    avatar.opacity = 1
                    photo_img.src = f'assets/songs/{filename}'
                    
                    av_photo.src = f'assets/songs/{filename}'
                    audio.src = f'assets/songs/{filename_mus}.mp3'
                    desc.value = field.value
                    author_music.value = field.value
                    search.offset=ft.transform.Offset(0,5)
                    page.update()
                else: 
                    print(f"field.value: {field.value}")
                    print(f"filename_mus: {filename_mus}")
                    print(f"filename: {filename}")
                    print(False)

            create_images_folder()  # Создаем папку assets/songs, если она еще не существует
            page.update() 


                    
                    
            
        
        
        async def audio_play(_):
    
            audio.resume()
            play_mus_btn.icon=ft.icons.STOP
            
            play_mus_btn.on_click=audio_stop
            while True:
                if play_mus_btn.on_click!=audio_play:
                    photo.scale=ft.transform.Scale(1.1)
                    page.update()
                    await asyncio.sleep(0.2)
                    photo.scale=ft.transform.Scale(1.2)
                    page.update()
                    await asyncio.sleep(0.2)
                    photo.scale=ft.transform.Scale(1.3)
                    page.update()
                    await asyncio.sleep(0.2)
                    photo.scale=ft.transform.Scale(1)
                    page.update()
                    
                else:
                    
                    photo.scale=ft.transform.Scale(1)
                    break
                    
                
            page.update()
            
            
    
        def audio_stop(_):
    
            audio.pause()
            play_mus_btn.icon=ft.icons.PLAY_ARROW
            play_mus_btn.on_click=audio_play
            photo.scale=ft.transform.Scale(1)
            page.update()
            
        def audio_autoplay_no(_):
            audio.pause()
            autoplay.on_click=audio_autoplay_yes
            page.update()
            print('autoplay false')
            
        def audio_autoplay_yes(_):
            autoplay.on_click = audio_autoplay_no  
            page.update()  
            print('автовоспроизведение включено')
            while True:
                if audio.get_current_position == 0000:
                    audio.play()
                    page.update()  
                
            
            
        autoplay.on_click=audio_autoplay_yes
        play_mus_btn.on_click=audio_play
        
        if page.route == '/home':  
            page.add(ft.Stack([
            
                ft.Container (
                expand=True,
                
                height=1,
                shadow=ft.BoxShadow(
                500,
                500
                ),
                offset=ft.transform.Offset(0,525)
                ),
            
                ft.Column([
                ft.Row([
                photo
                ], alignment=ft.MainAxisAlignment.CENTER,
                ),
                desc_music,
                ft.Row([
                    avatar,
                    author_music
                ]),
                ft.Row([
                    single
                ]),
                ft.Row([
                    autoplay_mus,
                    play_mus_btn
                ])
                
                ])
            
                ]))
        
            page.overlay.append(
                ft.Container (
                expand=True,
                
                height=1,
                shadow=ft.BoxShadow(
                150,
                500
                ),
                offset=ft.transform.Offset(0,950)
                ),
            )
        
            page.add(
                bottombar
            
            )
        
        find_btn.on_click = find_music_and_photo_in_internet
        
        
        
        page.update()
        
ft.app(target=Main.main, assets_dir='assets')
