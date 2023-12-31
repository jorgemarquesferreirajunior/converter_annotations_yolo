from datetime import datetime
import pytz

def lenFile(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except Exception as e:
        print(f"Erro ao contalibizar as linhas do arquivo {path}: {e}")


def showfilecfg(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                print(f'{i}:{line}', end='')
        print(f"Arquivo visualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao visualizado o arquivo {path}: {e}")

def configcfg(path, subdivisions, n_classes):
    try:
        with open(path, 'r+') as file:
            lines = file.readlines()
            max_batches = 2000 * n_classes
            for i, line in enumerate(lines):
                if i == 2:
                    lines[i] = 'subdivisions=' + str(subdivisions) + '\n'
                elif i == 18:
                    lines[i] = 'max_batches = ' + str(max_batches) + '\n'
                elif i == 20:
                    lines[i] = 'steps=' + str(int(max_batches * 0.8)) + ',' + str(int(max_batches * 0.9)) + '\n'
                elif i == 960 or i == 1048 or i == 1136:
                    lines[i] = 'filters=' + str((n_classes + 5) * 3) + '\n'
                elif i == 967 or i == 1055 or i == 1143:
                    lines[i] = 'classes=' + str(n_classes) + '\n'
                elif i > 1156 :
                    lines[i] = ''

            local_timezone = pytz.timezone('America/Sao_Paulo')
            now = datetime.now(local_timezone)   
            timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
            lines.append(f"\n#Data e hora da última modificação: {timestamp}\n")
            
            file.seek(0)
            file.writelines(lines)
            file.truncate()
        print(f"Arquivo editado com sucesso.")
    except Exception as e:
        print(f"Erro ao editar o arquivo {path}: {e}")
