# twitterlize

### Setting up a dev environment for Elastic search and Kibana 

Run the python script from your local terminal and analyze twitter trends on Kibana using ES 

```
#Creating elasticsearch container and configuring it to run on localhost 9200 
docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.12.1
docker run --name es01-test --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.12.1
```

```
#Creating Kibana container and configuring it to run on localhost 5601 
docker pull docker.elastic.co/kibana/kibana:7.12.1
docker run --name kib01-test --net elastic -p 5601:5601 -e "ELASTICSEARCH_HOSTS=http://es01-test:9200" docker.elastic.co/kibana/kibana:7.12.1
```

#### Clean up 

```
docker stop es01-test
docker stop kib01-test

#Remove the containers and the network 
docker network rm elastic
docker rm es01-test
docker rm kib01-test
```

#### Usage 

```
 python3 twitterlize.py India
 ```
 
Kibana Dashboard : 

 ```
 localhost:5601 
 #Create index for sentiment 
 # View logs in discover 
 ```
 
 <img width="1171" alt="Screen Shot 2021-05-14 at 1 45 28 AM" src="https://user-images.githubusercontent.com/81785727/118245799-148e7680-b456-11eb-93e4-d88d705cde57.png">

 
 <img width="1428" alt="Screen Shot 2021-05-14 at 1 44 06 AM" src="https://user-images.githubusercontent.com/81785727/118245695-f9236b80-b455-11eb-898b-046e4a8912bf.png">
 
 
 
