import json 

def translate_types_to_pandas(dictionary:dict) -> dict:
    dictionary_copy = dictionary.copy()
    for key, value in dictionary_copy.items():
        if value == "integer":
            dictionary_copy[key] = "int"
        if value == "timestamp":
            dictionary_copy[key] = "datetime64[ns]"            
    return dictionary_copy

def join_with_columns_origin(types_mapping:dict, list_columns_origin:list=None) -> dict:

    if list_columns_origin is None:
        return types_mapping
    
    types_mapping_with_columns_origin = {}
    
    for column_type_origin in list_columns_origin:
        if column_type_origin[0] not in types_mapping:
            types_mapping_with_columns_origin[column_type_origin[0]] = column_type_origin[1]
        else:
            types_mapping_with_columns_origin[column_type_origin[0]] = types_mapping[column_type_origin[0]]

    return types_mapping_with_columns_origin

def load_mapping_types(filename:str, list_columns_origin:list=None,is_translate_to_pandas:bool=True) -> dict:
    types_mapping_file = open(filename) 
    types_mapping_dict = json.load(types_mapping_file)
    types_mapping_with_columns_origin_dict = join_with_columns_origin(types_mapping_dict, list_columns_origin)
    
    if is_translate_to_pandas:
        return translate_types_to_pandas(types_mapping_with_columns_origin_dict)
    
    return types_mapping_with_columns_origin_dict

if __name__ == "__main__":
    print(load_mapping_types("/config/types_mapping.json"))
    print(load_mapping_types("/config/types_mapping.json", is_translate_to_pandas=False))
    print(load_mapping_types("/config/types_mapping.json", [('name','string')],False))
    print(load_mapping_types("/config/types_mapping.json", [('name','string'),('create_date','string')],False))