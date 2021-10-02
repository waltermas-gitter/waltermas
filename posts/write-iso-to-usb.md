Comprobar que el usb no esta montado:  
sudo lsblk -l

sudo umount /dev/sd<?><?>


sudo dd bs=4M if=path/to/input.iso of=/dev/sd<?> conv=fdatasync  status=progress

## Otros programas:
unetbootin

etcher
