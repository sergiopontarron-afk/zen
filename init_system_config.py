#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCRIPT DE INICIALIZACIÓN - CONFIGURACIONES DEL SISTEMA
=====================================================

Este script inicializa la nueva tabla SystemConfig y migra las configuraciones
existentes desde las sesiones a la base de datos permanente.

Funcionalidades:
- Crea la tabla SystemConfig si no existe
- Migra configuraciones por defecto
- Proporciona configuraciones iniciales del sistema

Uso:
    python init_system_config.py

Autor: Sistema de Gestión de Usuarios Flask
Fecha: 17 de octubre de 2025
"""

import sys
import os

# Agregar el directorio padre al path para importar la app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def initialize_system_config():
    """
    Inicializa las configuraciones del sistema en la base de datos.
    """
    from app import create_app
    from app.database import db
    from app.models import SystemConfig
    
    print("🔧 Inicializando configuraciones del sistema...")
    
    # Crear la aplicación Flask
    app = create_app()
    
    with app.app_context():
        try:
            # Crear todas las tablas si no existen
            print("📁 Creando tablas de base de datos...")
            db.create_all()
            
            # Configuración por defecto para políticas de contraseñas
            default_password_policy = {
                'min_length': 6,
                'require_uppercase': False,
                'require_lowercase': True,
                'require_numbers': False,
                'require_special': False
            }
            
            # Verificar si ya existe la configuración de políticas
            existing_policy = SystemConfig.query.filter_by(config_key='password_policy').first()
            
            if not existing_policy:
                print("🔐 Creando configuración por defecto de políticas de contraseñas...")
                SystemConfig.set_config(
                    config_key='password_policy',
                    config_value=default_password_policy,
                    description='Políticas de contraseñas del sistema',
                    updated_by='system'
                )
                print("✅ Políticas de contraseñas inicializadas")
            else:
                print("ℹ️  Las políticas de contraseñas ya existen en la base de datos")
            
            # Configuración por defecto para políticas de 2FA
            default_2fa_policy = {
                'require_2fa_all': False,
                'require_2fa_admin': True,
                'grace_period_days': 7
            }
            
            # Verificar si ya existe la configuración de 2FA
            existing_2fa_policy = SystemConfig.query.filter_by(config_key='2fa_policy').first()
            
            if not existing_2fa_policy:
                print("🛡️  Creando configuración por defecto de políticas 2FA...")
                SystemConfig.set_config(
                    config_key='2fa_policy',
                    config_value=default_2fa_policy,
                    description='Políticas de autenticación 2FA del sistema',
                    updated_by='system'
                )
                print("✅ Políticas de 2FA inicializadas")
            else:
                print("ℹ️  Las políticas de 2FA ya existen en la base de datos")
            
            # Configuraciones adicionales del sistema
            system_configs = [
                {
                    'key': 'session_timeout',
                    'value': {'timeout_minutes': 30, 'remember_me_days': 7},
                    'description': 'Configuración de tiempo de sesión'
                },
                {
                    'key': 'security_settings',
                    'value': {'max_login_attempts': 5, 'lockout_duration_minutes': 15},
                    'description': 'Configuraciones de seguridad del sistema'
                },
                {
                    'key': 'backup_settings',
                    'value': {'auto_backup': True, 'backup_frequency_hours': 24, 'max_backups': 10},
                    'description': 'Configuraciones de respaldo automático'
                }
            ]
            
            # Crear configuraciones adicionales si no existen
            for config in system_configs:
                existing = SystemConfig.query.filter_by(config_key=config['key']).first()
                if not existing:
                    print(f"⚙️  Creando configuración: {config['description']}...")
                    SystemConfig.set_config(
                        config_key=config['key'],
                        config_value=config['value'],
                        description=config['description'],
                        updated_by='system'
                    )
                    print(f"✅ {config['description']} inicializada")
            
            print("\n🎉 ¡Configuraciones del sistema inicializadas correctamente!")
            print("\n📋 Configuraciones disponibles:")
            
            # Mostrar todas las configuraciones actuales
            all_configs = SystemConfig.query.all()
            for config in all_configs:
                print(f"   🔸 {config.config_key}: {config.description}")
            
            print(f"\n📊 Total de configuraciones: {len(all_configs)}")
            
        except Exception as e:
            print(f"❌ Error al inicializar configuraciones: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    
    return True

def show_current_config():
    """
    Muestra las configuraciones actuales del sistema.
    """
    from app import create_app
    from app.models import SystemConfig
    
    app = create_app()
    
    with app.app_context():
        try:
            print("\n📋 CONFIGURACIONES ACTUALES DEL SISTEMA")
            print("=" * 50)
            
            configs = SystemConfig.query.all()
            
            if not configs:
                print("⚠️  No hay configuraciones en el sistema")
                return
            
            for config in configs:
                config_dict = config.to_dict()
                print(f"\n🔸 {config.config_key.upper()}")
                print(f"   Descripción: {config.description}")
                print(f"   Actualizado por: {config.updated_by}")
                print(f"   Última actualización: {config.updated_at}")
                print(f"   Configuración:")
                
                for key, value in config_dict['config_value'].items():
                    print(f"      • {key}: {value}")
            
        except Exception as e:
            print(f"❌ Error al mostrar configuraciones: {str(e)}")

if __name__ == '__main__':
    print("🚀 INICIALIZADOR DE CONFIGURACIONES DEL SISTEMA")
    print("=" * 60)
    
    if len(sys.argv) > 1 and sys.argv[1] == 'show':
        show_current_config()
    else:
        success = initialize_system_config()
        if success:
            print("\n💡 Para ver las configuraciones actuales, ejecuta:")
            print("   python init_system_config.py show")
        else:
            sys.exit(1)