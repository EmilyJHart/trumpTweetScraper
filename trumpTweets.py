import twint
#import json
#import os

c = twint.Config() #creates object

c.Username = "realDonaldTrump" 

c.Store_json = True 

c.Output = "trumpTweet.json"

twint.run.Search(c) #Searches for @realDonaldTrump's tweets








    
