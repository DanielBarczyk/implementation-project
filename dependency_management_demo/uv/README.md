# UV
Tworzenie nowego projektu
```sh
uv init
```
Dodawanie nowej dependencji
```sh
uv add PACKAGE_NAME
```
Instalowanie dependencji na podstawie uv.lock (pyproject.toml w przypadku braku uv.lock)
```sh
uv sync
```
Uruchamianie programu
```sh
uv run FILE_NAME
```
Używanie uv jako zamiennika dla pip:
```sh
uv pip install PACKAGE_NAME
```
Używanie uv jako zamiennika dla venv:
```sh
uv venv
```
Używanie uv do instalacji Pythona:
```sh
uv python install 3.12
```
