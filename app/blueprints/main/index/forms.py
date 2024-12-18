from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class MessageForm(FlaskForm):
    main_id = IntegerField("主留言編號")
    nickname = StringField("暱稱", validators=[DataRequired(), Length(1, 64)])
    message = TextAreaField("留言")
    submit = SubmitField("發表留言")
