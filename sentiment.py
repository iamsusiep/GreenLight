from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def sentimentAnalysis():#fileName):
    myfile = open("sample.txt", "r")#'uploads/' + fileName
    text = myfile.read()
    client = language.LanguageServiceClient()
    # if isinstance(text, six.binary_type):
    # text = text.decode('utf-8')
    # document = language.types.Document(
    #     content ='Google, headquartered in Mountain View, unveiled the '
    #              'new Android phone at the Consumer Electronic Show.  '
    #              'Sundar Pichai said in his keynote that users love '
    #              'their new Android phones.',
    #     language = 'en',
    #     type = 'PLAIN_TEXT',
    # )
    document = types.Document(
           content=text,
           type=enums.Document.Type.PLAIN_TEXT)

    # Detects sentiment in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    sentiment = client.analyze_sentiment(document).document_sentiment
    print('Score: {}'.format(sentiment.score))
    print('Magnitude: {}'.format(sentiment.magnitude))

sentimentAnalysis()