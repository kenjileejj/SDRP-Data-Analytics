'''
Team 4: "SDRP Decisions"
Lee Jia Juinn, Kenji
Sung Yu Xin
Lim Wei Zhen
'''

import pandas as pd
import statsmodels.formula.api as smf

#LOAD DATA
df = pd.read_csv(r'https://tinyurl.com/SDRP-AI-SUBMISSION')
#df = df.iloc[0:33,1:63]

#Recalibration of Certain Data for categorical
df.Panelist[df.Panelist == 'Jim Lim'] = '1Jim Lim'
df.Country_of_Respondent[df.Country_of_Respondent == 'Singapore'] = '1Singapore'
df.Country_of_Complainant[df.Country_of_Complainant == 'Singapore'] = '1Singapore'

#Data Processing - Categorizing Variables which are categorical
df['Usage_of_Domain_name'] = df['Usage_of_Domain_name'].astype('category')
df['Panelist_Type'] = df['Panelist_Type'].astype('category')
df['Country_of_Respondent'] = df['Country_of_Respondent'].astype('category')
df['Country_of_Complainant'] = df['Country_of_Complainant'].astype('category')
df['Industry_Complainant'] = df['Industry_Complainant'].astype('category')
df['Industry_Registrant'] = df['Industry_Registrant'].astype('category')
df['Panelist'] = df['Panelist'].astype('category')
df['Year_of_Judgment'] = df['Year_of_Judgment'].astype('category')



print df['Country_of_Respondent']

#Creating the List of Data concerning Transfer of Domain Names (to be used in modelling below)
actual = df['Conclusion']
actual = actual.tolist()

#Creating the Function to Print: True and False Positives and Negatives, Accuracy, Precision, Recall, F1
#A GENERAL FUNCTION (to calculate Accuracy, Precision, Recall and F1)
'''
Let:
tp = N.o of True Positives
tn = N.o of True Negatives
fp = N.o of False Positives
fn = N.o of False Negatives

y_hat = predicted results
y = actual results
'''

def function(y_hat, y):
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    # To Count the Number of True Positives and True Negatives:
    # Defensive Programming - to ward against errors
    if len(y_hat) != len(y):
        return None  # If the length of both are different, there must have been an error somewhere.
    else:
        #Count number of true positives
        for n in range(len(y)):
            if y_hat[n] > 0.5 and y[n] == 1:
                tp += 1
        #Count number of false positives
        for n in range(len(y)):
            if y_hat[n] > 0.5 and y[n] == 0:
                fp += 1
        #Count number of true negatives:
        for i in range(len(y)):
            if y_hat[i] < 0.5 and y[i] == 0:
                tn += 1
        #Count number of false negatives:
        for i in range(len(y)):
            if y_hat[i] < 0.5 and y[i] == 1:
                fn += 1


    print "The number of true positives is " + str(tp)
    print "The number of true negatives is " + str(tn)
    print "The number of false positives is " + str(fp)
    print "The number of false negatives is " + str(fn)

    # Function to Calculate Accuracy
    accuracy = float(tp + tn) / float(len(y_hat))
    print "The accuracy is " + str(accuracy)

    #Function to Calculate Precision
    precision = float(tp) / float((tp+fp))
    print "The precision is " + str(precision)

    #Function to Calculate Recall
    recall = float(tp) / float((tp+fn))
    print "The recall is " + str(recall)

    #Function to Calculate F1 Score
    f1 = 2 * float(precision*recall) / float(precision + recall)
    print "The F1 score is " + str(f1)

    return " "

#Printing of the Summary of Variables

print "\n" + "SUMMARY"
print df.describe()

print "\n"+"SUMMARY OF ATTRIBUTES"

print "\n"+"LEGEND"
print "\n"+"1 = Yes / Present in Judgment"
print "\n"+"0 = No / Not mentioned in Judgment"
print "\n"+"-1 = No"

print "\n"+"General Attributes"
print "\n"+"Conclusion"
print df['Conclusion'].value_counts()

print "\n"+"Length of Cases (in Months)"
print df['Length_of_Cases_in_months'].value_counts()

print "\n"+"Year of Judgment"
print df['Year_of_Judgment'].value_counts()

print "\n"+"Country of Respondent"
print df['Country_of_Respondent'].value_counts()

print "\n"+"Country of Complainant"
print df['Country_of_Complainant'].value_counts()

print "\n"+"Industry of Complainant"
print df['Industry_Complainant'].value_counts()

print "\n"+"Industry of Respondent"
print df['Industry_Registrant'].value_counts()

print "\n"+"Panelist"
print df['Panelist'].value_counts()

print "\n"+"Panelist Type"
print df['Panelist_Type'].value_counts()

print "\n"+"Was there an Attempt to Settle"
print df['Attempts_to_settle'].value_counts()

print "\n"+"Number of Attempts to Settle"
print df['Number_of_settle_attempts'].value_counts()

print "\n"+"Was there Mediation Prior to this? "
print df['Mediation_prior'].value_counts()

print "\n"+"How many attempts were there to Mediate? "
print df['Mediaiton_Prior_attempts'].value_counts()

print "\n"+"Number of Singaporean cases cited?"
print df['No_Cited_SG_Cases'].value_counts()

print "\n"+"Number of SDRP cases cited?"
print df['No_Cited_SDRP_cases'].value_counts()

print "\n"+"Number of UK and EU cases cited?"
print df['No_Cited_UK_EU_cases'].value_counts()

print "\n"+"Number of US cases cited?"
print df['No_Cited_US_Cases'].value_counts()

print "\n"+"Number of WIPO/UDRP cases cited?"
print df['No_Cited_WIPO_UDRP_cases'].value_counts()



print "\n" + "SUMMARY: Element 1 - Identical / Confusing Similarity"
print "\n"+"Is the word a Made Up Word?"
print df['Made_up_word'].value_counts()

print "\n"+"Is the word an English Word?"
print df['English_word'].value_counts()

print "\n"+"Length of Word?"
print df['Length_of_word'].value_counts()

print "\n"+"Is the Domain a variation of the Complainant's mark or brand?"
print df['Domain_a_variation_of_mark_or_brand'].value_counts()

print "\n"+"Does the Complainant have an existing trade mark?"
print df['Existence_of_Trade_Mark'].value_counts()

print "\n"+"Is the Complainant's trademark registered in Singapore?"
print df['Trade_Mark_Registered_in_Singapore'].value_counts()

print "\n"+"Is the Trademark registered in other Countries?"
print df['Trade_Mark_Registered_in_other_Countries'].value_counts()

print "\n"+"Length the trademark has been registered in Singapore? (in years)"
print df['Length_of_Trade_Mark_SG'].value_counts()

print "\n"+"Is the mark a Well-Known Mark?"
print df['Well_Known_Mark'].value_counts()

print "\n"+"Is the Complainant a foreign brand?"
print df['Foreign_brand'].value_counts()

print "\n"+"Is the Complainant a well-known foreign brand?"
print df['Well_known_Foreign_Brand'].value_counts()

print "\n"+"Are the domain name and Complainant's mark identical or confusingly similar?"
print df['Identical_Confusing_Similarity'].value_counts()

print "\n"+"Are the domain name and Complainant's mark exactly identical?"
print df['Identical_Words'].value_counts()

print "\n"+"Are the domain name and Complainant's mark similar?"
print df['Similar_words'].value_counts()

print "\n"+"What is the % that the words are similar?"
print df['Percentage_of_Similarity_of_Words'].value_counts()

print "\n"+"Are the pronounciation of the words similar?"
print df['Pronounciation_Similarity'].value_counts()



print "\n" + "SUMMARY: Element 2 - Complainant showed Respondent has no legitimate interests in the domain name"
print "\n"+"Has the Complainant showed that the Registrant has no legitimate interests in the domain name?"
print df['Complainant_Showed_Registrant_No_Legitimate_Interests'].value_counts()

print "\n"+"Did the Complainant have prior ownership of the Domain name?"
print df['Complainant_Prior_ownership'].value_counts()

print "\n"+"Did the Respondent show bona fide registration / usage of the domain name?"
print df['Respondent_Showed_Bona_Fide'].value_counts()

print "\n"+"Did the Respondent show that they had used the domain name fairly?"
print df['Respondent_showed_fair_use'].value_counts()

print "\n"+"Did the Respondent show that they are commonly known to a section of the market?"
print df['Respondent_Showed_Commonly_Known'].value_counts()

print "\n"+"Has the Respondent been using the Domain Name?"
print df['Respondent_using_Domain_Name'].value_counts()

print "\n"+"How has the Respondent been using the Domain Name?"
print df['Usage_of_Domain_name'].value_counts()

print "\n"+"* NOTE - Legend" \
    "\n" + "0 - Respondent did not use the domain name" \
"\n" + "1 - Respondent used the domain name for sale/rent/advertisements" \
       "\n"+"2 - Respondent used the domain name to redirect to another site / their own site's business" \
              "\n"+"3 - Respondent had legitimate usage of the domain name"

print "\n"+"Length of Usage of Domain Name?"
print df['Length_of_usage'].value_counts()

print "\n"+"Does the Respondent have localised goodwill attached to its domain name in Singapore?"
print df['Existence_of_localised_goodwill'].value_counts()

print "\n"+"Does the Respondent have localised goodwill attached to its domain name in Singapore?"
print df['Group_of_goodwill'].value_counts()

print "\n"+"Did the Complainant abandon the domain name?"
print df['Abandonment_by_Complainant'].value_counts()



print "\n" + "SUMMARY: Element 3 - Respondent Registered/Used Domain Name in Bad Faith"
print "\n"+"Is there evidence of Circumstances of registration for valuable consideration?"
print df['Evidence_of_Circumstances_of_registration_for_valuable_consideration'].value_counts()

print "\n"+"Is there evidence of registration to prevent Trademark owner usage?"
print df['Evidence_of_Registration_to_prevent_Trademark_owner_usage'].value_counts()

print "\n"+"Is there evidence of registration to disrupt business of Trademark proprietor?"
print df['Evidence_of_registration_to disrupt_business_of_trademark_proprietor'].value_counts()

print "\n"+"Is there evidence of registration to attract customers for commercial gain through likelihood of confusion?"
print df['Evidence_of_Attracting_customers_for_commercial_gain_through_likelihood_of_confusion'].value_counts()

print "\n"+"Is there evidence of bad faith on other grounds?"
print df['Evidence_of_bad_faith_on_other_grounds'].value_counts()

print "\n"+"Did the Respondent attempt to sell the domain name"
print df['Respondent_Attempt_to_sell'].value_counts()

print "\n"+"Did the Respondent respond to the Complainant?"
print df['Did_Respondent_Respond'].value_counts()

print "\n"+"No response from respondent "
print df['No_response_from_respondent'].value_counts()

print "\n"+"Was there a prior commercial relationship between the parties?"
print df['Prior_Commercial_relationship_between_parties'].value_counts()




#Descriptive Analysis
#Descriptive Statistics - Number of Cases over the Years
descriptiveData = df.groupby(['Year_of_Judgment']).size().reset_index(name = "Frequency")
print descriptiveData   #While the histogram may be plotted by the Python code itself, it is an active choice to instead use the one inbuilt in KeyNote to plot it out using the data adduced here. The Data in the keynote incldues the settled cases, which is added on manually.

#Descriptive Statistics - Proportion of cases decided in favour of Complainant
descriptiveData = df.groupby(['Conclusion']).size().reset_index(name = "Frequency")
print descriptiveData

#Descriptive Statistics - Default Cases
descriptiveData = df.groupby(['No_response_from_respondent']).size().reset_index(name = "Frequency")
print descriptiveData

#Descriptive Statistics - Number of Precedents Cited by Years
descriptiveData = df.groupby(['Year_of_Judgment', 'No_Cited_SG_Cases']).size().reset_index(name = "Frequency")
print descriptiveData
descriptiveData = df.groupby(['Year_of_Judgment', 'No_Cited_SDRP_cases']).size().reset_index(name = "Frequency")
print descriptiveData
descriptiveData = df.groupby(['Year_of_Judgment', 'No_Cited_UK_EU_cases']).size().reset_index(name = "Frequency")
print descriptiveData
descriptiveData = df.groupby(['Year_of_Judgment', 'No_Cited_US_Cases']).size().reset_index(name = "Frequency")
print descriptiveData
descriptiveData = df.groupby(['Year_of_Judgment', 'No_Cited_WIPO_UDRP_cases']).size().reset_index(name = "Frequency")
print descriptiveData
#These data were then used to divide by the cases each year to obtain the Number of Precedents Cited Per Case


#MODELS
'''
In this section we seek to come up with linear and logistic models of our data.

We decided on the following naming systems:
sm stands for sub-model
gm stands for general-model

so the models would be named as such: e.g. sm1_linear means the linear sub-model for the first element
'''
#SUB-MODEL 1: IDENTICAL/CONFUSING SIMILARITY
print "SUB-MODEL 1: Identical / Confusing Similarity"

    #Linear Model
print "SUB-MODEL 1: Identical / Confusing Similarity (LINEAR)"
sm1_linear = smf.ols(formula = 'Identical_Confusing_Similarity ~ Length_of_word + English_word+Trade_Mark_Registered_in_Singapore + Trade_Mark_Registered_in_other_Countries + Well_Known_Mark', data = df).fit()

print sm1_linear.summary()
predictedValue = sm1_linear.predict()
predictedValue = predictedValue.tolist()
print function(predictedValue,actual)



    #Logit Model
print "SUB-MODEL 1: Identical / Confusing Similarity (LOGIT)"

sm1_log = smf.logit(formula = 'Conclusion ~ Length_of_word + English_word+Trade_Mark_Registered_in_Singapore + Well_Known_Mark', data = df).fit()
print sm1_log.summary()
predictedValue = sm1_log.predict()
predictedValue = predictedValue.tolist()
print function(predictedValue,actual)

#SUB-MODEL 2: Complainant has shown that Respondent has no Legitimate Interest
print "SUB-MODEL 2: Complainant has shown that Respondent has no Legitimate Interests"

    #Linear Model
print "SUB-MODEL 2: Complainant has shown that Respondent has no Legitimate Interests (LINEAR)"
sm2_linear = smf.ols(formula = 'Complainant_Showed_Registrant_No_Legitimate_Interests ~ Respondent_Showed_Bona_Fide + Respondent_showed_fair_use + Usage_of_Domain_name', data = df).fit()
print sm2_linear.summary()
predictedValue = sm2_linear.predict()
predictedValue = predictedValue.tolist()
print function(predictedValue,actual)


    #Logit Model
print "SUB-MODEL 2: Complainant has shown that Respondent has no Legitimate Interests (LOGIT)"
        #Recalibrate data to make it binomial / only have 2 values instead of the original 3/4 values
'''

df['Complainant_Showed_Registrant_No_Legitimate_Interests'] = df["Complainant_Showed_Registrant_No_Legitimate_Interests"].map({-1:0, 0:0, 1:1})
df['Respondent_Showed_Bona_Fide'] = df["Respondent_Showed_Bona_Fide"].map({-1:0, 0:1, 1:1})
df['Respondent_showed_fair_use'] = df["Respondent_showed_fair_use"].map({-1:0, 0:1, 1:1})
df['Usage_of_Domain_name'] = df["Usage_of_Domain_name"].map({0:1, 1:0, 2:0, 3:1})
This mapping is no longer required given that the model was not helpful
#we tried the following logit model, which ran into errors. another model we tried also encountered a low pseudo R and very high P values that were close to 1. Thus we conclude that a logistic model is not appropriate for the data set for this second element of proving that the Complainant has no legitimate interests.

sm2_log = smf.logit(formula = 'Complainant_Showed_Registrant_No_Legitimate_Interests ~ Respondent_Showed_Bona_Fide + Respondent_showed_fair_use + Usage_of_Domain_name + Complainant_Prior_ownership', data = df).fit()
print sm2_log.summary()
predictedValue = sm2_log.predict(df)
predictedValue = predictedValue.tolist()
print function(predictedValue,actual)
'''

print "SUB-MODEL 3: Respondent registered or used the domain name in bad faith"

    #Linear Model
print "SUB-MODEL 3: Respondent registered or used the domain name in bad faith (LINEAR)"
sm3_linear = smf.ols(formula='Conclusion ~ No_response_from_respondent+Evidence_of_Attracting_customers_for_commercial_gain_through_likelihood_of_confusion+Evidence_of_bad_faith_on_other_grounds+Respondent_Attempt_to_sell', data=df).fit()
predictedValue = sm3_linear.predict(df)
predictedValue = predictedValue.tolist()

print sm3_linear.summary()
print function(predictedValue,actual)

    #Logit Model
print "SUB-MODEL 3: Respondent registered or used the domain name in bad faith (LOGIT)"

sm3_log = smf.ols(formula='Conclusion ~ No_response_from_respondent+Evidence_of_Attracting_customers_for_commercial_gain_through_likelihood_of_confusion+Evidence_of_bad_faith_on_other_grounds+Respondent_Attempt_to_sell', data=df).fit()
predictedValue = sm3_log.predict(df)
predictedValue = predictedValue.tolist()
print sm3_log.summary()
print function(predictedValue,actual)

print "GENERAL MODEL:"
    #Model A: Conclusion ~ General Variables
        #1 Panelists
gmA1_linear = smf.ols(formula='Conclusion ~ Panelist',data=df).fit()
print gmA1_linear.summary()
predictedValue = gmA1_linear.predict()
predictedValue = predictedValue.tolist()
print function(predictedValue,actual)

        #2 Panelist Type
gmA2_linear = smf.ols(formula='Conclusion ~ Panelist_Type',data=df).fit()
print gmA2_linear.summary()
predictedValue = gmA2_linear.predict(df)
predictedValue = predictedValue.tolist()
print function(predictedValue,actual)

        #Country of Complainant and Respondent
gmA3_linear = smf.ols(formula='Conclusion ~ Country_of_Respondent + Country_of_Complainant',data=df).fit()
print gmA3_linear.summary()
predictedValue = gmA3_linear.predict()
predictedValue = predictedValue.tolist()
print function(predictedValue,actual)

        #General Variables: Attempts to Settle/Mediate
gmA4_linear = smf.ols(formula='Conclusion ~ Attempts_to_settle + Number_of_settle_attempts + Mediation_prior + Mediaiton_Prior_attempts', data=df).fit()
predictedValue = gmA4_linear.predict(df)
predictedValue = predictedValue.tolist()
print gmA4_linear.summary()
print function(predictedValue,actual)


        #Log Model of Panelists + Attempts to Settle + Mediation Prior
''' Rationale: different panelists would afford different weight of the parties efforts to settle and mediate'''
gmA1_log = smf.logit(formula='Conclusion ~ Panelist_Type + Attempts_to_settle + Mediation_prior', data=df).fit()

predictedValue =gmA1_log.predict(df)
predictedValue = predictedValue.tolist()

print gmA1_log.summary()
print function(predictedValue, actual)


gmA1_linear = smf.ols(formula='Conclusion ~ Attempts_to_settle + Mediation_prior', data=df).fit()

predictedValue =gmA1_linear.predict(df)
predictedValue = predictedValue.tolist()

print gmA1_linear.summary()
print function(predictedValue, actual)

        #Precedents
gmA5_linear = smf.ols(formula = 'Conclusion ~  Country_of_Respondent + Panelist_Type + No_response_from_respondent + No_Cited_WIPO_UDRP_cases + No_Cited_US_Cases + No_Cited_UK_EU_cases + No_Cited_SDRP_cases + No_Cited_SG_Cases', data = df).fit()

predictedValue =gmA5_linear.predict()
predictedValue =predictedValue.tolist()

print gmA5_linear.summary()
print function(predictedValue,actual)



    #Model B: Conclusion ~ Attributes from Elements
        #Without Dummy Variable
            #Variable was phrased as "No response from respondent"
gmB1_linear = smf.ols(formula='Conclusion ~ Trade_Mark_Registered_in_Singapore+ No_response_from_respondent+Well_known_Foreign_Brand+Usage_of_Domain_name+Respondent_Showed_Bona_Fide+Evidence_of_Circumstances_of_registration_for_valuable_consideration+Evidence_of_Attracting_customers_for_commercial_gain_through_likelihood_of_confusion+Evidence_of_bad_faith_on_other_grounds+Respondent_Attempt_to_sell',data=df).fit()

predictedValue =gmB1_linear.predict(df)
predictedValue = predictedValue.tolist()

print gmB1_linear.summary()
print function(predictedValue,actual)

            #Variable was phrased as: "Did respondent respond"
gmB2_linear = smf.ols(formula='Conclusion ~ Trade_Mark_Registered_in_Singapore + Did_Respondent_Respond+Well_known_Foreign_Brand+Usage_of_Domain_name+Respondent_Showed_Bona_Fide+Evidence_of_Circumstances_of_registration_for_valuable_consideration+Evidence_of_Attracting_customers_for_commercial_gain_through_likelihood_of_confusion+Evidence_of_bad_faith_on_other_grounds+Respondent_Attempt_to_sell', data=df).fit()

predictedValue =gmB2_linear.predict(df)
predictedValue = predictedValue.tolist()

print gmB2_linear.summary()
print function(predictedValue,actual)

        #With Dummy Variables (we added Trade_Mark_Registered_in_Singapore as a control for Well_known_Foreign_Brand)
gmB3_linear = smf.ols(formula='Conclusion ~  No_response_from_respondent + Well_known_Foreign_Brand + Trade_Mark_Registered_in_Singapore + Percentage_of_Similarity_of_Words + Length_of_usage + Evidence_of_Circumstances_of_registration_for_valuable_consideration + Evidence_of_Attracting_customers_for_commercial_gain_through_likelihood_of_confusion + Evidence_of_bad_faith_on_other_grounds + Respondent_Attempt_to_sell',data=df).fit()


predictedValue = gmB3_linear.predict(df)
predictedValue = predictedValue.tolist()

print gmB3_linear.summary()
print function(predictedValue,actual)

    #Model C: Conclusion ~ General Variables + Attributes from Elements
gmC1_linear = smf.ols(formula='Conclusion ~ Panelist_Type+Attempts_to_settle + Mediation_prior + No_response_from_respondent+Well_known_Foreign_Brand+Trade_Mark_Registered_in_Singapore+Usage_of_Domain_name+Respondent_Showed_Bona_Fide+Evidence_of_Circumstances_of_registration_for_valuable_consideration+Evidence_of_Attracting_customers_for_commercial_gain_through_likelihood_of_confusion+Evidence_of_bad_faith_on_other_grounds',data=df).fit()


predictedValue = gmC1_linear.predict(df)
predictedValue = predictedValue.tolist()

print gmC1_linear.summary()
print function(predictedValue,actual)