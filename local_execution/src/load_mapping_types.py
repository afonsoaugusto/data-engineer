import json 

def translate_types_to_pandas(dictionary:dict) -> dict:
    dictionary_copy = dictionary.copy()
    for key, value in dictionary_copy.items():
        if value == "integer":
            dictionary_copy[key] = "int"
        if value == "timestamp":
            dictionary_copy[key] = "datetime64"            
    return dictionary_copy

def load_mapping_types(filename:str) -> dict:
    types_mapping_file = open(filename) 
    types_mapping_dict = json.load(types_mapping_file)
    return translate_types_to_pandas(types_mapping_dict)

if __name__ == "__main__":
    print(load_mapping_types("/config/types_mapping.json"))