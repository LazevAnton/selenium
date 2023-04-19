from service import SocialNetworkScraper

if __name__ == '__main__':
    service = SocialNetworkScraper()
    title = 'This post created by selenium'
    content = 'Selenium is an open source automation testing tool that supports a number of scripting languages' \
              ' like Python, C#, Java, Perl, Ruby, JavaScript, etc. depending on the application to be tested.' \
              ' One can choose the script accordingly'
    service.create_post(title,content)
    print('Done')
