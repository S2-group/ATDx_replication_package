import json

# Save JSON data into the given filePath
def save(file_path, data):
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4, default=str)

# Iterates over all entries of 'json_file', groups them by 'key', and saves each group into a separate JSON file in the 'target_path' folder
def main(json_file, key, target_path):
    json_file = json.load(open(json_file, 'r'))

    grouped_items = {}

    current_index = 1
    total_length = len(json_file)

    for item in json_file.values():
        print('Grouping item ' + str(current_index) + '/' + str(total_length))
        new_key = item[key]
        if(not new_key in grouped_items):
            grouped_items[new_key] = list()
        grouped_items[new_key].append(item)
        current_index += 1

    current_index = 1
    total_length = len(grouped_items)

    for proj_key in grouped_items:
        print('Saving file ' + str(current_index) + '/' + str(total_length))
        save(target_path + proj_key + '.json', grouped_items[proj_key])
        current_index += 1

if __name__ == "__main__":
    main('../data/arch_issues.json', 'project', '../data/jsons/')



