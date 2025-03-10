import os

output_name = "TgBot2_0_1.exe"  # Название файла которое будет после момпеляции
python_file = "TgBot2"  #название твоего кода но без .py


try:
    import PyInstaller
except ImportError:
    os.system("pip install pyinstaller")


os.system(f'pyinstaller --onefile  --log-level=DEBUG {python_file}.py --name "{output_name[:-4]}"')
