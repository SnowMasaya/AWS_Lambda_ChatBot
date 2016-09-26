AWS_Lambda_ChatBot
====

## Description

This code is the Image search bot for slack.
Image is support to understand the unknown contents.

This code made for the below contest.

https://awschatbot.devpost.com/

### Install

#### Enviroments Setting

If you easy to create the instance , you install the terraform

    https://www.terraform.io/intro/getting-started/install.html

If you easy to set up the enviroments, you install the ansible

    http://docs.ansible.com/ansible/intro_installation.html

You install the MySQL

   https://www.tutorialspoint.com/mysql/mysql-installation.htm

You install the Vagrant

   https://www.vagrantup.com/docs/installation/

If you make the data set fastest, you install the parallel

   https://www.gnu.org/software/parallel/

#### Python Enviroments Setting

Python Versions below

```
Python 3.5.0
```

Python Library install

```
pip install requirements.txt
```

MySQL python wrapper install

GEt the source code latest versions
     http://dev.mysql.com/downloads/connector/python/

Install the mysql for python

```
    cd {your} download directory
    tar xzf mysql-connector-python-VER.tar.gz
    cd mysql-connector-python-VER
    sudo python setup.py install
```

#### Prepare the Data

Prepare the Wikipedia data.

It is possible to get the abstract data and image data below site.

[WikiPedia](https://archive.org/download/enwiki-20080312)<br>

Abstract Data is below

```
enwiki-20080312-abstract.xml
```

Image data is below

```
enwiki-20080312-imagelinks.sql
```

You use the above the sql for make the wikipedia image database.
But the above the sql doesn't work for syntax error.
You have to remove the "TYPE=InnoDB;"

```
1: create database enwiki
2: use enwiki
2: source enwiki-20080312-imagelinks.sql
```

Create folder for the data

```
mkdir -p {your git clone folder}/Data/wiki_image/
```

You set the abstract data above folder

```
mv enwiki-20080312-abstract.xml {your git clone folder}/Data/wiki_image/
```

You exetuce the below command
It take a long time.

```
python execute_wiki_pedia_xml_to_json.py -xml enwiki-20080312-abstract.xml -img True
```

If you already install the parallel command, you execute the below command.
Because the below code is faster than above.
It also take a long time.

```
parallel --linebuffer -j {40-100(you adjustment)} :::: jobs.txt
```

"jobs.txt" is the below

```
python execute_wiki_pedia_xml_to_json.py -xml enwiki-20080312-abstract.xml -img True
```

#
### Usage 
#

#### Local Setting

If you already prepare the json data set, you move the json data the below folder

```
mkdir -p {your git clone folder}/docker/data/wiki_image
mv {your git clone folder}/Data/wiki_image/*.json {your git clone folder}/docker/data/wiki_image
```

You conpress the data

```
gzip {your git clone folder}/docker/data/wiki_image/*.json
```

You have to set the ip address

```
  config.vm.network "private_network", ip: "192.168.33.xx"
```

You run the vagrant

```
vagrant up
```

Docker install process below

https://docs.docker.com/engine/installation/linux/ubuntulinux/

If you use the setting the ansible you execute the below command

```
cd {your git clone folder}/ansible_setting
ansible-playbook -i vagrant_host vagrant_lambda_docker.yml
```

Build the docker image

```
cd /home/vagrant/AWS_Lambda_Chatbot/docker
make test-elasticsearch-english
```

Escape the docker container

```
exit
```

Tag the docker image
Because it is easy to understand the container mean

```
docker tag {docker elasticsearch image} elasticsearch_english
```

You start the elasticsearch container and regist data

```
cd {your git clone folder}/Question_Answer
sh elastic_start_english.sh [PIPE_NUMBER] [PARALLEL_NUMBER] [IMAGE_FLAG (True or False)] [ELS_IMAGE_NAME]
example)
sh elastic_start_english.sh 1 5 True elasticsearch_english
```

You have to push the container your docker hub

```
docker login
docker tag elasticsearch_english:latest {your docker repository name}:{tag name}
docker push {your docker repository name}:{tag name}
```

#### Instance Setting

You create the instance
Amazon Machine Image (AMI): Ubuntu
Choose an Instance Type:t2.micro
Security Groups:you have to open the 9200 port for the elasticsearch

http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html

If you use the terraform, you execute the below command

```
cd {your git clone folder}/terraform
terraform plan
terraform apply
```

Docker enviroment setting

https://docs.docker.com/engine/installation/linux/ubuntulinux/

If you use the setting the ansible you execute the below command
you edit the ip address your instance `aws_lambda_chatbot_host`

```
cd {your git clone folder}/ansible_setting
ansible-playbook -i aws_lambda_chatbot_host aws_lambda_chatbot.yml
```

Access the instance

```
ssh -i {your key} ubuntu@{your ip address}
```

You get the docker image

```
docker login
docker pull {your docker repository name}:{tag name}
```

You get the elasticsearch start command

```
git clone https://github.com/SnowMasaya/AWS_Lambda_ChatBot.git
```

You execute the below command
It is confirm the elasticsearch container is runnning

```
cd {your git clone folder}/Question_Answer
sh elastic_start_english.sh [PIPE_NUMBER] [PARALLEL_NUMBER] [IMAGE_FLAG (True or False)] [ELS_IMAGE_NAME]
example)
sh elastic_start_english.sh 1 5 True elasticsearch_english
```

#
### Lambda Setting
#

If you use the Lambda for slack bot, you read the below link.
I explain the how to use the lambda function for slack bot.

http://qiita.com/GushiSnow/private/0f69cab874aa8ea4a859

#
### Code Directory Structure 
#

```
AWS Lambda Chat Bot Hackthon
  - Question_Answer/　　　　... Question and Answer code
  - slack/　　　　　        ... Lambda function code for slack bot
  - docker/　　　　         ... Setting the container
  - ansible_setting/　　　　... Setting the environment code
  - terraform/　　　　      ... Create the instance
```

#
### Licence
#
```
The MIT License (MIT)

Copyright (c) 2016 Yumi Hamazono

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
#
### Author
#
[SnowMasaya](https://github.com/SnowMasaya)
### References 
#
>[AWS_Lambda_ChatBot](https://awschatbot.devpost.com/)<br>
>[WikiPedia](https://archive.org/download/enwiki-20080312)<br>
