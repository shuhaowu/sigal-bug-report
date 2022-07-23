```
Collecting albums /Traceback (most recent call last):
  File "/home/shuhao/.local/bin/sigal", line 8, in <module>
    sys.exit(main())
  File "/usr/lib/python3/dist-packages/click/core.py", line 1128, in __call__
    return self.main(*args, **kwargs)
  File "/usr/lib/python3/dist-packages/click/core.py", line 1053, in main
    rv = self.invoke(ctx)
  File "/usr/lib/python3/dist-packages/click/core.py", line 1659, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/lib/python3/dist-packages/click/core.py", line 1395, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/lib/python3/dist-packages/click/core.py", line 754, in invoke
    return __callback(*args, **kwargs)
  File "/home/shuhao/.local/lib/python3.10/site-packages/sigal/__init__.py", line 173, in build
    gal = Gallery(settings, ncpu=ncpu, quiet=quiet)
  File "/home/shuhao/.local/lib/python3.10/site-packages/sigal/gallery.py", line 743, in __init__
    album = Album(relpath, settings, dirs, files, self)
  File "/home/shuhao/.local/lib/python3.10/site-packages/sigal/gallery.py", line 395, in __init__
    media = Image(f, self.path, settings)
  File "/home/shuhao/.local/lib/python3.10/site-packages/sigal/gallery.py", line 238, in __init__
    if imgformat and PILImage.EXTENSION[self.src_ext] != imgformat.upper():
KeyError: '.png'
```
