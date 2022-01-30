import asyncio

from quart import Quart

from hypercorn.asyncio import serve
from hypercorn.config import Config
from quart import Quart
from strawberry import Schema

from fishfry.schema import Query, schema
from fishfry.strawview import GraphQLView

app = Quart("fishfry")

app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql_view", schema=schema))


@app.route('/')
async def index():
    return 'Welcome to Fishfry Tours. Please see <a href="/graphql">Graph<em>i</em>QL</a> to interact with the GraphQL endpoint.'

def hypercorn_serve():
    config = Config()
    config.bind = ["0.0.0.0:5000"]    
    config.use_reloader = True
    asyncio.run(serve(app, config, shutdown_trigger=lambda: asyncio.Future()))


if __name__ == '__main__':
    hypercorn_serve()