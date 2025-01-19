



import requests
from lxml import html

#access to html document in the forum:"https://support.mozilla.org/en-US/questions/firefox?show=all"
url = "https://support.mozilla.org/en-US/questions/firefox?show=all"


response = requests.get(url)

if response.status_code == 200:
    html_content = response.text



# parsing an HTML document (provided as a string) into a tree structure
tree = html.fromstring(html_content)

#the xpaths that i found for the elements in the task
my_xpaths = [
    ".//a[contains(text(), 'Get Help')]",
    ".//input[@placeholder='Search Support']",
    "(.//article[contains(@class, 'forum--question-item')])[1]",
    ".//article[contains(@class, 'forum--question-item')][position() <= 5]",
    "//article[contains(@class, 'forum--question-item')][.//li[@class='thread-solved']]",
    "//article[contains(@class, 'forum--question-item')][.//p[contains(text(), '1 day ago')]]",
    ".//article[contains(@class, 'forum--question-item')]//p[contains(@class, 'user-meta-asked-by')]//text()[contains(., '1 day ago')]/ancestor::article",
    "//article[contains(@class, 'forum--question-item')][.//h2[contains(@class, 'forum--question-item-heading')]/a[contains(text(), '?')]]",
    "//article[contains(@class, 'forum--question-item')][.//p[contains(@class, 'user-meta-asked-by')]/strong/a[starts-with(translate(text(), 'd', 'D'), 'D')]]",
    "//article[contains(@class, 'forum--question-item')][.//dl[@class='forum--meta-details replies']/li/span[@class='forum--meta-val' and number(.) > 2]]",
    "//article[contains(@class, 'forum--question-item')][.//h2[@class='forum--question-item-heading']/a[starts-with(translate(., 'P', 'p'), 'p')]]",
    "//article[contains(@class, 'forum--question-item')][.//h2[@class='forum--question-item-heading']/a[string-length(normalize-space(.)) >= 14]]",
    "//article[contains(@class, 'forum--question-item')]//li[(@class='tag')]//a[contains(text(),'Windows 11')]/ancestor::article",
]
#mapping every xpath for its element in the html document
for i, xpath in enumerate(my_xpaths, start=1):
    results = tree.xpath(xpath)
    print(f"\n(#{i}) XPath: {xpath}")
    for result in results:

        print(html.tostring(result, encoding='unicode').strip())
