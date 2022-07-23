```
$ sigal build
Collecting albums, done.
  Sorting albums  [####################################]  100%
   Sorting media  [####################################]  100%
Collecting files  [####################################]  100%   
Processing files  [####################################]  1/1
   Writing files  [####################################]  100%
$ ls -l build/
total 20
-rw-rw-r-- 1 shuhao shuhao  4001 Jul 23 17:02 index.html
drwxrwxr-x 1 shuhao shuhao   306 Jul 23 15:06 static
drwxrwxr-x 1 shuhao shuhao    26 Jul 23 17:02 thumbnails
-rw-rw-r-- 1 shuhao shuhao 12765 Jul 23 17:02 Untitled.jpeg
$ find -name "*.zip"
<no output>
```
