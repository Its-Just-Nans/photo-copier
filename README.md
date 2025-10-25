
# photo-copier

Transfer your pictures easily !
Work only for __`Windows`__

You need the `PIL` module :

If you have `pip` in your path :

```sh
pip install pillow
```

or

```sh
PATH_TO_PIP install pillow
```

## Create an executable

With the executable, the start of the program is slower :(

If you want to create an executable, you need to have `PyInstaller` installed

If you have `pip` in your path :

```sh
pip install pyinstaller
```

or

```sh
PATH_TO_PIP install pyinstaller
```

Then you need to execute `pyinstaller` :

You need to be in the folder of the program

If you have `pyinstaller` in your path

```sh
pyinstaller .\main.spec
```

or

```sh
py -m PyInstaller .\main.spec
```
