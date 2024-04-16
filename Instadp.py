import os
from instaloader import Instaloader, Profile


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


# Initialize Instaloader
L = Instaloader()

# Prompt the user for the Instagram username
profile_name = input("Enter the Instagram username: ")

# Specify the download location
download_location = "/storage/emulated/0/"
os.chdir(download_location)

# Download profile picture
profile = Profile.from_username(L.context, profile_name)
L.download_profile(profile, profile_pic_only=True)

print("Profile picture downloaded to", os.getcwd())
