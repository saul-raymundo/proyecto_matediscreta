# Programa de Operaciones con Conjuntos

Este repositorio contiene el código fuente y la documentación del Programa de Conjuntos, una aplicación de escritorio desarrollada en Python para la materia de Matemática Discreta.
La aplicación permite realizar de forma sencilla las operaciones fundamentales de teoría de conjuntos: unión, intersección, diferencia y complemento.

## Integrantes del equipo

* JOSE AMILCAR PALMA VILLANUEVA
* ROBIN GUSTAVO PÉREZ SÁCHEZ
* SAUL RAYMUNDO NUFIO
* CRISTIAN JOSUE ALBERTO DIAZ GARCIA

## Estructura del proyecto

* MOD_PROYECTO.py: Es el archivo principal de la aplicación. Contiene la interfaz gráfica creada con Tkinter, la barra de menú, los formularios y la lógica para descargar las fotos de los integrantes en la sección Sobre nosotros.
* MOD_PRUEVA.py / pruebas.py: Módulo que contiene la función opreac_conjunt y la lógica matemática para procesar las operaciones utilizando conjuntos de Python.
* Manual_Tecnico_PROYECTO_MATE_DISCRETA.docx: Documento técnico que explica la arquitectura del programa, las librerías utilizadas, el flujo de datos y el funcionamiento interno de cada función.
* Manual_de_Usuario_PROYECTO_MATE_DISCRETA.docx: Guía paso a paso orientada al usuario final, con instrucciones para ingresar los datos, ejemplos prácticos de cada operación y solución a mensajes de error.

## Requisitos e instalación

Para ejecutar el programa desde el código fuente necesitas tener instalado Python 3 y la librería Pillow para el manejo de imágenes.

Puedes instalar Pillow desde la consola con el siguiente comando:

pip install pillow

## Cómo ejecutar el programa

1. Asegúrate de tener todos los archivos en la misma carpeta.
2. Abre la terminal o consola de comandos en esa ubicación.
3. Ejecuta el archivo principal con el comando:

python MOD_PROYECTO.py

## Nota sobre las fotografías

La sección Sobre nosotros se conecta al repositorio de GitHub para descargar las imágenes de los integrantes al presionar la opción en el menú.
Se requiere una conexión a Internet activa para que las fotos carguen correctamente en la pantalla.
