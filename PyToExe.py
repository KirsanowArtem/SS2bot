import os

output_name = "TgBot2_0_1.exe"  # Версия, меняем только последнее число
python_file = "TgBot2"


try:
    import PyInstaller
except ImportError:
    os.system("pip install pyinstaller")


os.system(f'pyinstaller --onefile  --log-level=DEBUG {python_file}.py --name "{output_name[:-4]}"')
