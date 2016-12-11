# README #

This is a sample solution for caching and searching for URLs in a lookup table

### Technologies ###
* MySql server
* solr6.3
* mysql-connector-java-5.0.8

### Contents ###

* Folder [solr-6.3.0] contains solr data and url_lookup_core and configurations
* File [URL_Lookup_url_mapping.sql] sample mysql lookup table
* Folder [Solr_config_files] contains sorl core and configurations schema, db importer
* File [examples] contains some query examples

### How do I get set up? ###

* clone the repo or clone only needed configurations
* configure directories in configuration files with your machine
* configure mysql database server with your database server
* start solr server with this command /bin/solr start
* import and index data with this get request http://localhost:8983/solr/url_lookup_core/dataimport?command=full-import
* Do search requests ex: http://localhost:8983/solr/url_lookup_core/select?indent=on&q=url_from:"/products?tag=5678"&wt=json
* Note: you can use solr query for searching

### contact ###
Ahmed Mansy ahmed.mansy156@gmail.com