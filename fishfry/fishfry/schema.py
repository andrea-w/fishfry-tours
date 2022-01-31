import typing
import strawberry
from enum import Enum
import logging
from sqlalchemy.future import select

from fishfry import sqlamodels

logger = logging.getLogger("fishfry")

strawberry.type(sqlamodels.Boat)

@strawberry.enum
class StatusEnum(Enum):
    DOCKED = 'Docked'
    OUTBOUND_TO_SEA = 'Outbound to Sea'
    INBOUND_TO_HARBOUR = 'Inbound to Harbour'
    MAINTENANCE = 'Maintenance'

@strawberry.type
class Boat:
    name: str
    status: StatusEnum

@strawberry.type
class Query:
    boats: typing.List[sqlamodels.Boat]

    @strawberry.field(name="boats")
    async def _boats_resolver(self) -> typing.List[sqlamodels.Boat]:
        async with sqlamodels.atomic_session() as session:
            items = (await session.execute(select(sqlamodels.Boat))).scalars()
        boats = typing.cast(typing.List[sqlamodels.Boat], items)
        return boats

@strawberry.type(description="Standard CRUD operations for boats")
class BoatOps:
    @strawberry.mutation
    async def add_boat(self, name: str) -> sqlamodels.Boat:
        boat = sqlamodels.Boat(name=name, status=StatusEnum.DOCKED.value)
        async with sqlamodels.atomic_session() as session:
            session.add(boat)
        return boat

    @strawberry.mutation
    async def update_boat_status(self, id: int, status: StatusEnum) -> typing.Optional[sqlamodels.Boat]:
        async with sqlamodels.atomic_session() as session:
            item = (await session.execute(select(sqlamodels.Boat).where(sqlamodels.Boat.id == id))).scalars().first()
            boat = typing.cast(typing.Optional[sqlamodels.Boat], item)

            if boat is None:
                return None

            boat.status = status.value
        return boat

    @strawberry.mutation
    async def delete_boat(self, id: int) -> bool:
        async with sqlamodels.atomic_session() as session:
            item = (await session.execute(select(sqlamodels.Boat).where(sqlamodels.Boat.id == id))).scalars().first()
            boat = typing.cast(typing.Optional[sqlamodels.Boat], item)

            if boat is None:
                return False
            await session.delete(boat)
        return True

@strawberry.type
class Mutation:
    boats: BoatOps

    @strawberry.field(name="boats")
    def _boats_resolver(self) -> BoatOps:
        return BoatOps()


schema = strawberry.Schema(query = Query, mutation = Mutation)