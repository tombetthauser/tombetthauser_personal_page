import os



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




# import os

def process_images(inbox_dir='inbox', images_dir='images', record_file='record.txt'):
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

    # Check for files in the inbox directory
    for filename in os.listdir(inbox_dir):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()

        # Check if the file is an image or gif
        if file_ext in image_extensions:
            # Define the source and destination paths
            source = os.path.join(inbox_dir, filename)
            destination = os.path.join(images_dir, filename)

            # Copy the file only if it does not already exist in the destination directory
            if not os.path.exists(destination):
                with open(source, 'rb') as src_file:
                    with open(destination, 'wb') as dst_file:
                        while True:
                            chunk = src_file.read(1024)  # Read in chunks
                            if not chunk:
                                break
                            dst_file.write(chunk)
                print(f"Copied: {filename}")

                # Add filename to record.txt if it was copied
                with open(record_file, 'a') as record:
                    record.write(filename + '\n')
            else:
                print(f"Already exists: {filename}")

    print("Processing complete. All files copied where necessary.")


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









def update_feed_from_record(record_file='record.txt', feed_file='feed.html'):
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

    # Wrap each line in quotes and add a comma at the end
    wrapped_lines = [f'\t\t\t"{line.strip()}",\n' for line in record_lines]

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
                    img_resized = img.resize((thumbnail_width, thumbnail_height), Image.ANTIALIAS)

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
