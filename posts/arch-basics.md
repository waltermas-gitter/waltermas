### PC name
*/etc/hostname*
### pacman
```shell
pacman -S package  #install package
# S stands for syncronization

# Manual install
pacman -U _/path/to/package/package_name-version.pkg.tar.xz_
pacman -U http://www.example.com/repo/example.pkg.tar.xz

pacman -R package #remove package
pacman -Rs package #remove package and dependencies

pacman -Syu #update the system
S = sync
y = refresh
u = update

pacman -Ss string #search string
pacman -Qs string #search for installed packages
pacman -Qe #lists all installed packages
pacman -F string #search for package files

pactree package #tree of dependencies

paccache -r #delete database but the last 3 versions, from pacman-contrib
pacman -Sc #remove all unused packages
pacman -Scc #remove all cache files
```

### Nice scripts from the [wiki](https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks) 
```shell
#preview of install packages:
pacman -Qq | fzf --preview 'pacman -Qil {}' --layout=reverse --bind 'enter:execute(pacman -Qil {} | less)'

# Search for packages
pacman -Slq | fzf --preview 'pacman -Si {}' --layout=reverse
```

### Mirrors
Edit */etc/pacman.d/mirrorlist* uncomment the one you want

arch mirrorlist [generator](https://archlinux.org/mirrorlist/)

### Yay
```shell
cd /opt
sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R waltermas:waltermas ./yay-git
cd yay-git
makepkg -si
```

### Nice scripts from the [fzf wiki](https://github.com/junegunn/fzf/wiki/examples)
```shell
#search for package:
yay -Slq | fzf -q "$1" -m --preview 'yay -Si {1}'

```
