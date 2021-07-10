# Sea-Water-Quality-using-Machine-Learning

I was Selected For SMART INDIA HACKATHON,Conducted By Government of India, where we have Given a Problem to solve, By the MINISTRY OF EARTH SCIENCE,Govt of india...

The Problem Statement was "To Predict the quality of water by considering the given Features..."

We have Given the Dataset with Features..

It is a supervised Learning Problem ..

# Approach

# Supervised Learning Problem : Given Set of 'X's' , Predict 'Y'...

The Dataset contains all Features as Objects Datatypes with Many NaN Values. It is challening for us and it is Not Good to Proceed MODEL BUILDING with the UNCLEANED DATA...

We,Then Cleaned The Data :
  * Filled the Missing Values using Imputation Techniques...
  * Converted the Datatype of all Features to Categorical Datatypes using "astype('category')" function...
  * Lebel Encoded the Values for each Feature..
  * Then proceeded with DRAWING Insights From the Data...
  * Done train_test_split on the Data..
  * Then Proceeded with MODEL BUILDING.. :
  *  Fed Data (X_train to Different Models that include  :
  *       1. Linear Regression, 2. Decision Trees,3. Random Forest,4. Stochastic Gradient Boosting,5. Lasso,6. Linear Support vector Regressor,K-NN
  *  Cross Validation Done...
  *  Then Calculated  METRICS Such as : 
  *        R2_Score (R-Square score) and RMSE (Root mean Square Error) of Train Data scores, Cross validation score,and Test Data Scores
  *  Then Selected the Best Model using METRICS Comparison and Found RANDOM FOREST as Best Model and Given New Data, it is Predicing with Minimum Error
  *   Given that model To the MINISTRY OF EARTH SCIENCE 

# Thanks To Prof.Madhu(Ph.D),for Recommending me For the Hackathon among  350 Students in COMPUTER SCIENCE DEPARTMENT,GURU NANAK INSTITUTIONS,Hyderabad... 
