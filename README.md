# Chime-Song-Request

**App Name:** Chime Song Request

**App Tagline:** short one-liner description of your app


**Link(s) to any other public GitHub repo(s) of your app.** If you have one repo for iOS and one for Backend, please link to your backend repo in your iOS README, and your iOS repo in your backend README:

**iOS:** https://github.com/Jonghyun-Chung/ChimeSongRequest-iOS-

**Backend:** https://github.com/franklindtx/Chime-Song-Request-Backend


**Some screenshots of your app (highlight important features):**

![image1](https://raw.githubusercontent.com/franklindtx/Chime-Song-Request-Backend/master/image1.png)
![image2](https://raw.githubusercontent.com/franklindtx/Chime-Song-Request-Backend/master/image2.png)
![image3](https://raw.githubusercontent.com/franklindtx/Chime-Song-Request-Backend/master/image3.png)
![image4](https://raw.githubusercontent.com/franklindtx/Chime-Song-Request-Backend/master/image4.png)

1. We have added a Log-in feature to the app in order to make users put their own song requests by using their names. However, the process is completely anonymous so even if the user logged in with their names, other users are not able to see who requested which songs.

2. After logging in to the app, users can choose either to request songs with the button “Request a Song” in the main screen or to see which songs are requested on the board by tapping the button “View Requested Songs”. 

3. In the “Request a Song” screen, users can type a song name, a reason why they want the song to be played, and details of the song (like a version of the song they want to be played). In the text fields, upon each time users tap on the text box, the placeholder disappears and users can type their own words inside each box. If users do not type anything inside the box and move to the next textbox, the placeholder would reappear. After entering all the fields, they can tap the “Submit Request” button to submit the request and the app will go back to the main screen if the request was successful. 
![image5](https://raw.githubusercontent.com/franklindtx/Chime-Song-Request-Backend/master/image5.png)

4. We definitely integrated our app with its API. After a user logs in to the app by using the log-in feature of the app on the very first screen (by entering his/her name and tapping the “Log In” button,) the app automatically creates a new user object and saves it in the server with his/her name as shown above. Also, when the user inputs the details of the song that he/she wants to be played in “Request a Song” screen, the app automatically creates a song object and saves it in the User object that the user has previously created.



**A short description of your app (its purpose and features):**
It is well known that Cornell students can request songs that they want Chimemasters to play in specific time periods (like Monday at 5:30 to 5:35 or so). However, since many students do not know about how to request songs that they want to be played, we tried making this app in order to make the requesting process easier and more convenient. 
Students are limited to requesting only one song per a day that they must request a week beforehand and three songs to be played per day: one for the song that gets the most votes from other students and two based on the selection of Chimemasters after reading song requests with their reasons why they want that song.


**A list of how your app addresses each of the requirements (iOS / Backend):**


**iOS:**

1. We implemented AutoLayout by using NSLayoutConstraint in every screen of the app in accordance with the design that our designer has done. 
2. We used UITableView in the “Request Detail” screen, showing the list of songs that users have requested.
3. We used many UINavigationControllers to navigate between each screen. For instance, we used NavigationControllers to move between the main screen and the “Request a Song” screen and “Requested Songs” screen. 
4. We definitely integrated our app with its API. After a user logs in to the app by using the log-in feature of the app on the very first screen (by entering his/her name and tapping the “Log In” button,) the app automatically creates a new user object and saves it in the server with his/her name. 

**Backend:**

The backend satisfies the API and database modeling requirement by creating a user-song (one to many) relationship, and multiple routes to create users, get users, create songs, get songs, vote for a song, delete a song, etc. It satisfies the deployment requirement by creating an external IP 35.190.159.80. 

