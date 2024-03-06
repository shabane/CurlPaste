# Curl Paste

this project is a no-bullshit FileBin server.
you can curl your file to it with just one command.
this file support POST file under a specific username which this let you
access and get all the file under that username with just one command.

> i deployed this site on [octocat](https://octocat.ir/)

### How to use

- HTTP POST files with random URL

    `curl -F file=@yourfile.png octocat.ir`

- If you want your file to view just once

    `curl -F once=@yourfile.png octocat.ir`

- You can also send file by an username which the user can get all files at once

    `curl -F username=@yourfile.png octocat.ir`

- To password protect your files append the password in http query

    `curl -F username=@yourfile.zip octocat.ir/?password=yourPassword`

    - To list all the files under a specific username
    
        `curl octocat.ir/username`
        
    - Or using wget
    
        `wget octocat/username -qO -`
        
    - To download them just pipe them to wget
    
        `curl octocat.ir/username | wget -i -`
        
    - Or
    
        `wget localhost:8000/username -qO - | wget -i -`

    - To get password protected files
        `wget localhost:8000/username/?password=yourPassword -qO - | wget -i -`

### Deployment

to deploy simple just run the **docker image**

```bash
sudo docker run -p 80:80 mshabane/curlpaste:1.1.0
```


> Note that the server will listen from all sources(0.0.0.0)