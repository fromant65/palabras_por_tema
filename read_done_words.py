def main():
    topic = input("Ingresa el nombre del tema que quieres leer las palabras ingresadas: ")
    try: 
        file = open(f"./lists/{topic}.csv", "r")
        output = open("done_words_list.txt", "w")
        output.write(f"topic: {topic}\n")
        for line in file:
            word=  line.split(", ")[0]
            output.write(word+', ')
        file.close()
        output.close()
        print("Las palabras ya presentes en la lista fueron escritas en done_words_list.txt")
    except Exception as e:
        print(f"No hay un archivo llamado {topic}.csv")

if __name__=="__main__":
    main()