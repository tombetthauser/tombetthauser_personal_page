import os
from datetime import datetime

def get_image_creation_date(file_path: str) -> str:
    # Get the creation time of the file
    creation_time = os.path.getctime(file_path)
    
    # Convert the creation time to a datetime object
    creation_date = datetime.fromtimestamp(creation_time)
    
    # Format the date as "[Mon 'YY]"
    formatted_date = creation_date.strftime("[%b '%y]")
    
    return formatted_date

# Example usage:
# file_path = 'example_image.jpg'
# formatted_date = get_image_creation_date(file_path)
# print(formatted_date)


def formatted_current_date():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date as desired: [month-day-year]
    formatted_date = f"[{now.month}-{now.day}-{now.year}]"
    
    return formatted_date



def remove_dummy_file():
    # Define the directory and file paths
    dir_name = "inbox"
    file_name = "foo.txt"
    
    # Define the full path for the file
    file_path = os.path.join(dir_name, file_name)
    
    # Check if the file exists, then remove it
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_name}' removed.")
    else:
        print(f"File '{file_name}' does not exist in the '{dir_name}' directory.")

# Call the function
remove_dummy_file()




import os

def process_images(inbox_dir='inbox', images_dir='images', record_file='record.txt', text_file='text.txt'):
    # List of acceptable image file extensions
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif']

    # Create images directory if it doesn't exist
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # Read existing record.txt contents if it exists
    if os.path.exists(record_file):
        with open(record_file, 'r') as record:
            recorded_filenames = set(line.strip() for line in record)
    else:
        recorded_filenames = set()

    # List and print the files in the inbox directory for debugging
    inbox_files = os.listdir(inbox_dir)
    print(f"Files in inbox: {inbox_files}")

    # Function to generate a new filename if it already exists
    def get_unique_filename(filepath):
        directory, original_filename = os.path.split(filepath)
        name, ext = os.path.splitext(original_filename)
        counter = 1
        while os.path.exists(filepath):
            new_name = f"{counter}_{name}{ext}"
            filepath = os.path.join(directory, new_name)
            counter += 1
        return filepath

    # Check for files in the inbox directory
    for filename in inbox_files:
        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()

        # Check if the file is an image or gif
        if file_ext in image_extensions:
            # Define the source and destination paths
            source = os.path.join(inbox_dir, filename)
            destination = os.path.join(images_dir, filename)

            # If file already exists, generate a unique filename
            if os.path.exists(destination):
                destination = get_unique_filename(destination)
                print(f"File already exists, renaming to {os.path.basename(destination)}")

            # Copy the file to the destination
            print(f"Copying {filename} from {source} to {destination}")
            with open(source, 'rb') as src_file:
                with open(destination, 'wb') as dst_file:
                    while True:
                        chunk = src_file.read(1024)  # Read in chunks
                        if not chunk:
                            break
                        dst_file.write(chunk)
            print(f"Copied: {filename} as {os.path.basename(destination)}")

            # Read the existing record file content
            if os.path.exists(record_file):
                with open(record_file, 'r') as record:
                    existing_content = record.readlines()
            else:
                existing_content = []

            # Add the new filename to the top of the record.txt
            new_filename = os.path.basename(destination) + '\n'
            with open(record_file, 'w') as record:
                record.write(new_filename)  # Write new filename first
                record.writelines(existing_content)  # Write the rest of the old content

            with open(text_file, 'w') as record:
                record.write(new_filename)  # Write new filename first
                record.writelines(existing_content)  # Write the rest of the old content

            # Remove the file from the inbox after copying
            os.remove(source)
            print(f"Removed {filename} from {inbox_dir}")

    print("Processing complete. All files copied, removed from inbox, and record updated.")

# Copy inbox images to image folder
process_images()








def clean_record(images_dir='images', record_file='record.txt'):
    # Check if record.txt exists
    if not os.path.exists(record_file):
        print(f"{record_file} does not exist.")
        return

    # Get a list of filenames in the images directory
    images_in_dir = set(os.listdir(images_dir))

    # Read the current contents of record.txt
    with open(record_file, 'r') as record:
        lines = record.readlines()

    # Filter out lines that do not match any filenames in the images directory
    new_lines = [line for line in lines if line.strip() in images_in_dir]

    # Write the updated contents back to record.txt
    with open(record_file, 'w') as record:
        record.writelines(new_lines)

    print("Record file cleaned. Any missing files were removed from the record.")

# Example of using the function
clean_record()




def update_text_file(record_file='record.txt', text_file='text.txt'):
    # Read the lines from the record.txt file
    with open(record_file, 'r') as record_f:
        record_lines = record_f.readlines()
    
    # Read the lines from the text.txt file
    with open(text_file, 'r') as text_f:
        text_lines = text_f.readlines()

    # Get the number of lines in both files
    record_len = len(record_lines)
    text_len = len(text_lines)

    # If record.txt has more lines, copy the corresponding lines from record.txt to text.txt
    if record_len > text_len:
        for i in range(text_len, record_len):
            text_lines.append(record_lines[i])
    # If text.txt has more lines, truncate the excess lines
    elif record_len < text_len:
        text_lines = text_lines[:record_len]

    # Write the updated lines back to text.txt
    with open(text_file, 'w') as text_f:
        text_f.writelines(text_lines)

# Example usage:
# update_text_file('record.txt', 'text.txt')

update_text_file()




def update_feed_from_record(record_file='record.txt', feed_file='feed.html', text_file='text.txt'):
    # Check if record.txt exists
    if not os.path.exists(record_file):
        print(f"{record_file} does not exist.")
        return

    # Check if feed.html (or target file) exists
    if not os.path.exists(feed_file):
        print(f"{feed_file} does not exist.")
        return

    # Read the lines from record.txt
    with open(record_file, 'r') as record:
        record_lines = record.readlines()

    # Read the lines from text.txt
    with open(text_file, 'r') as text:
        text_lines = text.readlines()

    # Wrap each line in quotes and add a comma at the end
    # wrapped_lines = [f'\t\t\t"{line.strip()}",\n' for line in record_lines]
    wrapped_lines = []

    for idx, line in enumerate(record_lines):
        print(line)
        # img_date = get_image_creation_date(f"./images/{line.strip()}")
        img_date = formatted_current_date()
        print(img_date)

        filename = line.strip()

        img_text = text_lines[idx].strip().replace('"', "'")

        # new_line_str = f"\t\t\t{{ filename: `{line.strip()}`, date: `{img_date}` \},\n"
        # formatted_string = f"Here is a string with quotes: \"{value}\" and curly brackets: {{this is a literal curly bracket}}"
        new_line_str = f"\t\t\t {{ filename: \"{filename}\", date: \"{img_date}\", text: \"{img_text}\"}},\n"

        # new_line_str = '\t\t\t{ filename: \'%\', date: \'%\' },\n' % (line.strip(), img_date)
        wrapped_lines.append(new_line_str)

    # Read the feed file
    with open(feed_file, 'r') as feed:
        feed_content = feed.readlines()

    # Find the start and end tag positions
    start_index = None
    end_index = None

    for i, line in enumerate(feed_content):
        if "start tag" in line:
            start_index = i
        elif "end tag" in line:
            end_index = i
            break

    # Ensure both tags are present
    if start_index is None or end_index is None:
        print(f"Could not find 'start tag' or 'end tag' in {feed_file}.")
        return

    # Replace the lines between the start and end tag with the wrapped record lines
    updated_content = (
        feed_content[:start_index + 1] +  # Keep content up to and including "start tag"
        wrapped_lines +                   # Insert the wrapped record lines
        feed_content[end_index:]          # Keep content from "end tag" onward
    )

    # Write the updated content back to the feed file
    with open(feed_file, 'w') as feed:
        feed.writelines(updated_content)

    print(f"Feed file {feed_file} updated successfully.")

# Example of using the function
update_feed_from_record(feed_file='feed.html')
update_feed_from_record(feed_file='index.html')






from PIL import Image
# import os

def create_thumbnails(images_dir='images', thumbnails_dir='thumbnails', thumbnail_width=750):
    # Create the thumbnails directory if it doesn't exist
    if not os.path.exists(thumbnails_dir):
        os.makedirs(thumbnails_dir)

    # Get a set of filenames in the images directory
    image_files = set(os.listdir(images_dir))

    # Loop through each file in the images directory
    for filename in image_files:
        # Get the full paths for image and thumbnail
        image_path = os.path.join(images_dir, filename)
        thumbnail_path = os.path.join(thumbnails_dir, filename)

        # Only create the thumbnail if it doesn't exist
        if not os.path.exists(thumbnail_path):
            try:
                with Image.open(image_path) as img:
                    # Calculate the new height while maintaining the aspect ratio
                    width_percent = (thumbnail_width / float(img.size[0]))
                    thumbnail_height = int((float(img.size[1]) * float(width_percent)))

                    # Resize the image
                    img_resized = img.resize((thumbnail_width, thumbnail_height), Image.Resampling.LANCZOS)

                    # Save the resized image to the thumbnails folder
                    img_resized.save(thumbnail_path)

                    print(f"Thumbnail created for {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # Remove thumbnails that don't have corresponding images
    for thumbnail_file in os.listdir(thumbnails_dir):
        if thumbnail_file not in image_files:
            thumbnail_path = os.path.join(thumbnails_dir, thumbnail_file)
            os.remove(thumbnail_path)
            print(f"Removed orphaned thumbnail: {thumbnail_file}")

    print("Thumbnail generation complete and orphan cleanup done.")

# Example of using the function
create_thumbnails()




# import os

def create_inbox_with_dummy_file():
    # Define the directory and file paths
    dir_name = "inbox"
    file_name = "foo.txt"
    file_content = "bar"
    
    # Check if the directory exists, if not, create it
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"Directory '{dir_name}' created.")
    else:
        print(f"Directory '{dir_name}' already exists.")
    
    # Define the full path for the file
    file_path = os.path.join(dir_name, file_name)
    
    # Create the file and write 'bar' to it
    with open(file_path, "w") as file:
        file.write(file_content)
        print(f"File '{file_name}' created with content: {file_content}")

# Call the function
create_inbox_with_dummy_file()



def get_first_line(input_file):
    with open(input_file, 'r') as file:
        first_line = file.readline().strip()  # Read the first line and strip any surrounding whitespace
    return first_line



def replace_text_between_markers(start_string, end_string, file_to_update, new_text):
    # Read the file content
    with open(file_to_update, 'r') as file:
        lines = file.readlines()

    # Initialize variables
    new_content = []
    in_marker_block = False
    
    # Process the file line by line
    for line in lines:
        if start_string in line:
            # When the start marker is found, add the line and start replacing text
            new_content.append(line)
            new_content.append(new_text + '\n')  # Append the new text
            in_marker_block = True
        elif end_string in line and in_marker_block:
            # When the end marker is found, stop replacing text
            new_content.append(line)
            in_marker_block = False
        elif not in_marker_block:
            # Outside the marker block, just copy the line
            new_content.append(line)

    # Write the modified content back to the file
    with open(file_to_update, 'w') as file:
        file.writelines(new_content)

new_preview_header = f'''\
  <meta property="og:title" content=" ̴̛̬̱͈̃̅͠ ̴̣͙̱͕̥͒́̓t̵̢̺͉͔͛́͗͛̈́ơ̷̗͎m̴͚͍̞͙͑̔b̵̢͇͚̱͚̀͠ȩ̶̡̡͉̭́̾̚͝t̴̼͕̯̭̜͂̐̀̿t̶̛͉̭͍͒̔̽̍ͅh̷̦̟̖̟̀̔a̷̡̺̹̾̇̋̀͆ú̴̜̔͝s̸͈̦͍͓͂e̶͎͎̖̖̔ŕ̸̢͝ ̶̢̛͕͕̇ ̸̧̦̥̇̂͘" />
  <meta property="og:image" content="./thumbnails/{get_first_line('record.txt')}" />\
'''

replace_text_between_markers('<!-- START_PREVIEW_HEADER -->', '<!-- END_PREVIEW_HEADER -->', 'index.html', new_preview_header)


new_preview_header = f'''\
    <meta property="og:title" content="Tom's Social Media Feed" />
    <meta property="og:image" content="./thumbnails/{get_first_line('record.txt')}" />\
'''

replace_text_between_markers('<!-- START_PREVIEW_HEADER -->', '<!-- END_PREVIEW_HEADER -->', 'feed.html', new_preview_header)
