""" Handles configuration options for recording scenarios """

class RemoRecordingConfig:
    def __init__(self):
        self.metadata_filepath = "default-metadata-path.json"
        self.replay_file = "default-replay-file.log"
        self.recording_time = 20.0
