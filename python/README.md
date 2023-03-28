# Implementace hada v Pythonu

Tento had vyžaduje pro svůj běh [Flask](https://flask.palletsprojects.com/) (odzkoušeno na verzi 2.2.3).

Pro instalaci závislostí nejprve spusťte příkaz `python -m pip install Flask` nebo nainstalujte balíček Flask [Thonnyho](https://thonny.org/)

Samotného hada lze spustit souborem `run.cmd` nebo přímo z [Thonnyho](https://thonny.org/)

Do konfiguračního soubor `src\config.py` vyplňte údaje (např. pro hada týmu #8)
```
PORT = 6008
NAME = "Had týmu #8"
```

Samotného hada najdete v souboru `src\snake.py`, kde změníte tělo funkce `move`
