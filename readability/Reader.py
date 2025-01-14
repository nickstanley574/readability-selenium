from time import sleep
import html2text


class Reader:

  def __init__(self,driver,readability_js=None):
    self.driver = driver


    if (readability_js):
      self.script = readability_js
    else:
      self.script = open("Readability.js").read()

    self.script += """
    var documentClone = document.cloneNode(true);
    var article = new Readability(documentClone).parse();
    return [article.content, article.byline];
    """

  def __del__(self):
    self.driver.quit()

  def get_readable_dict(self,url):
    self.driver.get(url)
    sleep(3)
    script_result = self.driver.execute_script(self.script)
    content = html2text.html2text(script_result[0])
    byline  = html2text.html2text(script_result[1]).rstrip()
    return {'content': content, 'byline':byline}

  def get_readable(self,url):
    return self.get_readable_dict(url)['content']

  get_url = get_readable
