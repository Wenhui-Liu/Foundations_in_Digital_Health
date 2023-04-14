Comp.5520—Foundations in Digital Health—Spring 2023 Project 3-----reademe

Group Members‘ Name: Weibin Huang, Wenhui Liu, Yifan Zhang

E-mail: Weibin_Huang@student.uml.edu, Wenhui_Liu@student.uml.edu, yifan_zhang1@student.uml.edu

# Digital Health Project3: Train a SBDH NER  
Description:
In this project：
    Data preprocessing: Under data preprocessing folder, Lab3.ipynb is used to preprocessing data. It retrieves the social history part from discharge notes in mimiciii database and convert those annotated notes with SBDH related keywords into spacy format. 
    data.spacy contains all the data from training.csv. 
    train.spacy and test.spacy contains 80% and 20% data from training.csv respectively.  
  
    Training: To train a model with 80% data and validated on the other 20% data, simply go to the directory of training80dev20 folder and run the following command: python -m spacy train config.cfg --output ./output  
    You will get the best model under output/model-best and you can see the evaluation metrics in output/model-best/meta.json.

    To train and validated with all the data from training.csv, go to trainingdevall folder and run the following command: python -m spacy train config.cfg --output ./output  

    Testing: If there is a new test dataset with unseen data, you can test the performance of the previous trained model by running: python -m spacy evaluate ./output/model-best ./test.spacy > test_evaluation.txt   
    the test.spacy should be the spacy file contains the test data.  
    You will see the test results in test_evaluation.txt. 
  

GitHub link to your source code:

	https://github.com/Wenhui-Liu/Foundations_in_Digital_Health/tree/main/Project2

	Since this GitHub repository is private, you may not be able to link directly to my GitHub. 
	But we have set you as a collabrator, so that you can view it conveniently
