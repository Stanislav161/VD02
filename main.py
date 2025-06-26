< !DOCTYPE
html >
< html
lang = "ru" >
< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > Карточки
пользователей < / title >
< style >
*{
    margin: 0;
padding: 0;
box - sizing: border - box;
font - family: 'Segoe UI', Tahoma, Geneva, Verdana, sans - serif;
}

body
{
    background: linear - gradient(135deg,  # 6a11cb 0%, #2575fc 100%);
min - height: 100
vh;
display: flex;
justify - content: center;
align - items: center;
padding: 20
px;
}

.container
{
    display: flex;
flex - wrap: wrap;
justify - content: center;
gap: 30
px;
max - width: 1200
px;
}

.card
{
    width: 320px;
background: white;
border - radius: 20
px;
overflow: hidden;
box - shadow: 0
10
px
30
px
rgba(0, 0, 0, 0.15);
transition: all
0.4
s
ease;
}

.card: hover
{
    transform: translateY(-15px);
box - shadow: 0
15
px
40
px
rgba(0, 0, 0, 0.25);
background: linear - gradient(135
deg,  # ffffff 0%, #f8f9fa 100%);
}

.card: hover.photo
{
    transform: scale(1.1);
border: 5
px
solid  # 6a11cb;
}

.photo - container
{
    width: 100 %;
height: 220
px;
overflow: hidden;
background:  # 2575fc;
display: flex;
justify - content: center;
align - items: center;
}

.photo
{
    width: 150px;
height: 150
px;
border - radius: 50 %;
object - fit: cover;
border: 5
px
solid
rgba(255, 255, 255, 0.3);
transition: all
0.4
s
ease;
box - shadow: 0
5
px
15
px
rgba(0, 0, 0, 0.2);
}

.info
{
    padding: 25px;
text - align: center;
}

h2
{
    color:  # 2c3e50;
        margin - bottom: 15
px;
font - size: 1.6
rem;
}

.detail
{
    display: flex;
align - items: center;
margin: 12
px
0;
color:  # 34495e;
}

.detail
i
{
    width: 24px;
color:  # 2575fc;
font - size: 1.1
rem;
margin - right: 10
px;
}

.email
{
    color:  # 2980b9;
        word -
break: break
-all;
}
< / style >
    <!-- Иконочный
шрифт
Font
Awesome -->
< link
rel = "stylesheet"
href = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" >
       < / head >
           < body >
           < div


class ="container" >

< !-- Карточка
1 -->
< div


class ="card" >

< div


class ="photo-container" >

< img
src = "https://randomuser.me/api/portraits/women/65.jpg"
alt = "Фото пользователя"


class ="photo" >

< / div >
< div


class ="info" >

< h2 > Иванова
Мария
Петровна < / h2 >
< div


class ="detail" >

< i


class ="fas fa-envelope" > < / i >

< span


class ="email" > ivanova.maria @ example.com < / span >

< / div >
< div


class ="detail" >

< i


class ="fas fa-birthday-cake" > < / i >

< span > 15
марта
1992 < / span >
< / div >
< div


class ="detail" >

< i


class ="fas fa-city" > < / i >

< span > Москва < / span >
< / div >
< / div >
< / div >

< !-- Карточка
2 -->
< div


class ="card" >

< div


class ="photo-container" >

< img
src = "https://randomuser.me/api/portraits/men/32.jpg"
alt = "Фото пользователя"


class ="photo" >

< / div >
< div


class ="info" >

< h2 > Смирнов
Алексей
Владимирович < / h2 >
< div


class ="detail" >

< i


class ="fas fa-envelope" > < / i >

< span


class ="email" > smirnov.alexey @ company.ru < / span >

< / div >
< div


class ="detail" >

< i


class ="fas fa-birthday-cake" > < / i >

< span > 28
июля
1988 < / span >
< / div >
< div


class ="detail" >

< i


class ="fas fa-city" > < / i >

< span > Санкт - Петербург < / span >
< / div >
< / div >
< / div >

< !-- Карточка
3 -->
< div


class ="card" >

< div


class ="photo-container" >

< img
src = "https://randomuser.me/api/portraits/women/44.jpg"
alt = "Фото пользователя"


class ="photo" >

< / div >
< div


class ="info" >

< h2 > Козлова
Екатерина
Сергеевна < / h2 >
< div


class ="detail" >

< i


class ="fas fa-envelope" > < / i >

< span


class ="email" > kate.koz @ mail-service.com < / span >

< / div >
< div


class ="detail" >

< i


class ="fas fa-birthday-cake" > < / i >

< span > 3
декабря
1995 < / span >
< / div >
< div


class ="detail" >

< i


class ="fas fa-city" > < / i >

< span > Казань < / span >
< / div >
< / div >
< / div >
< / div >
< / body >
< / html >