[Help](https://neovim.io/doc/user/index.html)   
[Book](https://learnvimscriptthehardway.stevelosh.com/)   

### Archivo de configuracion
/home/waltermas/.config/nvim/init.vim

### vim-plug
```shell
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
``` 
:PlugInstall  

### Coc
[coc-extensions](https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions)  
```shell
curl -sL install-node.now.sh/lts | bash  #para coc
``` 

:cocList extensions  




### COMANDOS
:w write  
:e edit, abre un archivo  
:tabnew  
:r retrieve pega un archivo  
:! ejecuta un comando  
:.! salida del comando a vim  

### MOVERSE
numero +  
numero -  
numero %, va hasta el porcentaje  

w b   moverse entre palabras  
e     end of the word  
f F   saltar a letra  

H high  
M ir al medio  
L low  

control u, moverse up  
control d, moverse down  
control y, scroll up  
control e, scroll down  
control o, vuelve donde estaba despues de un salto  

control u en insert borra hasta el principio de la linea  

gt cambia de tab  
gg va al principio  
G va al final  
:numero ---salta a esa linea  
:+14,+18 co .   --- copia la linea relativa 14 a 18 aqui  

:+14y  copia linea relativa 14  
:+4d   borrar linea relativa 4  

d4k   borra 4 lineas para arriba   

0 principio de linea  
$ final de linea  
= easymotion =  
leader f: search one character  
leader s: search two character  
leader l: jump to line
leader w: jump to word


### INSERT
i - I insert at the beggining of the line  
a append - A append at the end of the line  
o nueva linea - O nueva linea arriba  

x borra bajo el cursor  
d delete  
dw borra una palabra  
dd corta toda la linea  

p paste  
y copy  
yy yank a line  
yiw yank in word copia la palabra bajo el cursor  
espacio y, lista de yanks, from coc-yank  

u undo  
control-r redo  
. repeat  
/ search , n next, N previous  
? seach backwards  
\* busca siguiente palabra bajo el cursor  

shift v visual line mode  

cw change word  
ciw change entire word  
cc change line  
dw  delete word  
ci( change inside parentesis  
yt,    yank till , 

vib select inner block  
vi" select inside quotes  

### REGISTERS
:registers  
"ayy  copia linea en register a  
"ap   pega linea del register a  
control r a en insert mode  

### MARKS
:marks  
ma marca donde esta el cursor, lo almacena en a  
'a va hasta el marcador a (linea)  
`a va hasta el marcador a (lugar exacto)  
markbar: leader m    toggle markbar

### FZF
:FZF  
:Files  abre archivo con preview  
:Rg   busca string dentro de los archivos  
:BLines busca string dentro de archivo abierto  
:Lines leader f busca string dentro de todos los buffers  
:History:
:Buffers
:Marks


:colorscheme <tab>  

:buffers  
:b <tab> para cambiar buffers
leader b

:history  

leader e   coc-explorer

### EMMET  
html:5 <ctrl-y>,  expande html  
div  
p  
a  
img  


### TABS  
tn :tabnew  
tl :tabnext  
th :tabprevious  

### MAPPINGS
:verbose vmap i 

### ultisnipedit
👆 genial
