import webcolors
from colorthief import ColorThief
import os
from os import walk

def getDominantColor(image_path):
    """
    extracts dominant color from image in RGB format using ColorThief
    converts color in RGB format to color in english (precise)
    associate color with larger group (ex: palegreen --> green)

    """

    color_thief = ColorThief(image_path)

    dominant_color = color_thief.get_color(quality=1)

    def closest_color(requested_color):
        min_colors = {}
        for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - requested_color[0]) ** 2
            gd = (g_c - requested_color[1]) ** 2
            bd = (b_c - requested_color[2]) ** 2
            min_colors[(rd + gd + bd)] = name
        return min_colors[min(min_colors.keys())]

    def get_color_name(rgb_color):
        try:
            closest_name = actual_name = webcolors.rgb_to_name(rgb_color)
        except ValueError:
            closest_name = closest_color(rgb_color)
            actual_name = None
        return closest_name

    color = get_color_name(dominant_color)

    if color in ('midnightblue', 'navy', 'darkblue', 'mediumblue', 'blue', 'royalblue'
                'steelblue', 'dodgerblue', 'deepskyblue', 'cornflowerblue', 'skyblue',
                'lightskyblue', 'lightsteelblue', 'lightblue', 'powderblue', 'aqua', 'cyan',
                'paleturquoise', 'lightcyan'):
        color = "blue"
    elif color in ('teal', 'darkcyan', 'lightseagreen', 'cadetblue', 'darkturquoise',
                'mediumturquoise', 'turquoise', 'aquamarine', 'darkgreen', 'green',
                'darkolivegreen', 'forestgreen', 'seagreen', 'olive', 'olivedrab',
                'mediumseagreen', 'limegreen', 'lime', 'springgreen', 'mediumspringgreen',
                'darkseagreen', 'mediumaquamarine', 'yellowgreen', 'lawngreen', 'chartreuse',
                'lightgreen', 'greenyellow', 'palegreen'):
        color = "green"
        
    elif color in ('indigo', 'purple', 'darkmagenta', 'darkviolet', 'darkslateblue', 'blueviolet',
                'darkorchid', 'fuschia', 'magenta', 'slateblue', 'mediumslateblue', 'mediumorchid',
                'mediumorchid', 'mediumpurple', 'orchid', 'violet', 'thistle', 'lavender',
                'mediumvioletred'):
        color = 'purple'
    elif color in ('deeppink', 'palevioletred', 'hotpink', 'lightpink', 'pink', 'darkred', 'red',
                'firebrick', 'crimson', 'indianred', 'lightcoral', 'salmon', 'darksalmon', 'lightsalmon',
                'orangered', 'tomato', 'darkorange', 'coral', 'orange', 'mistyrose', 'lavenderblush', 'plum'):
        color = "red"
    elif color in ('darkkhaki', 'gold', 'khaki', 'peachpuff', 'yellow', 'palegoldenrod', 'moccasin',
                'papayawhip', 'lightgoldenrodyellow', 'lemonchiffon', 'lightyellow'):
        color = 'yellow'
    else:
        color = "no color detected"

    return color, dominant_color



# getDominantColor('colordetect/greentext.png')

def main():
    color_dictionary = {}
    filenames = next(walk('Model3/words'), (None, None, []))[2]

    for filename in filenames:
        file_key = os.path.splitext(filename)[0]
        color_name, _ = getDominantColor('Model3/words/' + filename)
        if color_name != "no color detected":
            color_dictionary[file_key] = color_name

    # Function to extract the actual word from the dictionary key
    def get_actual_word(key):
            parts = key.split('_')
            line_number = int(parts[1])
            word_position = int(parts[2])
            
            if 0 <= line_number < len(lines):
                words = lines[line_number].split()
                if 0 <= word_position < len(words):
                    return words[word_position]
            
            return None
    
    # Read the text from the output.txt file
    with open('output.txt', 'r') as file:
        lines = file.read().splitlines()

    # Create a new dictionary with actual words as keys and associated colors as values
    actual_words_dict = {get_actual_word(key): color for key, color in color_dictionary.items()}


    print(actual_words_dict)
    return actual_words_dict


if __name__ == '__main__':
    main()