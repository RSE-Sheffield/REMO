import json

class RemoEncounterData:
    def __init__(self):
        self.entity_id = None
        self.entity_type = None
        self.distance_to_entity = 0.0
        
    def to_dictionary(self):
        return {
            "entity_id" : self.entity_id,
            "entity_type" : self.entity_type,
            "distance_to_entity" : self.distance_to_entity
        }

class RemoMetadata:
    def __init__(self):
        self.scenario_file = None
        self.ego_id = None
        self.ads_name = None
        self.replay_file = "default-replay-file.log"
        self.encounters = {} 

    def to_dictionary(self):
        as_dictionary = {
            "scenario_file" : self.scenario_file,
            "ego_id" : self.ego_id,
            "ads_name" : self.ads_name,
            "replay_file" : self.replay_file,
            "encounters" : {k: map(lambda e: e.to_dictionary, v) for k, v in self.encounters.items()}
        }
        
class RemoMetadataWriter:
    def __init__(self, metadata, filepath):
        self.metadata = metadata
        self.filepath = filepath
        
    def write(self):
        print("Attempting to write metadata file to " + str(self.filepath))
        with open(self.filepath, 'w') as file:
            json.dump(self.metadata.to_dictionary(), file, ensure_ascii=False, indent=4)

class RemoMetadataReader:
    def __init__(self, filepath):
        self.metadata_filepath = filepath

    def read_file(self):
        metadata = RemoMetadata()
        
        with open(self.metadata_filepathfilepath, 'r') as file:
            data = json.load(file)
            metadata.scenario_file = data['scenario_file']
            metadata.ego_id = int(data['ego_id'])
            metadata.ads_name = data['ads_name']         
            metadata.replay_file = data['replay_file']
            return metadata

        raise RuntimeError("Failed to read metadata file")
        