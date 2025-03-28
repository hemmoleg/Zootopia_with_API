import json
import data_fetcher

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def load_html(file_path):
    with open(file_path, "r") as handle:
        return handle.read()


def get_skin_types(animal_data):
    skin_type = set()
    for animal_obj in animal_data:
        if 'characteristics' in animal_obj and 'skin_type' in animal_obj['characteristics']:
            skin_type.add(animal_obj['characteristics']['skin_type'])

    return skin_type


def create_animal_data_html(animal_data, skin_type):
    animal_data_string = ""

    for animal_obj in animal_data:
        if (
            'characteristics' in animal_obj
            and 'skin_type' in animal_obj['characteristics']
            and animal_obj['characteristics']['skin_type'] == skin_type
        ):
            animal_data_string += serialize_animal(animal_obj)

    return animal_data_string


def serialize_animal(animal_obj):
    animal_data_string=""
    animal_data_string += "<li class='cards__item'>"
    animal_data_string += f"<div class='card__title'>Name: {animal_obj['name']}</div>"
    animal_data_string += "<div class='card__text'><ul>"

    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        animal_data_string += f"<li><strong>Diet:</strong> {animal_obj['characteristics']['diet']}</li>"

    animal_data_string += f"<li><strong>Locations:</strong> {animal_obj['locations'][0]}</li>"

    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        animal_data_string += f"<li><strong>Type:</strong> {animal_obj['characteristics']['type']}</li>"

    if 'characteristics' in animal_obj and 'group_behavior' in animal_obj['characteristics']:
        animal_data_string += f"<li><strong>Group behavior:</strong> {animal_obj['characteristics']['group_behavior']}</li>"

    if 'characteristics' in animal_obj and 'top_speed' in animal_obj['characteristics']:
        animal_data_string += f"<li><strong>Top speed:</strong> {animal_obj['characteristics']['top_speed']}</li>"

    if 'characteristics' in animal_obj and 'skin_type' in animal_obj['characteristics']:
        animal_data_string += f"<li><strong>Skin type:</strong> {animal_obj['characteristics']['skin_type']}</li>"

    animal_data_string += "</ul></div></li>\n"
    return animal_data_string


def get_skin_type_from_user(skin_types):
    print("Please select a skin type. Only animals with the skin type will be present in the html file.")
    print("Animals with no skin type attribute will not be present in the html.")

    while True:
        i = 1
        for skin_type in skin_types:
            print(f"{i}. {skin_type}")
            i += 1

        try:
            selected_skin_type = int(
                input("Please enter a number for the skin type you wish to be present in the html file: "))
            break
        except ValueError:
            print("Please enter an integer value")

    return selected_skin_type


def write_html(html):
    with open('animal.html', "w") as handle:
        handle.write(html)

    print("Website was successfully generated to the file animal.html")


def main():
    #animal_data = load_data('animals_data.json')

    input_animal = input("Enter a name of an animal: ")
    animal_data = data_fetcher.fetch_data(input_animal)

    skin_types = get_skin_types(animal_data)

    html = load_html('animals_template.html')

    if len(skin_types) > 0:
        skin_type = get_skin_type_from_user(skin_types)
        animal_data_string = create_animal_data_html(animal_data, list(skin_types)[skin_type - 1])
        html = str(html).replace("__REPLACE_ANIMALS_INFO__", animal_data_string)
    else:
        html = str(html).replace("__REPLACE_ANIMALS_INFO__", f"<h2>The animal '{input_animal}' doesn't exist.</h2>")

    write_html(html)


if __name__ == '__main__':
    main()