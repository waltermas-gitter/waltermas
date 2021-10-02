[bat](https://github.com/sharkdp/bat)  
***a cat replacement***

### install
```shell
# arch
pacman -S bat

# ubuntu, executable: batcat
apt install bat 
```

### plain output
```shell
bat -p file
bat --plain file
```

Nice oneliner to show all themes preview with fzf:
```shell
bat --list-themes | fzf --preview="bat --theme={} --color=always posteos.md"
#To set a theme:
export BAT_THEME="TwoDark"
```

***

[exa](https://the.exa.website)  
***a ls replacement***

### install
Just download and place on bin folder

```shell
exa --all
exa --recurse or -R
exa -l  #long
exa -1 #one per line
exa --header
exa --tree
exa --git
exa --icons
```

### custom colors:
```shell
export LS_COLORS="*.html=37;41"
```

***
[ripgrep](https://github.com/BurntSushi/ripgrep)

```shell
rg text #recursive by default
rg 'regular expression'
rg 'glob expression'

--hidden
-i/--ignore-case

rg text --type html  =  rg text -html
rg text --type-not html  =  rg text -Html
rg --type-list

rg fast README.md --replace FAST = rg fast README.md -r FAST

```

***

[fd](https://github.com/sharkdp/fd)

***find replacement***
```shell
fd text  #recursively
fd 'regular expression'

fd text /directory

fd --extension md  =  fd -e md
--hidden = -H

-x/--exec option runs an external command for each of the search results
-X/--exec-batch runs once for all results

--exclude = -E  #exclude directory


```


