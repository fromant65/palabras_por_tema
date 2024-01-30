# Procedimiento de generación de temas
- Se debe escribir en topics.txt la lista de temas deseados
- En caso de querer generarlos automaticamente, se le puede pedir a chatgpt que lo haga.
- El archivo topics.txt debe comenzar en cada linea con las palabras "En la..." o "En el...".
- Cada tema se separa por un salto de linea
- Antes de comenzar a generar palabras, se debe correr el archivo main.py
- La function delete_topic_files() existe en caso de que haya algún error en la generación inicial de los archivos CSV

# Procedimiento de generación de palabras 
1. Elegir un tema para generar.
2. Ejecutar el archivo read_done_words.py con el tema elegido. El mismo generará una lista de palabras ya generadas del tema en cuestión.
3. Agregar el tema y pegar esa lista de palabras donde corresponde en el prompt de chatgpt. 
4. Pasarle el prompt a ChatGPT.
5. Copiar la lista de palabras generadas por ChatGPT al final del archivo CSV del tema correspondiente.
6. Repetir hasta que la lista tenga la cantidad de palabras deseada.
