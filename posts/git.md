```html

<html lang="en">
  <head>
```
```shell
git clone git@gitlab.com:waltergroup/test.git
git status
git add -u , git add ., git add -A
git commit -m "mensaje"
git push

git remote -v update #para ver si hay cambios en remote
git pull (fetch + merge)  
git log

git branch mirama
git checkout mirama  #switch to mirama
git checkout master #vuelve a master
git push -u origin mirama
git merge mirama #desde master
git push origin --delete mirama #borra rama en gitlab
git branch -d mirama #borra mirama local

### create repo from command line 
git init
git add -A
git commit -m "initial commit"
git remote add origin git@gitlab.com:waltermas/wtagger.git
git push -u origin master

git fetch #actualiza
git branch --list #local
git branch -r #remotes
git branch -a #all

git ls-tree -r master --name-only #list tracked files

## restore  
git restore file # deshace los cambios al ultimo commit
git commit --amend -m "Este es el mensaje correcto"  

## añadir mas cambios al ultimo commit:  
git add src/archivo-con-cambios.js
git commit --amend -m "Mensaje del commit"  


git reset --hard HEAD~1 #borra el ultimo commit, deja los archivos como estaba antes
git reset --soft HEAD~1 #borra el ultimo commit sin tocar los archivos
git revert 74a1092 #para una vez hecho el push  

```

