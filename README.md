
# photo-copier

Transfer your pictures easily !
Work only for __`Windows`__

You need the `PIL` module :

```sh
python -m pip install pillow
```

## Usage with Pypi

```sh
python -m pip install -U photo-copier
python -m photo_copier
```

## Create an executable

With the executable, the start of the program is slower :(

If you want to create an executable, you need to have `PyInstaller` installed

If you have `pip` in your path :

```sh
python -m pip install pyinstaller
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
