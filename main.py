import requests
import tweepy
import json
import re
from colorama import init, Fore, Back, Style
import time

init(convert=True)

print(f'''{Fore.LIGHTBLUE_EX}                                                                                
                                            /((((((((((((.     *(.              
                (((*                      (((((((((((((((((((((/                
                ((((((.                 *(((((((((((((((((((((((((              
                ((((((((((.             (((((((((((((((((((((((*                
                 ((((((((((((((/        ((((((((((((((((((((((                  
                  ((((((((((((((((((((((((((((((((((((((((((((                  
                (((((((((((((((((((((((((((((((((((((((((((((*                  
                (((((((((((((((((((((((((((((((((((((((((((((                   
                  ((((((((((((((((((((((((((((((((((((((((((                    
                    /((((((((((((((((((((((((((((((((((((((.                    
                   .((((((((((((((((((((((((((((((((((((((                      
                     ((((((((((((((((((((((((((((((((((((                       
                       /(((((((((((((((((((((((((((((((                         
                             ,(((((((((((((((((((((((                           
                         /((((((((((((((((((((((((                              
              ,(((((((((((((((((((((((((((((((*                                 
                   .(((((((((((((((((((((.                                      {Fore.RESET}
''')
print('')
print(f'[{Fore.RED}+{Fore.RESET}] {Fore.RED}lyt1x{Fore.RESET} ♻ {Fore.LIGHTYELLOW_EX}Noahreyli Customs{Fore.RESET}')
print('')
with open('config.json', 'r') as f:
    data = json.load(f)
auth = tweepy.OAuthHandler(data["API_key"], data["API_key_secret"])
auth.set_access_token(data["Access_Token"], data["Access_Token_secret"])
api = tweepy.API(auth, wait_on_rate_limit=True)
tweets = re.compile("(https://t.co/)([a-zA-Z0-9]+)")
invites = re.compile("(discord.gg/|discord.com/invite/)([a-zA-Z0-9]+)")
used = ['fafchx5Y','N5u3MxgF']
usedlinks = ['https://t.co/1hRwyzEGlz']
tweetss = api.user_timeline(screen_name="NoahreyliCustom", include_rts=False, tweet_mode='extended')
while True:
    cursor = tweepy.Cursor(api.user_timeline, id='NoahreyliCustom', tweet_mode='extended').items(1)
    for i in cursor:
        print('')
        print(f'[{Fore.MAGENTA}+{Fore.RESET}] {Fore.MAGENTA}Checking the last tweet...{Fore.RESET}')
        print('')
        if tweets.search(i.full_text):
            if tweets.search(i.full_text).group() not in usedlinks:
                print(i.full_text)
                r = requests.get(tweets.search(i.full_text).group())
                invite = r.url
                if invites.search(invite):
                    code = invites.search(invite).group(2)
                    print(f'    [{Fore.GREEN}+{Fore.RESET}] {Fore.GREEN}Found a code: {Fore.BLUE}{code}{Fore.RESET}')
                    if code not in used:
                        url = f'https://discord.com/api/v9/invites/{code}'
                        headers = {
                            'authority': 'discord.com',
                            'content-length': '0',
                            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS4xMjggU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijg5LjAuNDM4OS4xMjgiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMzNjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                            'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijc4MDIyMjg1MzUwNDk1ODQ5NSIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI3ODc3ODI2MTYyNTM0NjQ1NzYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                            'authorization': data["token"],
                            'accept-language': 'fr',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
                            'accept': '*/*',
                            'origin': 'https://discord.com',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-dest': 'empty',
                            'referer': 'https://discord.com/channels/^@me',
                        }
                        ror = requests.post(url, headers=headers)
                        print(f'        [{Fore.GREEN}+{Fore.RESET}] {Fore.GREEN}Tried to join by a code {Fore.BLUE}{code}{Fore.RESET}{Fore.GREEN}, logs:{Fore.RESET} {ror.text}')
        else:
            print(f'    [{Fore.CYAN}+{Fore.RESET}] {Fore.CYAN}No link in that tweet{Fore.RESET}')
    print('')
    time.sleep(5)