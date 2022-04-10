.. register file documentation master file, created by
   sphinx-quickstart on Mon Apr  4 13:08:55 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Описание проекта
================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
.. _сетей: https://uneex.ru/LecturesCMC/LinuxNetwork2022
.. _Veniamin-Arefev: https://github.com/Veniamin-Arefev
.. _Uberariy: https://github.com/Uberariy
.. _stamplevskiyd: https://github.com/stamplevskiyd

Суть проекта:
Проверять письма по курсу сетей_. И в автоматическом режиме показывать оперативную статистику на сайте

Участники:

    #. Арефьев Вениамин Андреевич, группа 321, nick: Veniamin-Arefev_
    #. Оконишников Арий Ариевич, группа 321, nick: Uberariy_
    #. Стамплевский Дмитрий Максимович, группа 321, nick: stamplevskiyd_

Ссылка на публичный репозиторий:
https://github.com/Veniamin-Arefev/NetJudge

Пример исходного кода:
======================
.. code-block:: python
   :linenos:

   def ip_address(config, args):
       """Parses ip address command
       Returns True if command is correct
       """
       if 'add'.startswith(args[0]):  # ip addr add ...
           if not 'dev'.startswith(args[1]):
               return False
           dev = args[2]
           ip_addr = args[3]  # можно и без маски
           if not re.fullmatch(ip_regexp, ip_addr):
               return False
           state = config.devices[dev].state if dev in config.devices.keys() else 'down'
           config.devices[dev] = config.Interface(ip_addr, state)
           return True
       elif 'delete'.startswith(args[0]):  # ip addr del ...
           if not 'dev'.startswith(args[1]):
               return False
           dev = args[2]
           config.devices[dev] = ('No_ip_yet', 'down')
           return True

Скриншот:
==========
.. image:: _static/screenshot.png
