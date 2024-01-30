import os

def create_topic_set() -> set:
    # Los temas en topics.txt deben ser "En el..." o "En la..."
    topics = open("topics.txt")
    topic_list = topics.read().split("\n")
    topic_set = set()
    for topic in topic_list:
        topic = " ".join(topic.split(" ")[2:])
        topic_set.add(topic)
    topics.close()
    return topic_set

def create_new_topic_file(topic:str, categories:list):
    topic = topic.replace(" ", "_")
    file = open(f"./lists/{topic}.csv", "w", encoding="UTF-8")
    line_string=""
    for cat in categories:
        line_string += cat + ", "
    line_string = line_string[:-2]
    file.write(line_string+'\n')
    file.close()

def create_topics_files(topic_set:set):
    categories = ["palabra", "tipo gramatical", "word", "sentence", "言葉", "読み", "例文", "例文の読み"]
    for topic in topic_set:
        create_new_topic_file(topic, categories)

def delete_topics_files():
    folder = "./lists"
    for file in os.listdir(folder):
        # Combinar el directorio con el nombre del archivo para obtener la ruta completa
        path = os.path.join(folder, file)
        try:
            if os.path.isfile(path):  # Verificar si es un archivo
                os.remove(path)  # Borrar el archivo
                print(f"Archivo {file} borrado exitosamente.")
            else:
                print(f"{file} no es un archivo.")
        except Exception as e:
            print(f"No se pudo borrar {file}: {str(e)}")

def main():
    topic_set = create_topic_set()
    create_topics_files(topic_set)
    #delete_topics_files()

if __name__ == "__main__":
    main()