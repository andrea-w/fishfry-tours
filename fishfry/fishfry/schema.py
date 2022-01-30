import strawberry
import json
from enum import Enum
from typing import Any, List
import logging

logger = logging.getLogger("fishfry")


@strawberry.enum
class StatusEnum(Enum):
    DOCKED = 'Docked'
    OUTBOUND_TO_SEA = 'Outbound to Sea'
    INBOUND_TO_HARBOUR = 'Inbound to Harbour'
    MAINTENANCE = 'Maintenance'

@strawberry.input
class AddBoatInput:
    name: str = strawberry.field(description="The name of the boat")

@strawberry.type
class Boat:
    name: str
    status: StatusEnum

@strawberry.type
class Query:
    @strawberry.field(name="boats")
    async def boat(self, name: str) -> Boat:
        return get_boat_by_name(name)

    @strawberry.field(name="boats")
    async def boats(self) -> List[Boat]:
        return get_all_boats()

@strawberry.type(description="Standard CRUD operations for boats")
class Mutation:
    @strawberry.mutation
    async def add_boat(self, name: str) -> Boat:
        return add_boat(name)

    @strawberry.mutation
    async def update_boat_status(self, name: str, status: StatusEnum) -> bool:
        return update_boat_by_name(name, status)


schema = strawberry.Schema(query = Query, mutation = Mutation)

# -------------------------------- HELPERS --------------------------------------
def get_all_boats() -> List[Boat]:
    with open("/home/andrea/Documents/fishfry-tours/fishfry/fishfry/data.json", 'r') as json_file:
        data = json.load(json_file)
        boats_list = []
        for boat in data['boats']:
            boats_list.append(Boat(name=boat['name'], status=StatusEnum[boat['status']]))
    
    return boats_list

def get_boat_by_name(name: str) -> Boat:
    with open("/home/andrea/Documents/fishfry-tours/fishfry/fishfry/data.json", 'r') as json_file:
        data = json.load(json_file)
        for boat in data['boats']:
            if boat.name == name:
                return Boat(name=boat.name, status=boat.status)

    return None

def add_boat(name: str) -> Boat:
    new_boat = Boat(name=name, status=StatusEnum.DOCKED)
    with open("/home/andrea/Documents/fishfry-tours/fishfry/fishfry/data.json", 'w+') as json_file:
        json_file.write(json.dumps(new_boat))
        logger.info('Added boat {} with status {}'.format(new_boat.name, new_boat.status))
        return new_boat


def update_boat_by_name(name: str, status: StatusEnum) -> bool:
    boats_list = get_all_boats()
    logger.info(boats_list)
    found = False
    for boat in boats_list:
        if boat.name == name:
            boat.status = status
            found = True
            break
    if found:
        with open("/home/andrea/Documents/fishfry-tours/fishfry/fishfry/data.json", 'w') as json_file:
           json_file.write(json.dumps(boats_list))
           logger.info('Updated boat {} to {}'.format(name, status))
           return True
    logger.warn('Could not find boat {} in datastore. Update unsuccessful'.format(name))
    return False