
from remo.remo_metadata import *

def test_encounterdata_to_dictionary():
    data = RemoEncounterData()
    data.entity_id = 23
    data.entity_type = "default"
    data.distance_to_entity = 24.0

    expected_output = {
        "entity_id": 23,
        "entity_type": "default",
        "distance_to_entity": 24.0,
        "name": None
    }
    
    assert data.to_dictionary() == expected_output
    
def test_remo_metadata_to_dictionary():
    data = RemoEncounterData()
    data.entity_id = 23
    data.entity_type = "default"
    data.distance_to_entity = 24.0
    
    metadata = RemoMetadata()
    metadata.scenario_file = "default_scenario_file.json"
    metadata.ego_id = 4
    metadata.ads_name = "test_ads"
    metadata.replay_file = "replay_file.json"
    metadata.encounters = {
        0 : [data]
    }
    
    expected_output = {
        "scenario_file": "default_scenario_file.json",
        "ego_id": 4,
        "ads_name": "test_ads",
        "replay_file": "replay_file.json",
        "encounters": {
            0 : [{
                "entity_id": 23,
                "entity_type": "default",
                "distance_to_entity": 24.0
            }]
        }
    }
    
    assert metadata.to_dictionary() == expected_output

    
def test_metadata_reader():
    data = RemoEncounterData()
    data.entity_id = 23
    data.entity_type = 8
    data.distance_to_entity = 24.0
    
    metadata = RemoMetadata()
    metadata.scenario_file = "default_scenario_file.json"
    metadata.ego_id = 4
    metadata.ads_name = "test_ads"
    metadata.replay_file = "replay_file.json"
    metadata.encounters = {
        0 : [data]
    }
    
    metadata_path = "test_metadata.json"
    writer = RemoMetadataWriter(metadata, metadata_path)
    writer.write()
    
    reader = RemoMetadataReader(metadata_path)
    new_metadata = reader.read()

    assert metadata.to_dictionary() == new_metadata.to_dictionary()