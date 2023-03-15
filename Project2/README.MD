These are the submission files for Lab2.  

Data extraction and indexing are in Lab2.ipynb. To create a new core, run ./bin/solr create -c test -d path_to/conf. We've used all the files in conf folder provided in the course github page except the schema.xml. You can replace the managed-schema with our schema.xml in the conf folder and then create the core.  

We've implemented both command line user interface and GUI for the search system. You can find command line user interface search system in Lab2.ipynb.     

For GUI search system. The related pthon files are: main.py, UI_model.py and UMLS_CONNECT.py. To get the results for the search system, simply run main.py.
