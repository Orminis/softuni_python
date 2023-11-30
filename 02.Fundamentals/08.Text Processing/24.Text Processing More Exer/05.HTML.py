"""
You will receive 3 lines of input. On the first line you will receive a title of an article.
On the next line you will receive the content of that article.
On the next n lines until you receive "end of comments" you will get the comments about the article.
Print the whole information in html format.
The title should be in "h1" tag (<h1></h1>);
the content in article tag (<article></article>); each comment should be in div tag (<div></div>).
For more clarification see the example below"""
"""
Example:
    Input:
        SoftUni Article
        Some content of the SoftUni article
        some comment
        more comment
        last comment
        end of comments
    Output:
        <h1>
            SoftUni Article
        </h1>
        <article>
            Some content of the SoftUni article
        </article>
        <div>
            some comment
        </div>
        <div>
            more comment
        </div>
        <div>
            last comment
</div>
"""
article_title = input()
article_context = input()

comments_list = []
comments = input()

while not comments == "end of comments":
    comments_list.append(comments)

    comments = input()

print(f"<h1>\n{' '*4}{article_title}\n</h1>")
print(f"<article>\n{' '*4}{article_context}\n</article>")
for comment in comments_list:
    print(f"<div>\n{' '*4}{comment}\n</div>")