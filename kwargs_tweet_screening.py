#tweet screening

#define a kwargs to handle tweet conditions
def screening(**kwargs):
    username = kwargs['handle']
    post = kwargs['tweet']
    
    #find tweet lenght
    post_len = len(post)
    
    #condition to check if 'Buhari','government','sars' are not in tweet and tweet not more than 140 characters
    if ('Buhari' not in post) and ('sars' not in post) and ('government' not in post) and post_len < 140:
        print(f'''
        {username:}
        {post}
        Character lenght: {post_len}
        Status: Published
        ''')
    else: 
        print(f'''
        {username:}
        {post}
        Character lenght: {post_len}
        Status: Not published
        ''')
    

#collect user handle and tweet for user
user_handle = input('Tweeter handle: ')
user_tweet = input('Write your tweet: \n')

#call function and pass in keywords arguments
screening(handle=user_handle, tweet=user_tweet)
