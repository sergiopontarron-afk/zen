#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PUNTO DE ENTRADA PRINCIPAL - SISTEMA DE GESTIÓN DE USUARIOS FLASK
================================================================

Este archivo es el punto de entrada principal de la aplicación Flask.
Se encarga de crear la instancia de la aplicación y ejecutarla en modo desarrollo.

Características:
- Importa la factory function create_app() desde el módulo app
- Crea una instancia de la aplicación Flask
- Ejecuta el servidor de desarrollo con debug=True para facilitar el desarrollo

Uso:
    python run.py

El servidor se iniciará en http://127.0.0.1:5000 por defecto.

Autor: Sistema de Gestión de Usuarios Flask
Fecha: 17 de octubre de 2025
"""

# Importar la factory function para crear la aplicación Flask
from app import create_app

# Crear la instancia de la aplicación Flask utilizando el patrón Application Factory
app = create_app()

# Punto de entrada principal del programa
if __name__ == '__main__':
    """
    Ejecutar la aplicación Flask en modo desarrollo.
    
    Configuración:
    - debug=True: Activa el modo debug para desarrollo
      * Recarga automática cuando se detectan cambios en el código
      * Muestra errores detallados en el navegador
      * Activa el debugger interactivo de Werkzeug
    
    Nota: En producción, se debe usar un servidor WSGI como Gunicorn
    en lugar de este servidor de desarrollo.
    """
    app.run(
        debug=True,          # Modo debug para desarrollo
        host='127.0.0.1',    # Solo accesible desde localhost (seguridad)
        port=5000            # Puerto por defecto de Flask
    )
