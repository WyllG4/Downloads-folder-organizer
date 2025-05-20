from pathlib import Path
import shutil

downloads_dir = Path.home() / "Downloads"

# Mapeamento de tipos de arquivos para subpastas
tipos_arquivos = {
    'Imagens': ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'],
    'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.odt'],
    'Planilhas': ['.xls', '.xlsx', '.csv'],
    'Apresentações': ['.ppt', '.pptx'],
    'Executáveis': ['.exe', '.msi', '.bat', '.sh'],
    'Compactados': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Vídeos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Áudios': ['.mp3', '.wav', '.aac', '.ogg'],
    'Instaladores': ['.apk', '.dmg', '.deb', '.rpm'],
    'Python': ['.py', '.pyc'],
    'Outros': []
}

for item in downloads_dir.iterdir():
    if item.is_file():
        destino = downloads_dir / 'Outros' 
        for pasta, extensoes in tipos_arquivos.items():
            if item.suffix.lower() in extensoes:
                destino = downloads_dir / pasta
                break

        destino.mkdir(exist_ok=True)
        try:
            shutil.move(str(item), destino / item.name)
            print(f"Movido: {item.name} -> {destino.name}/")
        except Exception as e:
            print(f"Erro ao mover {item.name}: {e}")
