import requests
from bs4 import BeautifulSoup

print('''
                              .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
        _
     /\                        (_)
    /  \   _ __  ___  __ _ _ __ _
   / /\ \ | '_ \/ __|/ _` | '__| |
  / ____ \| | | \__ \ (_| | |  | |
 /_/    \_\_| |_|___/\__,_|_|  |_|
 
   Author : AnsariHacker07
   github : https://github.com/AnsariHacker07
   Instagram : hacker_ansari_07  ''')

# Prompt the user to enter the Instagram username
username = input('Enter the Instagram username: ')

# Send a GET request to the Instagram profile page
response = requests.get(f'https://www.instagram.com/{username}/')

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the profile picture URL
    profile_pic_url = soup.find('meta', attrs={'property': 'og:image'})['content']

    # Send a GET request to the profile picture URL
    profile_pic_response = requests.get(profile_pic_url)

    # Save the profile picture to a file
    with open('/storage/emulated/0/profile_pic.jpg', 'wb') as file:
        file.write(profile_pic_response.content)

    print('Profile picture saved to /storage/emulated/0/profile_pic.jpg')

else:
    print('Failed to download the profile picture.')
    print(f'Error: {response.status_code}')
      
