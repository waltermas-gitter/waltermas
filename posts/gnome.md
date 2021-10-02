**Themes**  
[gnome look org](https://www.gnome-look.org/browse/cat/)  
en carpetas:  
~/.icons  
~/.themes

**Desktop entry**  
```shell
[Desktop Entry]
Type=Application
Encoding=UTF-8
Version=1.0
Name=Locker
GenericName=Locker
Comment=my fast lock app
Exec=/home/waltermas/MEGAsync/scripts/locker.sh
Icon=/home/waltermas/.icons/iconfinder_icon-118-lock-rounded_314696.png
Categories=GNOME;Application;
```

[desktop entry documentation](https://wiki.archlinux.org/title/desktop_entries)


En */usr/share/applications*{: style="color: blue"} van las entradas de menu  
En *~/.local/share/applications*{: style="color: blue"} van las entradas de menu para el usuario  
En *~/.config/autostart*{: style="color: blue"} van los programas al inicio

**dconf-editor**  
Para configurar atajos  
/org/gnome/desktop/wm/keybindings/switch-applications

Para cambiar el tamaño del cursor:  
dconf write /org/gnome/desktop/interface/cursor-size 48

Borro trash del dock:  
/org/gnome/shell/extensions/dash-to-dock/show-trash

**Custom launcher for VM**
```shell
VBoxManage setextradata global GUI/DistinguishMachineWindowGroups true
xprop WM_CLASS
#WM_CLASS(STRING) = "VirtualBox Machine UUID: {9c1f2428-9e1d-43cb-a3f8-3f0967bfa190}", "VirtualBox Machine"

#In ~/.local/share/applications/lubuntu21.desktop
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Name=lubuntu 21
Comment=Starts the VirtualBox machine lubuntu 21
Type=Application
Exec=/usr/lib/virtualbox/VirtualBoxVM --comment "lubuntu 21" --startvm "{9c1f2428-9e1d-43cb-a3f8-3f0967bfa190}"
Icon=lubuntu_logo
StartupWMClass=VirtualBox Machine UUID: {9c1f2428-9e1d-43cb-a3f8-3f0967bfa190}

```

gtk-launch  
