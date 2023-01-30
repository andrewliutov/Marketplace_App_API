from market.celery import app
from .service import new_user_registered_signal, new_order_signal


@app.task
def new_user_email(user_id):
    new_user_registered_signal(user_id)


@app.task
def new_order(user_id):
    new_order_signal(user_id)
