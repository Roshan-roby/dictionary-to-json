import json
dictionarty = {
            "result":[
                {
                    "name":"Roshan",
                    "current learning":"python",
                    "emotion":"happy"
                },
                {
                    "name":"vishal",
                    "current learning":"python",
                    "emotion":"happy"
                },
                {
                    "name":"sneha",
                    "current learning":"html",
                    "emotion":"happy"
                }
            ]
        }
json_object = json.dumps(dictionarty) 
print(json_object)
