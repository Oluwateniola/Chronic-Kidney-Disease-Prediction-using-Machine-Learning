# Chronic-Kidney-Disease-Prediction-using-Machine-Learning


The data science lifecycle is designed for big data issues and the data science projects. 
Generally, the data science project consists of seven steps which are problem definition, data collection, data preparation, data exploration,
machine learning modeling, model evaluation and model deployment.

The goal of this project is to go through the data science lifecycle steps in order to build a heart disease classification web application
using kidney disease dataset. This project uses FastAPI to deploy the model and build the web application.

# Dataset

Data Set Column Information: - 26 attributes 
<li>age	-	age</li>
<li>bp	-	blood pressure </li>
<li>sg	-	specific gravity </li>
<li>al	- albumin </li>
<li>su	-	sugar </li>
<li>rbc	-	red blood cells </li>
<li>pc	-	pus cell </li>
<li>pcc	-	pus cell clumps </li>
<li>ba	-	bacteria </li>
<li>bgr	-	blood glucose random </li>
<li>bu	-	blood urea </li>
<li>sc	-	serum creatinine </li>
<li>sod	-	sodium </li>
<li>pot	-	potassium </li>
<li>hemo	-	hemoglobin </li>
<li>pcv	-	packed cell volume </li>
<li>wc	-	white blood cell count </li>
<li>rc	-	red blood cell count </li>
<li>htn	-	hypertension </li>
<li>dm	-	diabetes mellitus </li>
<li>cad	-	coronary artery disease </li>
<li>appet	-	appetite </li>
<li>pe	-	pedal edema </li> 
<li><li>ane	-	anemia </li>
<li>class	-	classification </li>

# Discussion

In this study, I developed and evaluated a series of artificial intelligence-based models considering minimum variables such as sex, age, 
symptoms, and medications. These models predict patients’ likelihood of having chronic kidney disease. Among various models tested, support vector classifier (SVC) 
performed best, with a prediction score of 0.9937. 

This work examines the ability to detect CKD using machine learning algorithms while considering the least number of tests or features. 
I approached this by applying five machine learning classifiers: logistic regression, SVM, random forest, and decision tree classifier and K nearest neighbors 
on a small dataset of 400 records. In order to reduce the number of features and remove redundancy, the association between variables have been studied. 
A filter feature selection method has been applied to the remaining attributes and found that there are hemoglobin, albumin, and specific gravity have the most 
impact to predict the CKD.

The classifiers have been trained, tested, and validated using 5-fold cross-validation. Higher performance was achieved with the gradient boosting algorithm
by accuracy score of 0.994
