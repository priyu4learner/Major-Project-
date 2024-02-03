import yaml
import json

# Specify the filename of your YAML file
yaml_filename = 'C:/Users/HP/OneDrive - MNNIT Allahabad, Prayagraj, India/Desktop/rnn_bot/chatbot/my_data/general convo.yml'  # Replace 'your_file_name.yaml' with the actual filename

# Load YAML data from the file
with open(yaml_filename, 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# Convert to JSON format with intent patterns, responses, and tag
json_data = {
    "intents": [
        {
            "patterns": [conversation[0]],
            "responses": [conversation[1]],
            "tag": yaml_data["categories"]  # You can customize the tag based on the content
        }
        for conversation in yaml_data["conversations"]
    ]
}

# Convert Python dictionary to JSON string
json_string = json.dumps(json_data, indent=2)

# Save JSON data to a file
with open('convo.json', 'w') as json_file:
    json_file.write(json_string)

print("Conversion completed. JSON data saved to 'output.json'.")
