from app.extensions import db


class Message(db.Model):
    """
    留言資料表
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="序號")
    user_ip = db.Column(db.String(64), nullable=True, comment="留言者IP")
    main_id = db.Column(db.Integer, nullable=True, comment="主留言ID，空值為主留言")
    nickname = db.Column(db.String(64), nullable=False, comment="留言者暱稱")
    message = db.Column(db.Text, nullable=False, comment="留言內容")
    status = db.Column(db.Integer, nullable=False, default=1, comment="留言狀態 0: 待審核 1: 可見")
    created_at = db.Column(db.DateTime, nullable=False, comment="留言時間")
