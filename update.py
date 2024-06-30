import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

images_folder = 'feed'
# index_file = './index.html'

def resize_image(input_path, output_path, width=1024):
    """Resizes the image to the specified width while maintaining aspect ratio."""
    with Image.open(input_path) as img:
        aspect_ratio = img.height / img.width
        new_height = int(width * aspect_ratio)
        img = img.resize((width, new_height), Image.ANTIALIAS)
        img.save(output_path)

def process_images(images_folder, thumbnails_folder, width=1024):
    """Processes images: resizes them if necessary and cleans up thumbnails folder."""
    # Ensure the thumbnails folder exists
    if not os.path.exists(thumbnails_folder):
        os.makedirs(thumbnails_folder)

    # Get the list of files in the images and thumbnails folders
    images = {f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))}
    thumbnails = {f for f in os.listdir(thumbnails_folder) if os.path.isfile(os.path.join(thumbnails_folder, f))}

    # Process each image in the images folder
    for image_file in images:
        image_path = os.path.join(images_folder, image_file)
        thumbnail_path = os.path.join(thumbnails_folder, image_file)

        if image_file not in thumbnails:
            # Resize and save the image as a thumbnail
            resize_image(image_path, thumbnail_path, width)
        else:
            print(f"Thumbnail for '{image_file}' already exists, skipping...")

    # Remove thumbnails that do not have corresponding images
    for thumbnail_file in thumbnails:
        if thumbnail_file not in images:
            os.remove(os.path.join(thumbnails_folder, thumbnail_file))
            print(f"Removed orphan thumbnail '{thumbnail_file}'")

# if __name__ == "__main__":
# images_folder = "path/to/your/images/folder"
# thumbnails_folder = "path/to/your/thumbnails/folder"

# process_images(images_folder, thumbnails_folder)



def get_exif_date(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == 'DateTimeOriginal':
                    return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        print(f"Error getting EXIF date for {image_path}: {e}")
    return None

def update_file(images_folder, index_file):
    image_files = [f for f in os.listdir(images_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]

    image_files_with_dates = []
    for image_file in image_files:
        image_path = os.path.join(images_folder, image_file)
        exif_date = get_exif_date(image_path)
        if exif_date is None:
            exif_date = datetime.fromtimestamp(os.path.getctime(image_path))
        image_files_with_dates.append((image_file, exif_date))

    sorted_image_files = sorted(image_files_with_dates, key=lambda x: x[1], reverse=True)

    image_html = ""
    for image_file, creation_time in sorted_image_files:
        img_src = os.path.join(images_folder, image_file)
        filename = os.path.splitext(image_file)[0].replace('-', ' ')
        formatted_date = creation_time.strftime('%m/%d/%y')
        image_html += f'<a href="./feed/{image_file}"><img class="feed-image" src="./thumbnails/{image_file}"></a>\n<p class="feed-text">[{formatted_date}]</p>\n'


    with open(index_file, 'r') as file:
        html_content = file.read()

    start_marker = '<div id="image-container">'
    end_marker = '</div>'
    start_index = html_content.find(start_marker)
    end_index = html_content.find(end_marker, start_index)

    if start_index != -1 and end_index != -1:
        new_html_content = html_content[:start_index + len(start_marker)] + '\n' + image_html + html_content[end_index:]
    else:
        new_html_content = html_content.replace(
            '</body>',
            f'<div id="image-container">\n{image_html}</div>\n</body>'
        )

    with open(index_file, 'w') as file:
        file.write(new_html_content)

    print(f"{index_file} has been updated successfully.")


process_images('./feed', './thumbnails')

update_file(images_folder, './index.html')
update_file(images_folder, './feed.html')









# import os
# from datetime import datetime

# images_folder = 'feed'
# index_file = './index.html'

# def update_file(images_folder, index_file):
#     image_files = sorted(
#         [f for f in os.listdir(images_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))],
#         key=lambda x: os.path.getctime(os.path.join(images_folder, x)),
#         reverse=True
#     )

#     image_html = ""
#     for image_file in image_files:
#         img_src = os.path.join(images_folder, image_file)
#         filename = os.path.splitext(image_file)[0].replace('-', ' ')
#         creation_time = datetime.fromtimestamp(os.path.getctime(os.path.join(images_folder, image_file)))
#         formatted_date = creation_time.strftime('%m/%d/%y')
#         image_html += f'<img class="feed-image" src="{img_src}">\n<p class="feed-text">{image_file}</p>\n'

#     with open(index_file, 'r') as file:
#         html_content = file.read()

#     start_marker = '<div id="image-container">'
#     end_marker = '</div>'
#     start_index = html_content.find(start_marker)
#     end_index = html_content.find(end_marker, start_index)

#     if start_index != -1 and end_index != -1:
#         new_html_content = html_content[:start_index + len(start_marker)] + '\n' + image_html + html_content[end_index:]
#     else:
#         new_html_content = html_content.replace(
#             '</body>',
#             f'<div id="image-container">\n{image_html}</div>\n</body>'
#         )

#     with open(index_file, 'w') as file:
#         file.write(new_html_content)

#     print(f"{index_file} has been updated successfully.")

# update_file('feed', './index.html')
# update_file('feed', './feed.html')
