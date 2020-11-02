from flask_mongoengine import MongoEngine


class db():
    def init(app):
        db = MongoEngine(app)


class Something(db.Document):
    some = db.StringField()


inserted = Something(some='whatever').save()

print(inserted)
for obj in Something.objects:
    print(obj)
