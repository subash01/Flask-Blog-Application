import os

class Config:
	SECRET_KEY='30e67d95a5791a1a3bdbe8db69d5de9f'
	SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
	MAIL_SERVER='smtp.googlemail.com'
	MAIL_PORT=587
	MAIL_USE_TLS=True
	MAIL_USERNAME=os.environ.get('EMAIL_USER')
	MAIL_PASSWORD=os.environ.get('EMAIL_PASS')
