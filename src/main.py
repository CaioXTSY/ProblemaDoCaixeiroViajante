from pathlib import Path
import file_converter

def list_files_in_directory(directory):
    files = list(directory.glob('*'))
    files_dict = {i: file.name for i, file in enumerate(files, start=1)}
    return files_dict

def main():
    src_dir = Path(__file__).resolve().parent / 'bases'
    files_dict = list_files_in_directory(src_dir)

    for index, file in files_dict.items():
        print(f"{index}: {file}")

    try:
        file_index = int(input('Selecione o índice do arquivo: '))
        file_name = files_dict[file_index]
        file_path = src_dir / file_name
    except (ValueError, KeyError):
        print("Índice inválido.")
        return

    if file_path.exists() and file_path.is_file():
        graph = file_converter.Converter(str(file_path)).grafo()
        for key, value in graph.items():
            print(f"{key}: {value}")
    else:
        print(f"Arquivo '{file_name}' não encontrado no diretório '{src_dir}'.")

if __name__ == "__main__":
    main()
