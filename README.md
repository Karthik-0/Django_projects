# Django_projects

## Events App
- Store event title, place (reuse Places App), tags (use taggit), created_by (user), created, modified (use django-model-utils TimeStampedModel)
- Store event timings (one event can have multiple timings or can be all day)
- Views for event detail, events list for a month, day, year and all events (use django-filter for filtering based on date, month etc)
- View to create event

## Movies app:

Movies should have the following information
- Title 
- Prefix
- Subtitle 
- Slug
- Directors
- Studio 
- Released date
- Cover image
- Review 
- Genre
- ASIN - ASIN stands for Amazon Standard Identification Number

A movie can be associated with only one studio however a studio can be associated with n number of movies.

The studio should have the following information
- Title
- Prefix
- Website
- Slug

A movie can have n number of genre and a genre can have n number of movies.

Genre should contain 
- Tile
- Slug

Similarly, a movie can have n number of directors and a director can have n number of movies.

Director can have basic information like 
- First name
- Last name
- Middle name
- Phone number
- Birthdate
- Website
- Gender

The required views are
- Movies list
- Movie detail
- Genre list
- Genre detail
- Studio list
- Studio detail
- Directors list
- Director detail

Consider, movie = Movie.objects.get(id=1). movie.amazon_url should return the Amazon URL for that movie using ASIN. Keep in mind amazon_url is not a model field.
