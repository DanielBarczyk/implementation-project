### pip & venv

Tworzenie izolowanego środowiska:
```sh
# ↓program↓   ↓uruchom moduł venv↓   ↓argument – ścieżka do folderu↓
    python           -m venv                      .venv
#  
```
Aktywacja środowiska:
```sh
source .venv/bin/activate
```
Instalowanie zależności:
```sh
# ↓program↓   ↓uruchom moduł pip↓   ↓           argumenty          ↓
    python           -m pip         install -r requirements_list.txt
#  
```
pip freeze:
```sh
# ↓program↓   ↓uruchom moduł pip↓   ↓argumenty↓
    python           -m pip            freeze    > requirements_lock_versions.txt
#  
```
