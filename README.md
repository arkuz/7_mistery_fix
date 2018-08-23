# Решатель квадратных уравнений

Данный проект посвящен знакомству с таким понятием, как тестирование, а конкретно с модулем unittest. В скрипте quadratic_equation.py находится алгоритм решения квадратных уравнений. В скрипте tests.py содержатся тесты для алгоритма квадратных уравнений. 

# Как использовать

```bash
Name of file "roots.py"

from quadratic_equation import get_roots

def print_roots(root1, root2):
    print(root1)
    print(root2)

root1, root2 = get_roots(1, -2, 1)
print_roots(root1, root2)
root1, root2 = get_roots(1, 2, -3)
print_roots(root1, root2)
root1, root2 = get_roots(1, -2, 1)
print_roots(root1, root2)
root1, root2 = get_roots(1, 2, 3)
```
# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python3 tests.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

python3 roots.py
1.0
None
-3.0
1.0
1.0
None
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
