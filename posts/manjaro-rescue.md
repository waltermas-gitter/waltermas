These are useful resources I found when my manjaro broke.

I guess it broke because of I update base-devel only, and not the whole system.

<span style="color: red">pacman-static</span> saved my life

wget https://pkgbuild.com/~eschwartz/repo/x86_64-extracted/pacman-static

*arch-chroot*
from package *arch-install-scripts*

[chroot wiki](https://wiki.archlinux.org/index.php/Chroot_(Español))

```shell
mount /mnt /dev/sd9 
arch-chroot /mnt
```

Also I modified locales:  
[locale wiki](https://wiki.archlinux.org/index.php/Locale_(Español))


