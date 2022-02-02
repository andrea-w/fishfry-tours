import asyncio

from hypercorn.asyncio import serve
from hypercorn.config import Config as HypercornConfig
from quart import Quart
from quart_cors import cors

from fishfry import base
import os
from fishfry.schema import schema
from fishfry.strawview import GraphQLView

app = Quart("fishfry")
app = cors(app, allow_origin="*")
app.config.from_object(base.config)

app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql_view", schema=schema))


@app.route('/')
async def index():
    return 'Welcome to Fishfry Tours. Please see <a href="/graphql">Graph<em>i</em>QL</a> to interact with the GraphQL endpoint.'

def hypercorn_serve():
    hypercorn_config = HypercornConfig()
    hypercorn_config.bind = ["0.0.0.0:{}".format(os.environ.get('PORT'))]    
    hypercorn_config.use_reloader = True
    asyncio.run(serve(app, hypercorn_config, shutdown_trigger=lambda: asyncio.Future()))


if __name__ == '__main__':
    hypercorn_serve()