#!/bin/bash

# Obtener la ruta del directorio actual donde se encuentra el script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Ruta completa de dotfiles_backup
BACKUP_DIR="$SCRIPT_DIR/dotfiles_backup"

# Verificar si dotfiles_backup ya existe y limpiar su contenido si es necesario
if [ -d "$BACKUP_DIR" ]; then
	rm -rf "$BACKUP_DIR"/*
else
	mkdir -p "$BACKUP_DIR"
fi

# Copiar las carpetas
cp -r ~/.config/alacritty ~/.config/i3 ~/.config/rofi "$BACKUP_DIR"/

# Copiar el archivo desde el directorio home
cp ~/.zshrc "$BACKUP_DIR"/
