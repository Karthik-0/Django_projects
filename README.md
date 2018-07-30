# Django_projects

## Events App
- Store event title, place (reuse Places App), tags (use taggit), created_by (user), created, modified (use django-model-utils TimeStampedModel)
- Store event timings (one event can have multiple timings or can be all day)
- Views for event detail, events list for a month, day, year and all events (use django-filter for filtering based on date, month etc)
- View to create event