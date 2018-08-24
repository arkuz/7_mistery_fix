# Решатель квадратных уравнений

Данный проект посвящен решению квадратных уравнений. По входным данным `a, b, c` расчитывается дискриминант и находятся корни уравнений.

# Как использовать

Импортируем функцию `get_roots()` из модуля `quadratic_equation.py`
```python
from quadratic_equation import get_roots
```

Вызываем функцию с параметрами `get_roots(a, b, c)`.
```python
root1, root2 = get_roots(1, -2, 1)
```


# Как запускать

Создать файл `roots.py` с кодом:
```python
from quadratic_equation import get_roots

root1, root2 = get_roots(1, -2, 1)

print('root1 = {0}, root2 = {1}'.format(root1, root2))
```

Результат выполнения:
```bash
$python3 roots.py
root1 = 1.0, root2 = None
```

Запуск на Windows аналогичен.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
