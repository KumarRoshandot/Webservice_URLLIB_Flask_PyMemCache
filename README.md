# Webservice_URLLIB
Web-service which will return data from URL using URLLIB

The Purpose is to create a webservice app which upon querying should return data.

1) There are packages and its related information data like version number , its dependencies etc .. are present on https://registry.npmjs.org.

2) The Objective is to fetch Package dependencies information in a tree fashion structure .

3) Creating a Web service which will be provided with package name and its version , and will display its dependencies in tree fashion.

4) The task is divided into 2 parts ,

  --->  Fecth data from URL using URLLIB and get its dependencies information
  --->  This dependencies value will be used by web service app to return it to web user.
  
  
5) URL Data 

  --->  This is a package name synk_test inside which has the file to return tree data.
  --->  to fecth data URLLIB has been used 
  --->  If any invalid URL is used then using exception handling it will return Error Message which eventually be returned to calling program.
  --->  THIS URL Program will accept 2 parameter ( Package name and version value , e.g.. package-> 'express' , version -> 'latest'), So that the URL will become 'https://registry.npmjs.org/express/latest' or 'https://registry.npmjs.org/async/2.0.1'
  
  
6) 
