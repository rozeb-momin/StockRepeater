import sys
import tweepy

# authorization tokens
consumer_key = "re38SBE6Fw1Nz9u8GtoZ5qwFC"
consumer_secret = "SmfOUi2cFBEBF49Ql8N4pgPF8NXh9AxtGlZf8ukqpC5IOCPDgd"
access_key = "176690424-Fgs5QZ4eqRWYtB0DJJrz8zIAfchbkPZhjVpwCPVU"
access_secret = "HF9UNg5T6uebWUqpvmU2JL42IozaiH20LRJWhql9xajPZ"

## Scalper Bots User IDs & Usernames
large_caps_scalper_id, large_caps_username = '1379234944652697600', 'r_scalp'
small_caps_scalper_id, small_caps_username = '1388217130709962753', 'SwingBot_Small'

# Testing News IDs
reuters_username, reuters_id = 'Reuters', '1652541'

# Personal IDs
rozeb_id = '176690424'

testing_id, testing_username = reuters_id, reuters_username

# StreamListener class inherits from tweepy.StreamListener and overrides on_status/on_error methods.
class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.user.screen_name == testing_username:
            text = str(status.text)
            print(text)
            with open("out.txt", "w", encoding='utf-8') as f:
                f.write(f"{status.str_id + ' : ' + text}\n")
        else:
            print(status.user.screen_name)
    # def on_status(self, status):
    #
    #
    #     # if "retweeted_status" attribute exists, flag this tweet as a retweet.
    #     is_retweet = hasattr(status, "retweeted_status")
    #     is_quote = hasattr(status, "quoted_status")
    #
    #     if not is_retweet and not is_quote:
    #
    #         # check if text has been truncated
    #         if hasattr(status,"extended_tweet"):
    #             text = status.extended_tweet["full_text"]
    #         else:
    #             text = status.text
    #
    #         #Filter out noise
    #         # filter_condition = f'@{small_caps_username}' or f'@{large_caps_username}'
    #         filter_condition = f'@{reuters_username}'
    #         if filter_condition in text:
    #             text = 'Noisy Tweet'
    #         else:
    #             text = text
    #         # print(status.id_str + ' ' + text)
    #
    #         # with open("out.csv", "a", encoding='utf-8') as f:
    #         #     f.write("%s,%s,%s,%s,%s,%s\n" % (status.created_at,status.user.screen_name,text))


    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()

if __name__ == "__main__":
    # complete authorization and initialize API endpoint
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # # initialize stream
    streamListener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended')
    # with open("out.csv", "w", encoding='utf-8') as f:
    #     f.write("date,user,text\n")
    stream.filter(follow=[testing_id])
