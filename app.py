# pip install -r requirements.txt
import graphene
from flask import Flask
from flask_graphql import GraphQLView


from db.database import db_session, connection_url
# from gql.mutation import Mutation
from gql.query import Query

app = Flask(__name__)
app.debug = True

app.config["SQLALCHEMY_DATABASE_URI"] = connection_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


schema = graphene.Schema(query=Query,
                         # mutation=Mutation
                         )

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5001,
            debug=True
            )


# כדי להריץ:
# in the terminal
# docker compose down
# למחוק את כל מה שקיים כרגע בקודר דסקטופ:

# docker compose build
# docker compose up
# לגשת:
# http://127.0.0.1:5001/graphql
# לא משנה בפוסטמן או בדפדפן
# כדי לכבות:
# docker compose down


# אחרי שהכל רץ, טוענים את ה data
# לפתוח טרמינל חדש
# להריץ את הפקודה:
# docker-compose exec api bash
# ואז להריץ בפנים את הפקודה:
# python load_data.py



