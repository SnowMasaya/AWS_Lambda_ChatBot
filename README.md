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

If you already prepare the json data set, you move the json data the below folder


#
### Code Directory Structure 
#

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
