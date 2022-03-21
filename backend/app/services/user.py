
from app.models.user import User

class User():
    def read_all():
        people = User.query.all()
        # Serialize the data for the response
        #person_schema = PersonSchema(many=True)
        #data = person_schema.dump(people)
        return people