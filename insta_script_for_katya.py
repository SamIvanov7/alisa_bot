import json


def load_json_file(file_name):
    """Загружает файл JSON и возвращает его данные."""
    try:
        with open(file_name, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Ошибка: файл {file_name} не найден")
    except Exception as e:
        print(f"Ошибка: {e}")


def get_followers_list(data_followers):
    """Извлекает значения "value" и "href" из словаря "string_list_data" каждого элемента в data_followers
    и возвращает список подписчиков."""
    followers = [
        [item["string_list_data"][0]["value"], item["string_list_data"][0]["href"]]
        for item in data_followers
    ]
    return followers


def get_following_list(data_following):
    """Извлекает значения "value" и "href" из словаря "string_list_data" каждого элемента в "relationships_following"
    в data_following и возвращает список подписок."""
    following = [
        [item["string_list_data"][0]["value"], item["string_list_data"][0]["href"]]
        for item in data_following["relationships_following"]
    ]
    return following


def find_common_items(list1, list2):
    """Находит общие элементы в list1 и list2 и возвращает их."""
    common = [item for item in list1 if item in list2]
    return common


def remove_common_items(list1, list2):
    """Удаляет общие элементы из list1 и list2 и возвращает обновленный list1."""
    result = [item for item in list1 if item not in list2]
    return result


def write_list_to_file(file_name, lst):
    """Записывает список в текстовый файл."""
    try:
        with open(file_name, "w") as f:
            for item in lst:
                f.write(f"{item}\n")
    except Exception as e:
        print(f"Ошибка: {e}")


# просим юзера ввести названия файлов
followers_file_name = input("Enter the name of the followers JSON file: ")
following_file_name = input("Enter the name of the following JSON file: ")

# загружаем файлы в скрипт
data_followers = load_json_file(followers_file_name)
data_following = load_json_file(following_file_name)

if data_followers and data_following:
    # получаем списки фоловеров и фоловингов
    followers = get_followers_list(data_followers)
    following = get_following_list(data_following)

    # получаем разницу этих списков
common_followers = find_common_items(followers, following)
print(f"There are {len(common_followers)} common followers: {common_followers}")

# удаляем разницу из фоловингов тем самым получаем список гребней
updated_following = remove_common_items(following, common_followers)

# записываем список гребней в файл
following_file_output = "grebni.txt"
write_list_to_file(following_file_output, updated_following)
print(f"{len(updated_following)} grebnei have been written to {following_file_output}.")
