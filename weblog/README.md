# Adding a Blogpost

1. Create a new txt file in the /inbox directory
2. Format it single lines for first the title, then subsequent paragraphs (example below)

```txt
New Blog Post Title

Here's a sample paragraph. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. 

Here's a second sample paragraph. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. 

Here's a third sample paragraph. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum.
```

3. After you add this commit and the weblog/update.py should run, you can also run this manually
4. After weblog/update.py runs the new page should appear as an html file in the /weblog root and the post should be added to record.txt
5. If you want to change how the title appears, change it in record.txt and run weblog/update.py again
6. If you want to archive the post move it into weblog/archived_blog_posts/ and run weblog/update.py again
7. if you want to delete it, delete the file from /weblog/ and run /weblog/update.py again