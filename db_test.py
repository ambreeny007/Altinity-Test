from testflows.core import Scenario, Given, When, Then
from clickhouse_driver import Client

with Scenario('Test Database'):
    with Given("I got connected to DB"):
        client = Client('localhost')
    with When("I Execute the query"):
        result = client.execute('SELECT 1')
    with Then("I see query result"):
        assert len(result) == 1
