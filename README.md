# gceni_testing (copy)

Pacote para TESTAR criação de pacotes:
+ skimage - exposure
+ skimage - filter

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install gceni_testing

```bash
pip install gceni_testing
```

## Usage

```python
from package_name import file1_name
file1_name.my_function()
```

## Author
GCeni

## License
[MIT](https://choosealicense.com/licenses/mit/)

# Anotações
## Conceitos
+ **Pypi**: Repositório público oficial de pacotes.
+ **Wheel & Sdist**: Tipos de distribuições.
+ **Setuptools**: pacote usdo em setup.py para gerar distribuições.
+ **Twine**: Pacote usado para subir as distribuições no repositório Pypi.

## Estruturas
### Simples
+ Estrutura: 

        project_name/
            README.md
            setup.py
            requirements.txt
            package_name/
                __init__.py
                file1_name.py
                file2_name.py
+ Importações:

        import package_name.file1_name
    ou

        from package_name import file1_name

### Vários Módulos
+ Estrutura:

        project_name/
            README.md
            setup.py
            requirements.txt
            package_name/
                __init__.py
                module1/
                    __init__.py
                    file1_name.py
                    file2_name.py
                module2/
                    __init__.py
                    file1_name.py
                    file2_name.py
+ Importações:

        import package_name.module1_name.file1_name

    ou

        from package_name.module1_name import file1_name

