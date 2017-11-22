# progressBar

Pequeña utilidad para mostrar en CLI una barra de porcentaje.

## Instalación

    pip install git+git://github.com/felipem775/progressbar.git

## Uso

Para utilizarlo simplemente lo importamos y lo llamamos con dos o tres parámetros:
- Valor actual
- Valor máximo
- [Mensaje]


```python
import progressBar
progressBar.progressBar(2,20)
```

Resultado:
```
[======                                                           ]  2/20  10%
```

Si utilizamos como parámetro un mensaje aparecerá sobre la línea:

```python
import progressBar
progressBar.progressBar(2,20, "Moviendo ficheros")
```

Resultado:
```
Moviendo ficheros
[======                                                           ]  2/20  10%
```
