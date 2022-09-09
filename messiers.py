import json
import random
import time
import os
import logging
from dict2xml import dict2xml
import yaml
import json2table

logging.basicConfig(filename='log.log', level=logging.DEBUG)


def get(object="missing", format="json"):
    print(format)
    format = format.lower()
    if object == "all":
      with open("./data/messier.json", "r") as f:
          data = json.load(f)
          if "json" in format:
              return data
          elif "xml" in format:
              print("dict2xml starting")
              xml_data = dict2xml(data, wrap='root', indent="   ")
              print(xml_data)
              return xml_data
          elif format == "yaml":
              return yaml.dump(data, allow_unicode=True)
          elif format == "html" or "visual":
              html_data = json2table.convert(
                  data,
                  build_direction="LEFT_TO_RIGHT",
                  table_attributes={"border": "1"})

              print(html_data)
              return html_data
    try:
        print(object)
        object = int(object)
        print(object)
    except ValueError:
        return {"success": "false", "name": "Must be integer!"}

    print("get")
    print(f"object is {object}")
    if object == "missing":
        return {
            "success": "false",
            "name":
            "object cannot be None! Please specify the object you want..."
        }
    
    else:
        if int(object) > 110:
            return {
                "success": "false",
                "name": "Messier only found 110 objects! You are over 110!"
            }
        elif int(object) <= 0:
            return {"success": "false", "name": "Object cannot be 0 or below!"}
    
        else:
            object = f"M{object}"
            print(object)

            with open("./data/messier.json", "r") as f:
                data = json.load(f)
                data = data[object]

                if "json" in format:
                    return data
    
                elif format == "xml":
                    xml_data = dict2xml(data, wrap='root', indent="   ")
                    print(xml_data)
                    return xml_data
                elif format == "yaml":
                    return yaml.dump(data, allow_unicode=True)
                elif format == "html" or "visual":
                    html_data = json2table.convert(
                        data,
                        build_direction="LEFT_TO_RIGHT",
                        table_attributes={"border": "1"})
    
                    print(html_data)
                    return html_data
  
