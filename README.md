<h1>Detecção e Binarização de placas de carros por imagens</h1>
<br>

<p>
    A ideia desse projeto é testar a detecção e a binarização de placas de carros
    localizadas em uma pasta do computador.
    A Detecção das placas é feita utilizando a classificação por cascata ( haarcascade ) presente na
    biblioteca OpenCv.
    A Binarização é feita manualmente, a partir da imagem preta e branca resultante da detecção.
</p>


### No Windows
1 - Instalar todas as dependências
```bash
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

2 - Executar
```bash
venv\Scripts\activate.bat
python run.py
```

<br>

### No Linux
1 - Instalar todas as dependências
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2 - Executar
```bash
source venv/bin/activate
python run.py
```
