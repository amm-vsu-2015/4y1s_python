## Вводное занятие. Установка среды

### Задание

```
– Установить необходимый софт.
– Прочитать "4. Неформальное введение в Python" до заголовка "5.7. Подробнее об определении функций" в "Учебник_Python_3.1".
```

### Установка дистрибутивов и среды разработки

Для начала устанавливаем дистрибутив [Anaconda](https://www.anaconda.com/download/#windows) с версией Python 3.7.x. После установки все необходимые пакеты будут доступны, как и сам Python. Дистрибутив представляет собой набор программ. В данном случае, Python и ряд пакетов.

В целом, на этом можно и закончить. Но для удобства есть возможность поставить среду разработки [PyCharm](https://www.jetbrains.com/pycharm/) -> Download -> Community Edition. Можно поставить и Ultimate, получив лицензию через [github educaton pack](https://education.github.com/pack).

После установки PyCharm, его можно просто запустить. Он предложит настройки по вкусу. Далее, создаем новый проект. PyCharm автоматически увидит установленную Anaconda с пробросит необходимые зависимости.

### Альтернатива: установка чистого python и необходимых пакетов

Если кто-то захочет самостоятельно установить пакеты и python без ёмкого Anaconda.

Устанавливаем Python: (mac/linux)

```shell
Обычная установка для Mac через Homebrew:

brew install python # начиная с версии 3.4, пакетный менеджер pip поставляется с python.


# https://github.com/pyenv/pyenv
Для Mac через pyenv: (благодаря различным средам, можно изолировать приложения, скачивать много версий python)

brew install pyenv # install pyenv
echo 'eval "$(pyenv init -)"' >> ~/Projects/config/env.sh # configure environment
exec $SHELL # restart your $shell (bash or other)

pyenv install 3.7.0 # install python 3.7

# На этом этапе можно установить Anaconda отдельно (либо позже использовать пакеты, вместо неё)

pyenv install anaconda3-4.1.1 # установка anaconda
cd path/to/directory # переход в директорию проекта
pyenv local anaconda3-4.1.1 # установка anaconda как версии python (local – только для этой директории)
pyenv rehash # как бы перехешить настройки

pyenv versions
  system
  2.7.12
  3.5.2
* anaconda3-4.1.1 (set by /Users/your_account/path/to/directory/.python-version)

```

Устанавливаем пакеты:

```shell
pip install numpy # и так далее
pip list # проверить установленные пакеты
```

## Как запускать программы в pycharm

1. Создаете проект (new project) -> выбираете python 3.7 anaconda.
2. Создаете файл, в котором будете писать программу
3. Добавляете конфигурацию (add configuration / run -> add configuration)
4. Конфигурация добавляется нажатием плюсика слева сверху и выбором шаблона (python).
5. В поле script указываете файл программы (путь до него можно указать нажатием иконки папки справа)
