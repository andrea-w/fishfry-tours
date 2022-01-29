import strawberry
from enum import Enum

@strawberry.enum
class StatusEnum(Enum):
    DOCKED = 'Docked'
    OUTBOUND_TO_SEA = 'Outbound to Sea'
    INBOUND_TO_HARBOUR = 'Inbound to Harbour'
    MAINTENANCE = 'Maintenance'

@strawberry.input
class AddBoatInput:
    name: str = strawberry.field(description="The name of the boat")
    status: StatusEnum = strawberry.field(description="The current status of the boat")

@strawberry.type
class Boat:
    name: str
    status: StatusEnum

@strawberry.type
class Query:
    @strawberry.field(name="boats")
    async def boat(self) -> Boat:
        return Boat(name='Boaty McBoatFace', status=StatusEnum.DOCKED)

@strawberry.type(description="Standard CRUD operations for boats")
class BoatOps:
    @strawberry.mutation
    async def add_boat(self, boat: AddBoatInput) -> Boat:
        ...

    @strawberry.mutation
    async def delete_boat(self, id: int) -> bool:
        ...

    @strawberry.mutation
    async def update_boat_status(self, id: int, status: StatusEnum):
        ...

@strawberry.type
class Mutation:
    boats: BoatOps

    @strawberry.field(name="boats")
    def _boats_resolver(self) -> BoatOps:
        return BoatOps()

schema = strawberry.Schema(query = Query, mutation = Mutation)