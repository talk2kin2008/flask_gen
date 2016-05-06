
def getTemplate(className='User',tableName='users'):
    '''return template to create User model
        className: User
        tableName: users
    '''

    s = '''
from sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin

class {className}(UserMixin, db.Model):
    __tablename__={tableName}
    id = db.column(db.Integer, primary_key=True)
    username= db.column(db.String(64), unique=True, index=True)
    email = db.column(db.String(64), unique=True, index=True)
    password_hash = db.column(dbString(128))
    role_id = db.column(db.Integer, db.ForeignKey('roles.id'))
'''.format(className=className,tableName=tableName)

    return s
    
    