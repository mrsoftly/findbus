# Usa una imagen oficial de Python
FROM python:3.12.3

# Establece el directorio de trabajo
WORKDIR /findbs_v2

# Copia los archivos del proyecto
COPY . /findbs_v2

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto por donde correrá Flask
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "main.py"]
