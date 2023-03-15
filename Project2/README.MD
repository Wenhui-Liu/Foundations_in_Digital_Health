Comp.5520—Foundations in Digital Health—Spring 2023
Project 2-----reademe

Group Members‘ Name: Weibin Huang, Wenhui Liu, Yifan Zhang


E-mail: Weibin_Huang@student.uml.edu, Wenhui_Liu@student.uml.edu, yifan_zhang1@student.uml.edu

Description: In this project： 
             1. Data extraction and indexing are in Part 1 Lab2.ipynb. To create a new core, 
			 run ./bin/solr create -c test -d path_to/conf. We've used all the files in conf folder
             provided in the course github page except the schema.xml. You can replace the managed-schema
             with our shcema.xml in the conf folder and then create the core.
		     2. We've implemented both command line user interface and GUI for the search system. You can find 
             command line user interface search system in Part 2 in Lab2.ipynb.
             3.For GUI search system. The related pthon files are: main.py, UI_model.py and UMLS_CONNECT.py. 
             To get the results for the search system, simply run main.py.

            Run system against the following query conditions, and save all screen shots in a file.
			1. Car crash in note text
			2. Car crash in note text and hospital_expire_flag=1 for the associated hospital admission
			3. 162.9 in ICD codes.
			4. Note chartdate is between 2110-01-01 AND 2120-01-01 
			5. Brain cancer and its synonyms from CHV in note text


GitHub link to your source code:

		https://github.com/Wenhui-Liu/Foundations_in_Digital_Health/tree/main/Project2

		Since this GitHub repository is private, you may not be able to link directly to my GitHub. 
		But we have set you as a collabrator, so that you can view it conveniently
