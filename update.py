import os
from datetime import datetime

# Define the path to the images folder and the index.html file
images_folder = 'feed'
index_file = './index.html'

def update_file(images_folder, index_file):
    # Get a list of image files in the folder, sorted by modification time in reverse order
    image_files = sorted(
        [f for f in os.listdir(images_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))],
        key=lambda x: os.path.getmtime(os.path.join(images_folder, x)),
        reverse=True
    )

    # Generate the HTML content for the images
    image_html = ""
    for image_file in image_files:
        img_src = os.path.join(images_folder, image_file)
        filename = os.path.splitext(image_file)[0].replace('-', ' ')
        creation_time = datetime.fromtimestamp(os.path.getmtime(os.path.join(images_folder, image_file)))
        # formatted_date = creation_time.strftime('%Y-%m-%d %H:%M:%S')
        formatted_date = creation_time.strftime('%m/%d/%y')
        # image_html += f'<img class="feed-image" src="{img_src}">\n<p class="feed-text">{img_src} [{formatted_date}]</p>\n'
        # image_html += f'<img class="feed-image" src="{img_src}">\n<p class="feed-text"><span class="heart-emoji">♥️</span> {image_file}</p>\n'
        image_html += f'<img class="feed-image" src="{img_src}">\n<p class="feed-text">{image_file}</p>\n'

    # Read the existing index.html file
    with open(index_file, 'r') as file:
        html_content = file.read()

    # Find the start and end of the image container div
    start_marker = '<div id="image-container">'
    end_marker = '</div>'
    start_index = html_content.find(start_marker)
    end_index = html_content.find(end_marker, start_index)

    # If the div is found, replace its content; otherwise, create a new div
    if start_index != -1 and end_index != -1:
        new_html_content = html_content[:start_index + len(start_marker)] + '\n' + image_html + html_content[end_index:]
    else:
        new_html_content = html_content.replace(
            '</body>',
            f'<div id="image-container">\n{image_html}</div>\n</body>'
        )

    # Write the updated HTML content back to the index.html file
    with open(index_file, 'w') as file:
        file.write(new_html_content)

    print("index.html has been updated successfully.")

update_file('feed', './index.html')
update_file('feed', './feed.html')
