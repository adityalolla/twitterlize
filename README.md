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


