#!/bin/bash

# Actualizar los repositorios
sudo pacman -Syu --noconfirm

# Lista de paquetes a instalar desde los repositorios oficiales
pacman_packages=(
  "xclip"
  "pcmanfm"
  "firefox"
  "alacritty"
  "audacious"
  "keepass"
  "alsa-utils"
  "pavucontrol"
  "gvfs"
  "feh"
  "picom"
  "gparted"
  "vlc"
  "tmux"
  "klavaro"
  "xorg-xinput"
  "tree"
)

# Instalar los paquetes desde los repositorios oficiales
for package in "${pacman_packages[@]}"
do
  echo "Instalando $package..."
  sudo pacman -S --noconfirm $package
done

# Instalar AUR helper (yay) si no está instalado
if ! command -v yay &> /dev/null
then
  echo "Instalando yay (AUR helper)..."
  git clone https://aur.archlinux.org/yay.git
  cd yay
  makepkg -si --noconfirm
  cd ..
  rm -rf yay
fi

# Lista de paquetes a instalar desde AUR
aur_packages=(
  "brave-bin"
  "simplescreenrecorder"
  "cava"
  "woeusb"
  "dosfstools"
)

# Instalar los paquetes desde AUR
for aur_package in "${aur_packages[@]}"
do
  echo "Instalando $aur_package desde AUR..."
  yay -S --noconfirm $aur_package
done

echo "Instalación de programas completada."
