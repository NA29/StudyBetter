import json
import cv2
import matplotlib.pyplot as plt
from path import Path
from htr_pipeline import read_page, DetectorConfig, LineClusteringConfig, ReaderConfig, PrefixTree
import os
# from colordetect.colors import getDominantColor
import shutil
import sys 

sys.path.append('autocorrect')

from autocorrect import autocorrect



# Set up the output directory for the individual word images
output_directory = 'Model3//words'

if os.path.exists(output_directory):
    shutil.rmtree(output_directory)
os.makedirs(output_directory, exist_ok=True)

# Load configurations and word list
with open('Model3//data//config.json') as f:
    sample_config = json.load(f)

with open('Model3//data//words_alpha.txt') as f:
    word_list = [w.strip().upper() for w in f.readlines()]
prefix_tree = PrefixTree(word_list)


with open('output.txt', 'w') as file:
    for img_filename in Path('Model3/data').files('*.PNG'):
        result = ""  # Initialize result string for each image

        # dominant_color = getDominantColor(img_filename)
        # result += f"Dominant Color: {dominant_color}/n"

        

        # read text
        img = cv2.imread(img_filename)
        scale = sample_config.get(img_filename.basename(), {}).get('scale', 1)
        margin = sample_config.get(img_filename.basename(), {}).get('margin', 0)
        read_lines = read_page(img,
                               detector_config=DetectorConfig(scale=scale, margin=margin),
                               line_clustering_config=LineClusteringConfig(min_words_per_line=2),
                               reader_config=ReaderConfig(decoder='word_beam_search', prefix_tree=prefix_tree))

        #autocorrect 
        autocorrected_lines = []

        # output text to file and accumulate in `result`
        for read_line in read_lines:
            line_text = ' '.join(read_word.text for read_word in read_line) + '\n'
        
            # Autocorrect the line_text using the autocorrect function
            autocorrected_line = autocorrect(line_text)
            
            # Append the autocorrected line to the list
            autocorrected_lines.append(autocorrected_line)

        with open('output.txt', 'w') as file:
            # Write the autocorrected lines to the file
            for autocorrected_line in autocorrected_lines:
                file.write(autocorrected_line)

            file.write('\n')

     
        


        # Save individual word images
        for i, read_line in enumerate(read_lines):
            for j, read_word in enumerate(read_line):
                aabb = read_word.aabb
                word_image = img[aabb.ymin:aabb.ymax, aabb.xmin:aabb.xmax]
                word_filename = os.path.join(output_directory, f'word_{i}_{j}.png')
                cv2.imwrite(word_filename, word_image)

        # Print results for the current image after processing with the decoder
        print(result)

        #plot
       
        plt.figure(f'Image: {img_filename}', dpi=150)

        img_height, img_width = img.shape[:2]
        
        for i, read_line in enumerate(read_lines):
            for read_word in read_line:
                aabb = read_word.aabb
                xs = [aabb.xmin, aabb.xmin, aabb.xmax, aabb.xmax, aabb.xmin]
                ys = [aabb.ymin, aabb.ymax, aabb.ymax, aabb.ymin, aabb.ymin]
                plt.plot(xs, ys, c='r' if i % 2 else 'b')
                plt.text(aabb.xmin, aabb.ymin - 2, read_word.text)
                plt.imshow(img, cmap='gray')
                plt.axis('off')  # Turn off axis
                plt.axis('image')  # Ensure aspect ratio is the same as the image
                plt.xlim([0, img_width])
                plt.ylim([img_height, 0])
                
plt.show()