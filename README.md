# api-for-video-service
# Test Technical Task

- [Референсы](#референсы)  
- [🔴 DB](#🔴-db)  
    - [🔴 Film](#🔴-film)  
    - [🔴 Image](#🔴-image)  
    - [🔴 Type](#🔴-type)  
    - [🔴 Genre](#🔴-genre)  
    - [🔴 Audio](#🔴-audio)  
    - [🔴 Category](#🔴-category)  
    - [Season](#season)  
    - [Episode](#episode)  
- [Endpoint](#endpoint)  
    - [🔴 Films List Endpoint](#🔴-films-list-endpoint)  
    - [🔴 General](#🔴-general)  
    - [🔴 Pagination](#🔴-pagination)  
    - [🔴 Sorting](#🔴-sorting)  
    - [🔴 Filtering](#🔴-filtering)  
    - [🔴 Search](#🔴-search)  
    - [🔴 Errors Handling](#🔴-errors-handling)  
    - [🔴 Примечания](#🔴-примечания)  
    - [Film Details](#film-details)  
    - [Пример для сериала (есть сезоны и серии)](#пример-для-сериала-(есть-сезоны-и-серии))  

Тут будет описано техническое задание для создания API project для Video Service Application. Не все задачи есть
обязательными! Обязательные будут отмечены красным кружком.  

<font color="d44c47">Реализация с использованием гпт не интересует</font>

## Референсы
![](./reference.png)

## 🔴 DB

БД используем - Postgresql  
Для реализации нужно сделать такие модели:  

<font color="d44c47">Это просто описание сущностей и требований к полей. В реализации некоторых полей в моделях может не быть или они могут быть в других моделях, то есть нужно самому составить модели для работы с бд</font>

### 🔴 Film

```
name = обязательное поле, стринговое значение, длина которого не менее 2 символов и не более 150
description = опциональное поле, стринговое значение, длина которого не менее 50 символов и не более 350
release_year = интовое знаенчие 4-значное, которое не меньше 1900
type = тип фильма, связь с Type Model. Каждый фильм имеет только один тип всегда обязательное поле
genre = жанры фильма, может быть пустым и может быть много в одном фильме. связь с моделью Genre
seasons = необязательное, заполняется для таких типов как сериалы, аниме. не менее 1
category = обязательное поле
images = для каждого фильма может быть несколько. Связь с
```

### 🔴 Image

изображения фильмов

```
url = ссылка на файл на клауде, обязательное поле
is_main = булево значение, обязательное, по дефолту тру
```

### 🔴 Type

типи (фильм, сериал, аниме, подкаст и тд)

```
name = обязательное поле. уникальное название типа, стринговое значение не менее 2 и не более 50 символов
```
### 🔴 Genre

жанры фильмов

```
name = обязательное поле. уникальное название жанра, стринговое значение не менее 2 и не более 50 символов
```
### 🔴 Audio

озвучки фильмов (укр, англ, немецкий, польский и тд)

```
name = обязательное поле. уникальное название озвучки, стринговое значение не менее 2 и не более 50 символов
```
### 🔴 Category

возрастная категория. 16+ 18+ 6+ 0+ и тд

```
name = обязательное поле. уникальное название возрастной категории, стринговое значение не менее 2 и не более 3 символов
```
### Season

Если брать такую реализацию, то нужно поправить модель

```
film = обязательное поле, связь с Film Model. Каждый сезон привязан к одному фильму.
season_number = обязательное поле, интовое значение, отображает номер сезона в сериале.
description = опциональное поле, стринговое значение, длина которого не менее 50 символов и не более 350.
```
### Episode


```
season = обязательное поле, связь с Season Model. Каждая серия привязана к одному сезону.
episode_number = обязательное поле, интовое значение, отображает номер серии в сезоне.
name = обязательное поле, стринговое значение, длина которого не менее 2 символов и не более 150.
description = опциональное поле, стринговое значение, длина которого не менее 50 символов и не более 350.
duration = обязательное поле, продолжительность серии в формате времени (часы, минуты).
url = ссылка на клауд с файлом
```
## Endpoint

### 🔴 Films List Endpoint

#### 🔴 General

На главной странице у нас будут показан список доступных фильмов.  
Фильмы показаны карточками: на каждой карточке есть картинка постера фильма, название фильма и названия жанров, к
которым он относиться

**Endpoint:** `/api/films`  
    Нужно реализовать ендпоинт для листинга фильмов.  

**Sorting:**  
- Название фильма asc  
- Год выпуска desc  

**Fields:**  
- `id": {id}` из таблицы Film
- `"name": {name}` из таблицы Film
- `"description": {description}` из таблицы Film
- `"release_year": {release_year}` из таблицы Film
- `"type": {name}` из таблицы Type
- `"genre":` список `{name}` из таблицы Genre
- `"seasons": {seasons}` из таблицы Film (если применимо)
- `"category": {name}` из таблицы Category
- `"img": {url}` из таблицы Image, где поле `is_main` = true

Response Example:

```json
[
    {
        "id": 1,
        "name": "Inception",
        "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting a
        "release_year": 2010,
        "type": "Movie",
        "genre": ["Action", "Sci-Fi"],
        "seasons": null,
        "category": "18+",
        "img": "https://image-url-link.com"
    },
    {
        "id": 2,
        "name": "Stranger Things",
        "description": "When a young boy disappears, his mother, a police chief and his friends must confront terrifying supernatural forces in
        "release_year": 2016,
        "type": "Series",
        "genre": ["Drama", "Fantasy", "Horror"],
        "seasons": 4,
        "category": "16+",
        "img": "https://image-url-link2.com"
    }
]
```
#### 🔴 Pagination

Нужно реализовать пагинацию для ендпоинта листинга фильмов  
**Параметры:**
- `?page={page_number}` - номер страницы. По умолчанию `1` , если параметр не указан.

**Настройки пагинации:**  
- Нужно показывать на каждой странице по 10 фильмов


#### 🔴 Sorting

**Endpoint:** `/api/films?ordering=release_year`  
Нужно реализовать функциональность сортировки для ендпоинта листинга фильмов, позволяющую сортировать фильмыпо году их выпуска.  

**Sorting Parameters:**  
- `?ordering=release_year` - сортировка по возрастанию года выпуска  
- `?ordering=-release_year` - сортировка по убыванию года выпуска  

#### 🔴 Filtering

**Endpoint:** `/api/films?filter[type]={type}&filter[genre]={genre}&filter[category]={category}`  
Нужно реализовать функциональность фильтрации для ендпоинта листинга фильмов, позволяющую фильтровать фильмы по заданным критериям.  

**Filtering Parameters:**
- `?type={type_id}` - фильтрация по заданному типу фильма (ID из таблицы Type)
- `?genre={genre_id}` - фильтрация по заданному жанру (ID из таблицы Genre)
- `?category={category_id}` - фильтрация по заданной возрастной категории (ID из таблицы Category)

**Fields:**
- `"id": {id}` из таблицы Film
- `"name": {name}` из таблицы Film
- `"release_year": {release_year}` из таблицы Film
- `"img": {url}` из таблицы Image, где поле **is_main** = true

#### 🔴 Search

Нужно реализовать поиск фильмов по имени (film name contains search_query)


**Endpoint:** `/api/films/search?search={search_query}`  

**Параметры поиска:**
- `?search={search_query}` - строка поиска, введенная пользователем. Должна быть не пустой.

#### 🔴 Errors Handling

Нужно обработать ошибки, которые могут возникать при запросе  
404 - не коректный запрос, неправильные параметры фильтрации / сортировки, неправильная страница  
500 - ошибка сервера  

#### 🔴 Примечания

Паганиция, сортировка, фильтрация должны работать как отдельно, так и вместе  
Для поиска так же должны работать паганиция, сортировка, фильтрация как отдельно, так и вместе

### Film Details

**Endpoint:** `/api/v1/films/<int:id>/`  
Пример: `/api/v1/films/4/`  

**Fields:**  
- `"id"` : `{id}` from `Film` table
- `"name"` : `{name}` from `Film` table
- `"description"` : `{description}` from `Film` table (если есть)
- `"release_year"` : `{release_year}` from `Film` table
- `"type"` : `{name}` from `Type` table related to the film
- `"genre"` : array of `{name}` from `Genre` table related to the film
- `"seasons"` : `{seasons}` from `Film` table (если тип - сериал или аниме)
- `"category"` : `{name}` from `Category` table related to the film
- `"images"` : array of `{url}` from `Image` table

**Пример ответа:**  

```json
{
    "id": 4,
    "name": "The Dark Knight",
    "description": "When the menace known as the Joker emerges...",
    "release_year": 2008,
    "type": "Фильм",
    "genre": ["Экшн", "Драма"],
    "seasons": null,
    "category": "16+",
    "images": [
        "https://images.unsplash.com/photo-1599940824219-e6aa9be5fba2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Y2FycGF0aGlhbnN8ZW58MH"
        "https://images.unsplash.com/photo-1599940824219-e6aa9be5fba2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Y2FycGF0aGlhbnN8ZW58MH"
        "https://images.unsplash.com/photo-1599940824219-e6aa9be5fba2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Y2FycGF0aGlhbnN8ZW58MH"
        "https://images.unsplash.com/photo-1599940824219-e6aa9be5fba2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Y2FycGF0aGlhbnN8ZW58MH"
    ]
}
```

**Ожидаемый ресурсный метод:** `GET`

**Статусы ответа:**  
- `200 OK` - если информация о фильме успешно получена
- `404 NOT FOUND` - если фильм с указанным ID не найден
- `500 INTERNAL SERVER ERROR` - если произошла ошибка на сервере

### Пример для сериала (есть сезоны и серии)

Endpoint: `/api/v1/films/4/`  
Endpoint: `/api/v1/films/4?season=`  

```json
{
    "film_id": 6,
    "film_name": "Игра престолов",
    "film_description": "Эпическая сага о мире Вестероса, где дома сражаются за железный трон.",
    "release_year": 2011,
    "type": "Сериал",
    "genre": ["Фэнтези", "Драма"],
    "category": "18+",
    "seasons": [
        {
            "season_id": 54,
            "season_number": 1,
            "description": "Первый сезон введет вас в мир интриг и борьбы за власть.",
            "total_episodes": 10
        },
        {
            "season_id": 55,
            "season_number": 2,
            "description": "Война пяти королей начинается...",
            "total_episodes": 24
        }
    ],
    "current_season_details": {
        "season_id": 54,
        "season_number": 1,
        "description": "Первый сезон введет вас в мир интриг и борьбы за власть.",
        "episodes": [
            {
                "episode_id": 101,
                "episode_number": 1,
                "name": "Зима близко",
                "description": "Нед Старк получает предложение стать Рукою короля...",
                "duration": "01:00:00",
                "url": "https://cloud-storage.com/path/to/episode_101"
            },
            {
                "episode_id": 102,
                "episode_number": 2,
                "name": "Королевский путь",
                "description": "Семья Старков отправляется в королевскую столицу...",
                "duration": "00:58:00",
                "url": "https://cloud-storage.com/path/to/episode_102"
            }
        ]
    }
}
```


