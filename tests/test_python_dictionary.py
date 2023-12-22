# Make Dictionary
d = dict()

# Add to Dictionary
d.update({"name" : "apple"})
d.update({"color" : "red"})
d.update({"taste" : "tart"})

# Delete from Dictionary
d.pop("color") # removes --> {"color" : "red"}

# Read from Dictionary
d.get("name") # returns --> "apple"
d.get("name", "default_value_if_key_not_found") # default value is optional

# Iterate through Dictionary
for key, value in d.items():
    # do something with key or value
    pass

# Check if item exists in Dictionary
if key in d:
    # do something with key or value
    pass

# Update/Modify Dictionary Value
d["name"] = "banana"