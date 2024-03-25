Step 1- go to the terminal
Step 2- write - poetry run python manage.py runserver
step 3- open another terminal (while running first terminal)
#FOR CELERY
Step 1- celery -A cinema worker -l INFO
step 2- open another terminal (while running sceond terminal)
Step 3- celery -A cinema beat -l INFO

#FOR Pytest
step 1- open another terminal (while running first terminal)
step 2 - pytest

1.I never used content based and collaborative filterting . But I used postgreSQL for efficient storage and querying of user preferences and movie metadata.
2.I prefer PostgreSQL while I have worked with it.And know that instagram, snapchat, Tweeter have used for database management.
3.I have set up both internally and virtually django-celery.I have made a celery.py file where I setup for task method when should it go and do the work.And in app folder I have made tasks.py where the task is assign. I have faced difficulties in controlling inputing the
django-setup first of all in the tasks.py then the code was running good.
