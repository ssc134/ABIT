Atlan Backend Internship Task/Challenge

The dummy data used is in the file ```Plant_Generation_Data.json``` acquired from Kaggle's dataset.
https://www.kaggle.com/anikannal/solar-power-generation-data

```main.py``` is a server written in Flask.

```test.py``` is used to test the server.

The docker image named ```ubuntu_flask_server.tar``` can be found in the folder in the link below.
https://drive.google.com/drive/folders/1v4VZATZYa2JzF6RJ10IVkay1hvCKRWOg?usp=sharing


Guide for setting up the server in Ubuntu 20.4:

1) Loading the Docker image.
    ```bash
    sudo docker load < ubuntu_flask_server.tar
    ```

2) Creating and running the container.
    a) Copy the "IMAGE ID" after executing the below command.
        ```bash
        sudo docker images
        ```
    b) Substitute the copied "IMAGE ID" for <image_id> and port of your choice for <port> in the below command.
        ```bash
        sudo docker run -it -p <port>:5000 <image_id>
        ```
        Now you are into the docker container in interctive mode.
3) Running the server.
    ```bash
    cd ~/src
    python3 main5.py
    ```
4) Now to checking if the server from container port is connected to host port. Open browers and enter the url http://0.0.0.0:<port>, with <port> being the port you used in step 2.b. 
   If the server is running, laoded page will show the message
   ```
   Congratulations! Your server is running.
   ```
5) Now open the file test.py and replace the URI string in line 3 with the URI you entered in the browser.
6) Save and run the test.py file.
    ```bash
    python3 test.py
    ```


    
