#!/bin/bash

# Eliminar los paquetes huérfanos
sudo pacman -Rs $(pacman -Qdtq)

# Limpiar la caché de paquetes descargados
sudo pacman -Sc

# Limpiar la caché de todos los paquetes
sudo pacman -Scc

