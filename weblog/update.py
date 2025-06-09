import os
from datetime import datetime

def get_image_creation_date(file_path: str) -> str:
    creation_time = os.path.getctime(file_path)
    creation_date = datetime.fromtimestamp(creation_time)
    formatted_date = creation_date.strftime("[%b '%y]")
    return formatted_date

def formatted_current_date():
    now = datetime.now()
    formatted_date = f"[{now.month}-{now.day}-{now.year}]"
    return formatted_date

def remove_dummy_file():
    dir_name = "weblog/inbox"
    file_name = "foo.txt"
    file_path = os.path.join(dir_name, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_name}' removed.")
    else:
        print(f"File '{file_name}' does not exist in the '{dir_name}' directory.")

remove_dummy_file()


def convert_txt_to_html(file_path):
    file_path = os.path.join("weblog", file_path)
    if not file_path.endswith('.txt'):
        print("Error: Please provide a .txt file.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]

        if not lines:
            print("Error: File is empty or contains only whitespace.")
            return

        title = lines[0]
        sub_title = lines[1]
        paragraphs = lines[2:]

        html_content = f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Blog Haikus</title>
    <link rel="stylesheet" href="./css/dectionary.css">

    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{sub_title}">
    <meta property="og:image" content="./typing.gif">
    <meta property="og:type" content="website">

</head>
<body style="max-width: 700px;">
""" + f"""
    <b>{title}</b>
    <i>{sub_title}</i>
"""

        for para in paragraphs:
            html_content += f"    <p>{para}</p>\n"

        date = datetime.now().strftime("%m/%d/%Y")
        date_string = f"""<p>[{date}]</p>"""
        # html_content += date_string

        html_content += "</body>\n</html>"

        html_file_path = file_path.replace('.txt', '.html')

        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        os.remove(file_path)
        print(f"Converted and deleted: {file_path} → {html_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def _old_convert_txt_to_html(file_path):
    file_path = os.path.join("weblog", file_path)
    if not file_path.endswith('.txt'):
        print("Error: Please provide a .txt file.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]

        if not lines:
            print("Error: File is empty or contains only whitespace.")
            return

        title = lines[0]
        paragraphs = lines[1:]

        html_content = """<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Blog Haikus</title>
    <style>
        body {
            max-width: 700px;
        }
    </style>
</head>
<body style="max-width: 700px;">
    <!-- <a href="#" onclick="goBack()">/back</a> -->
    <a href="../index.html">/tombetthauser</a> <a href="./index.html">/weblog</a>
""" + f"""
    <h2>{title}</h2>
"""

        for para in paragraphs:
            html_content += f"    <p>{para}</p>\n"

        date = datetime.now().strftime("%m/%d/%Y")
        date_string = f"""
    <p>[{date}]</p>
"""

        html_content += date_string
        html_content += "</body>\n</html>"

        html_file_path = file_path.replace('.txt', '.html')

        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        os.remove(file_path)
        print(f"Converted and deleted: {file_path} → {html_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def process_text_files(inbox_dir='weblog/inbox', target_dir='weblog', record_file='weblog/record.txt', text_file='weblog/text.txt'):
    file_extensions = ['.txt']

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    if os.path.exists(record_file):
        with open(record_file, 'r') as record:
            recorded_filenames = set(line.strip() for line in record)
    else:
        recorded_filenames = set()

    inbox_files = os.listdir(inbox_dir)
    print(f"Files in inbox: {inbox_files}")

    def get_unique_filename(filepath):
        directory, original_filename = os.path.split(filepath)
        name, ext = os.path.splitext(original_filename)
        counter = 1
        while os.path.exists(filepath):
            new_name = f"{counter}_{name}{ext}"
            filepath = os.path.join(directory, new_name)
            counter += 1
        return filepath

    for filename in inbox_files:
        file_ext = os.path.splitext(filename)[1].lower()

        if file_ext in file_extensions:
            source = os.path.join(inbox_dir, filename)
            destination = os.path.join(target_dir, filename)

            if os.path.exists(destination):
                destination = get_unique_filename(destination)
                print(f"File already exists, renaming to {os.path.basename(destination)}")

            print(f"Copying {filename} from {source} to {destination}")
            with open(source, 'rb') as src_file:
                with open(destination, 'wb') as dst_file:
                    while True:
                        chunk = src_file.read(1024)
                        if not chunk:
                            break
                        dst_file.write(chunk)
            print(f"Copied: {filename} as {os.path.basename(destination)}")

            if os.path.exists(record_file):
                with open(record_file, 'r') as record:
                    existing_content = record.readlines()
            else:
                existing_content = []

            new_filename = os.path.basename(destination) + '\n'
            with open(record_file, 'w') as record:
                record.write(os.path.splitext(new_filename)[0] + '.html\n')
                record.writelines(existing_content)

            os.remove(source)
            print(f"Removed {filename} from {inbox_dir}")

            convert_txt_to_html(filename)

    print("Processing complete. All files copied, removed from inbox, and record updated.")

process_text_files()

def clean_record(blog_files_dir='weblog', record_file='weblog/record.txt'):
    if not os.path.exists(record_file):
        print(f"{record_file} does not exist.")
        return

    blog_files_in_dir = set(os.listdir(blog_files_dir))

    with open(record_file, 'r') as record:
        lines = record.readlines()

    print('\n\n')
    print(blog_files_in_dir)
    print('\n')
    print(lines)
    print('\n\n')

    new_lines = [line for line in lines if line.strip() in blog_files_in_dir]

    with open(record_file, 'w') as record:
        record.writelines(new_lines)

    print("Record file cleaned. Any missing files were removed from the record.")

clean_record()

def update_feed_from_record(record_file='weblog/record.txt', feed_file='weblog/index.html', text_file='weblog/text.txt'):
    if not os.path.exists(record_file):
        print(f"{record_file} does not exist.")
        return

    if not os.path.exists(feed_file):
        print(f"{feed_file} does not exist.")
        return

    with open(record_file, 'r') as record:
        record_lines = record.readlines()

    record_lines = [line.strip() for line in record_lines]

    blog_html_link_lines = []

    for idx, line in enumerate(record_lines):
        print(line)
        img_date = formatted_current_date()
        print(img_date)

        filename = line.strip()

        new_line_str = f"<li><a href=\"{filename}\">{filename}</a></li>\n"
        blog_html_link_lines.append(new_line_str)

    with open(feed_file, 'r') as feed:
        feed_content = feed.readlines()

    start_index = None
    end_index = None

    for i, line in enumerate(feed_content):
        if "start tag" in line:
            start_index = i
        elif "end tag" in line:
            end_index = i
            break

    if start_index is None or end_index is None:
        print(f"Could not find 'start tag' or 'end tag' in {feed_file}.")
        return

    updated_content = (
        feed_content[:start_index + 1] +
        blog_html_link_lines +
        feed_content[end_index:]
    )

    with open(feed_file, 'w') as feed:
        feed.writelines(updated_content)

    print(f"Feed file {feed_file} updated successfully.")

update_feed_from_record()

def create_inbox_with_dummy_file():
    dir_name = "weblog/inbox"
    file_name = "foo.txt"
    file_content = "bar"

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"Directory '{dir_name}' created.")
    else:
        print(f"Directory '{dir_name}' already exists.")

    file_path = os.path.join(dir_name, file_name)

    with open(file_path, "w") as file:
        file.write(file_content)
        print(f"File '{file_name}' created with content: {file_content}")

create_inbox_with_dummy_file()
