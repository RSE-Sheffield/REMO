import os
from remo.cawsr.json_to_xml_files import *

def test_json_to_xml():
    converter = XMLToFiles()
    input_file = "src/tests/example_scenario.json"
    output_dir = "test_output/test_json_to_xml"
    
    if not os.path.isdir(output_dir):
      os.makedirs(output_dir)

    converter.parse_scenario(input_file, output_dir)