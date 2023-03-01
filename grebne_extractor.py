import json


def load_json_file(file_name):
    """Loads a JSON file and returns the data."""
    try:
        with open(file_name, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Error: {file_name} not found")
    except Exception as e:
        print(f"Error: {e}")


def get_followers_list(data_followers):
    """Extracts the "value" and "href" values from the "string_list_data"
    dictionary of each item in data_followers and returns a list of followers."""
    followers = [
        [item["string_list_data"][0]["value"], item["string_list_data"][0]["href"]]
        for item in data_followers
    ]
    return followers


def get_following_list(data_following):
    """Extracts the "value" and "href" values from the "string_list_data"
    dictionary of each item in data_following["relationships_following"]
    and returns a list of following."""
    following = [
        [item["string_list_data"][0]["value"], item["string_list_data"][0]["href"]]
        for item in data_following["relationships_following"]
    ]
    return following


def find_common_items(list1, list2):
    """Finds the common items in list1 and list2 and returns them."""
    common = [item for item in list1 if item in list2]
    return common


def remove_common_items(list1, list2):
    """Removes the common items in list1 and list2 and returns the updated list1."""
    result = [item for item in list1 if item not in list2]
    return result


def write_list_to_file(file_name, lst):
    """Writes a list to a text file."""
    try:
        with open(file_name, "w") as f:
            for item in lst:
                f.write(f"{item}\n")
    except Exception as e:
        print(f"Error: {e}")


def process_files(followers_path, following_path):
    # Load the JSON files
    with open(followers_path, "r") as f:
        data_followers = json.load(f)
    with open(following_path, "r") as f:
        data_following = json.load(f)

    # Extract the followers and following lists
    followers = get_followers_list(data_followers)
    following = get_following_list(data_following)

    # Find the common followers and remove them from the following list
    common_followers = find_common_items(followers, following)
    updated_following = remove_common_items(following, common_followers)

    # Write the updated following list to a file
    following_output_path = "grebni.txt"
    write_list_to_file(following_output_path, updated_following)

    # Return a message indicating success and the path to the output file
    message = (
        f"{len(updated_following)} гребней записано в файл {following_output_path}."
    )
    return message
