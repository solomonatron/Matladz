import twitter
import sys

# Import API keys
with open('keys') as f:
	lines = f.readlines()

# Check key length
if (len(lines) != 4):
	print(len(lines))
	sys.exit(1)

# Check stdin and args - can accept tweet as arguments or though pipe
if (len(sys.argv) > 1):
	# Create the tweet
	tweet = ' '.join(sys.argv[1:])
else:
	# Might break if stdin is empty
	stdin = sys.stdin.read()
	if (len(stdin) > 0):
		tweet = stdin.strip()
	else:
		sys.exit(1)

#print(tweet)

# Authenticate using the keys in the "keys" file
# 1st - Consumer Key (API key)
# 2nd - Consumer Secret (API secret)
# 3rd - Access Token
# 4th - Access Token Secret
api = twitter.Api(consumer_key=lines[0].strip(), consumer_secret=lines[1].strip(), access_token_key=lines[2].strip(), access_token_secret=lines[3].strip())

#print(api.VerifyCredentials())

status = api.PostUpdate(tweet)

#print(status)
