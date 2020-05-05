import nltk
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize
from newspaper import Article
nltk.download('all')
from nltk.corpus import stopwords
stop = stopwords.words('english')

def beautiflyFunction(link):
    return BeautifulSoup(link,'html.parser')

def requestFunction(link):
    return requests.get(link)

def nltk_process(document):
    sentences = nltk.sent_tokenize(document)
    #print(sentences)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def find_html(soup,tag,class_name):
    return soup.find_all(tag, class_=class_name)

def ArticalProcc(artical_link):
    word=[]
    artical = Article(artical_link)
    artical.download()
    artical.parse()
    artical.nlp()
    word.append(artical.authors)
    word.append(artical.keywords)
    #print(artical.authors)
    #print(artical.keywords)
    print("AtricalSummery:-")
    print(artical.summary)
    return word

def withoutNews(news_link):
    artical=requestFunction(news_link).text
    artical_soup=beautiflyFunction(artical)
    body = find_html(artical_soup,'div',"css-53u6y8")
    list_paragph=[]
    for i in range(len(body)):
        paragph=body[i].find('p').get_text()
        #print(paragph)
        list_paragph.append(paragph)
        final_artical="".join(list_paragph)
    return nltk_process(final_artical)


def SwacrppingNews():
    main_link="https://www.nytimes.com/"
    #requests.get("https://www.nytimes.com/section/business")
    coverpage=requestFunction(main_link+"section/business").content
    soup1 = beautiflyFunction(coverpage)
    coverpage_news = find_html(soup1,'h2','css-l2vidh e4e4i5l1')
    first_news_link=main_link+coverpage_news[0].find('a')['href']
    return ArticalProcc(first_news_link)






