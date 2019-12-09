# Chime-Song-Request

App Name: Chime Song Request

App Tagline: short one-liner description of your app
 


Link(s) to any other public GitHub repo(s) of your app. If you have one repo for iOS and one for Backend, please link to your backend repo in your iOS README, and your iOS repo in your backend README.

iOS: https://github.com/Jonghyun-Chung/ChimeSongRequest-iOS-

Backend:https://github.com/franklindtx/Chime-Song-Request-Backend


Some screenshots of your app (highlight important features)

![alt test](screenshots/picturename)
A short description of your app (its purpose and features)
It is well known that Cornell students can request songs that they want Chimemasters to play in specific time periods (like Monday at 5:30 to 5:35 or so). However, since many students do not know about how to request songs that they want to be played, we tried making this app in order to make the requesting process easier and more convenient. 

Students are limited to requesting only one song per a day that they must request a week beforehand and three songs to be played per day: one for the song that gets the most votes from other students and two based on the selection of Chimemasters after reading song requests with their reasons why they want that song.

A list of how your app addresses each of the requirements (iOS / Backend)

The backend satisfies the API and database modeling requirement by creating a user-song (one to many) relationship, and multiple routes to create users, get users, create songs, get songs, vote for a song, delete a song, etc. It satisfies the deployment requirement by creating an external IP 35.190.159.80. 

