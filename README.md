# Webservice_URLLIB
Web-service which will return data from URL using URLLIB


# Pre-Requisites
a) python (preferably 3+ )

b) Flask

c) memcached ( 1.4.5 or later)

d) pymemcache

# Execution
a) Place 'package_dep_webservice.py' and synk_task folder in one location and run:-  python package_dep_webservice.py

b) Upon Running open browser and run 'http://127.0.0.1:5000/dependencies/<PACKAGE NAME>/<VERSION>' e.g.. http://127.0.0.1:5000/dependencies/express/latest


The Purpose is to create a webservice app which upon querying should return data.

1) There are packages and its related information data like version number , its dependencies etc .. are present on https://registry.npmjs.org.

2) The Objective is to fetch Package dependencies information in a tree fashion structure .

3) Creating a Web service which will be provided with package name and its version , and will display its dependencies in tree fashion.

4) The task is divided into 2 parts ,

    --->  Fecth data from URL using URLLIB and get its dependencies information.
    
    --->  This dependencies value will be used by web service app to return it to web user.
  
  
5) URL Data 

    --->  This is a package name synk_test inside which has the file to return tree data
    
    --->  to fecth data URLLIB has been used 
    
    --->  If any invalid URL is used then using exception handling it will return Error Message which eventually be returned to calling program.
    
    --->  THIS URL Program will accept 2 parameter ( Package name and version value , e.g.. package-> 'express' , version -> 'latest'), So that the URL will become 'https://registry.npmjs.org/express/latest' or 'https://registry.npmjs.org/async/2.0.1'
  
  
6)  Web Service 

      ---> Flask library is used to create a web service app.
      
      ---> It also used pymemcache for caching the data , so that for next call it can fetch data from cache instead of again going to URL Data.
      
      --->  If there is no record found in cache then it will call URL Data ( from synk_task Package ) and will return it to web user and also cache it .
      
      
      
      
      
   Use Unix Env to execute
