### Install on manjaro
```shell
sudo pacman -Sy openssh 
sudo systemctl status sshd.service
sudo systemctl enable sshd.service
sudo systemctl start sshd.service
```

#### Edit config file
```shell
sudo nvim /etc/ssh/sshd_config
```

#### ifconfig
