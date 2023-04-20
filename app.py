import config
from service import SocialNetworkScraper

if __name__ == '__main__':
    service = SocialNetworkScraper()
    title = 'Post created after selenium register user'
    content = 'Beautiful Soup is a library that makes it easy to scrape information from web pages. ' \
              'It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying' \
              ' the parse tree.'
    username = config.SOCIAL_NETWORK_REGISTER_USER
    password = config.SOCIAL_NETWORK_REGISTER_PASSWORD
    email = config.SOCIAL_NETWORK_REGISTER_EMAIL
    service.social_network_register(username,password,email)
    service.create_post(title, content)
    # print('Done')
