<a href="https://copyq.readthedocs.io/en/latest/index.html">copyq documentation</a>

copyq show

copyq menu

copyq popup "hola"

copyq tab notas add "prueba nota"

copyq copy - < textfile.txt

my google selection script:  
```shell
copyq:
execute('opera', 'http://google.com/search?q=' + str(selection()))
``` 

my todo scripts:

```shell
#todoq-add:
#!/bin/bash
copyq tab todo add "$@"

#todoq-list
#!/bin/bash
N=`copyq tab todo count`
for (( i=0; i<$N; i++ ))
do
	echo $i 📌 `copyq tab todo read $i`
done

#todoq-remove:
#!/bin/bash
copyq tab todo remove $1
```


