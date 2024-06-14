from pytube import YouTube

def download_video(url, resolution='720p', output_path='./'):
    try:
        yt = YouTube(url)
        
        # Mostra as opções de stream disponíveis
        print("Opções de stream disponíveis:")
        for stream in yt.streams:
            print(stream)
        
        # Filtra os streams disponíveis pela resolução escolhida
        selected_stream = yt.streams.filter(res=resolution, progressive=True).first()
        
        if selected_stream:
            # Faz o download do vídeo
            print(f"Fazendo download do vídeo '{yt.title}' na resolução {resolution}...")
            selected_stream.download(output_path)
            print("Download concluído!")
        else:
            print(f"Nenhuma stream encontrada com a resolução {resolution}.")
    except Exception as e:
        print(f"Ocorreu um erro ao fazer download do vídeo: {str(e)}")

def main():
    print("Bem-vindo ao programa de download de vídeos do YouTube!")
    video_url = input("Insira o link do vídeo do YouTube: ")
    video_resolution = input("Insira a resolução desejada (por exemplo, '720p', '480p'): ")
    output_folder = input("Insira o caminho de saída para salvar o vídeo (pressione Enter para salvar na pasta atual): ").strip()
    
    if output_folder == '':
        output_folder = './'
    
    download_video(video_url, video_resolution, output_folder)

if __name__ == "__main__":
    main()
