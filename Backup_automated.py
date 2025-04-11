import os
import time
import schedule
import shutil
import datetime

source_dir = r"C:\Users\Vega 2\Desktop\TODAS CARPETAS\ARTE"
destination_dir = r"C:\Users\Vega 2\Desktop\TODAS CARPETAS\Prueba5"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))  # create the route + folder and name

    # Mostrar la ruta generada antes de intentar copiar
    print(f"Ruta de destino generada: {dest_dir}")

    try:
        shutil.copytree(source, dest_dir)  # copy the documents
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in {dest}")

# Añadido: verificar si la tarea programada se está ejecutando
def task():
    print("Tarea programada ejecutada")
    copy_folder_to_directory(source_dir, destination_dir)

# Agregar la tarea al programador para que se ejecute todos los días a las 19:35
schedule.every().day.at("21:23").do(task)

while True:
    print("Esperando para ejecutar la tarea programada...")
    schedule.run_pending()
    time.sleep(30)