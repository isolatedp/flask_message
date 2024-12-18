from datetime import datetime
import traceback

from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
import pytz

from app.utils.get_request_ip import get_request_ip
from app.extensions import db
from app.models.sayhello_db import Message
from .forms import MessageForm

class Index(MethodView):
    def get(self):
        try:
            form = MessageForm()

            messages = db.session.query(Message).\
                filter(Message.status == 1
                       , Message.main_id == None).\
                order_by(Message.created_at.desc()).all()
            
            messages_response = db.session.query(Message).\
                filter(Message.status == 1
                       , Message.main_id != None).\
                order_by(Message.created_at.asc()).all()

        except Exception as e:
            traceback.print_exc()
        return render_template("main/index.html", form=form, messages=messages, messages_response=messages_response)
    

    def post(self):
        try:
            request_ip = get_request_ip(request)
            form = MessageForm()
            if not form.validate_on_submit():
                return redirect("main.index")
            
            taiwan_tz = pytz.timezone('Asia/Taipei')
            today = datetime.now(taiwan_tz)
            
            message = Message()
            message.user_ip = request_ip
            message.main_id = form.main_id.data
            message.nickname = form.nickname.data
            message.message = form.message.data
            message.status = 1
            message.created_at = today

            db.session.add(message)
            db.session.commit()

            flash_message = "留言成功" if form.main_id.data is None else "回覆成功"
            flash(flash_message, "success")

        except Exception as e:
            traceback.print_exc()
            db.session.rollback()
            flash_message = "留言失敗" if form.main_id.data is None else "回覆失敗"
            flash(flash_message, "danger")

        return redirect(url_for("main.index"))
        