Программа для сокрытия/(извлечения сокрытой) информации
в bmp файле (используется True Color). Формат сокрытия 1 байт
скрываемой информации скрывается в одном пикселе (по 2 бита на
цвет(6 бит) и еще 2 бита на неиспользуемый в True Color альфа канал). 

Стеганография - способ передачи или хранения информации с учётом сохранения в тайне самого самого факта передачи.
В отличие от криптографии, которая скрывает содержимое секретного
сообщения, стеганография скрывает сам факт его существования.

Метод LSB (Least Significant Bit, наименьший значащий бит) — суть этого
метода заключается в замене последних значащих битов в контейнере
(изображения, аудио или видеозаписи) на биты скрываемого
сообщения. Разница между пустым и заполненным контейнерами
должна быть не ощутима для органов восприятия человека.

Суть метода заключается в следующем: допустим, имеется 8-битное
изображение в градациях серого. 00h (00000000b) обозначает чёрный
цвет, FFh (11111111b) — белый. Всего имеется 256 градаций (2^8).
Также предположим, что сообщение состоит из 1 байта — например,
01101011b. При использовании 2 младших бит в описаниях пикселей,
нам потребуется 4 пикселя. Допустим, они чёрного цвета. Тогда
пиксели, содержащие скрытое сообщение, будут выглядеть следующим
образом: 00000001 00000010 00000010 00000011. Тогда цвет пикселей
изменится: первого — на 1/255, второго и третьего — на 2/255 и
четвёртого — на 3/255. Такие градации, мало того, что незаметны для
человека, могут вообще не отобразиться при использовании
низкокачественных устройств вывода.

Важно: изображение сохраняется построчно СНИЗУ-ВВЕРХ. Для хранения
каждой строки выделяется кратное 4 количество байт. В незначащих
байтах хранится мусор.
