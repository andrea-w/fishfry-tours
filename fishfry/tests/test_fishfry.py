import logging
from fishfry import __version__, webapp, schema
import pytest
import pytest_asyncio

def test_version():
    assert __version__ == '0.1.0'

class TestViews:
    async def test_index(self):
        assert "Welcome" in (await webapp.index())

@pytest.mark.asyncio
@pytest.mark.usefixtures("empty_db")
class TestGraphQuery:
    # Helper function to create new boat with specified name
    async def _create(self, name: str, shouldNotBeNone: bool = True):
        result = await schema.schema.execute('mutation { boats { addBoat(name: \"%s\") { id } } }' % name)
        if shouldNotBeNone:
            assert result.data is not None
            assert "id" in result.data['boats']['addBoat']
            newid = result.data['boats']['addBoat']['id']
            return newid
        else:
            assert result.data is None
            return result

    # Helper function to delete boat with specified id
    async def _delete(self, id: int) -> bool:
        result = await schema.schema.execute('mutation { boats { deleteBoat(id: %s) } }' % id)
        assert result.data is not None
        return result.data['boats']['deleteBoat']

    # Helper function to fetch all boats in database
    async def _fetch_all(self):
        result = await schema.schema.execute('query { boats { id name status } }')
        assert result.data is not None
        return result
    
    # Create 1 new boat, then delete it
    async def test_create_delete(self):
        newid = await self._create('Test Boat')
        result = await schema.schema.execute("mutation { boats { deleteBoat(id: %s) } }" % newid)
        assert result.data is not None
        assert result.data['boats']['deleteBoat'] == True

    # Create 1 new boat, then update its status
    async def test_create_update(self):
        newid = await self._create('Test Boat')
        result = await schema.schema.execute("mutation { boats { updateBoatStatus(id: %s, status: MAINTENANCE) { id status } } }" % newid)
        assert result.data is not None
        assert result.data['boats']['updateBoatStatus']['id'] == newid
        assert result.data['boats']['updateBoatStatus']['status'] == "Maintenance"
        delete_success = await self._delete(newid)
        assert delete_success == True

    # Try to create 2 new boats that have the same name - second boat should fail to create
    async def test_duplicate_create(self):
        newid = await self._create('Test Boat')
        result = await self._create('Test Boat', False)
        assert result.data is None
        assert 'asyncpg.exceptions.UniqueViolationError' in result.errors[0].message
        delete_success = await self._delete(newid)
        assert delete_success == True

    # Try to update a boat with an invalid status - should return error message
    async def test_update_invalid_status(self):
        newid = await self._create('Test Boat')
        result = await schema.schema.execute("mutation { boats { updateBoatStatus(id: %s, status: STOLEN) { id status} } }" % newid)
        assert result.data is None
        assert 'Value \'STOLEN\' does not exist in \'StatusEnum\' enum' in result.errors[0].message
        delete_success = await self._delete(newid)
        assert delete_success == True

    # Create 3 new boats in database, fetch all boats and make sure the 3 are returned
    async def test_fetch_boats(self):
        id_1 = await self._create('Test Boat 1')
        id_2 = await self._create('Test Boat 2')
        id_3 = await self._create('Test Boat 3')
        result = await self._fetch_all()
        assert result.data is not None
        assert len(result.data['boats']) == 3
        assert result.data['boats'][0]['id'] == id_1
        assert result.data['boats'][1]['id'] == id_2
        assert result.data['boats'][2]['id'] == id_3
        delete_1 = await self._delete(id_1)
        delete_2 = await self._delete(id_2)
        delete_3 = await self._delete(id_3)
        assert delete_1 == True
        assert delete_2 == True
        assert delete_3 == True