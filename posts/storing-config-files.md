Pasos que segui:  
```shell
git init --bare $HOME/.cfg
alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
config config --local status.showUntrackedFiles no
echo "alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'" >> $HOME/.zshrc

config remote add origin git@gitlab.com:waltermas/kiss2configfiles.git
config push --set-upstream origin master

```

[tutorial](https://www.atlassian.com/git/tutorials/dotfiles)

Para ver archivos que sigo:
```shell
cd ~ && config ls-tree -r master --name-only
```

