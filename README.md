# Health-Care-Provider-Fraud-Detection-Analysis

### <b>1. <u>Introduction</u></b>: 
Health care fraud is an organized crime which involves peers of providers, physicians, beneficiaries acting together knowingly mis-representing or mis-stating something about the type, the scope, or the nature of the medical treatment or service provided, in a manner that could result in unauthorized payments(fraud claims) being made. Fraud and abuse have led to significant additional expenses in the health care systems. Insurance companies are the most vulnerable institutions impacted due to these bad practices. Due to this reason, insurance companies increased their insurance premiums and as result healthcare is becoming a costly matter day by day. Healthcare fraud and abuse take many forms. Some of the most common types of frauds by providers are:
<ol type = 'i'>
<li>Billing for services that were not provided.</li>
<li>Duplicate submission of a claim for the same service.</li>
<li>Misrepresenting the service provided.</li>
<li>Charging for a more complex or expensive service than was actually provided.</li>
<li>Billing for a covered service when the service actually provided was not covered.</li>
</ol>

### <b>2. <u>Business Problem</u></b>:
<ol type = 'i'>
<li><u>Goal Setting</u>:  Predict the potentially fraudulent providers based on the claims filed by them.</li>
<li><u>Tasks</u>:</li>
<ol type = 'a'>
<li>To identify important variables/features which help in detecting the behavior of potentially fraud providers.</li>
<li>To understand future behavior of providers by identifying fraudulent patterns in the provider's claims.</li>
</ol> 
</ol>

### <b>3. <u>ML Formulation</u></b>:
<ol type = 'i'>
<li><u>Objective</u>:  To design a binary classification model which predicts if a claim applied by providers is fraud or legitimate based on the beneficiary details, inpatient and outpatient data.</li>
<li><u>Business Constraints</u>: The business constraints are as follows: </li>
<ol type = 'a'>
<li>Interpretability: Highly important to cite reasons why the model predicted a claim as fraud. This may be required for further investigation with the providers.</li>
<li>Misclassifications: The Cost of misclassification is high as seen from the confusion matrix. If FN are high means we are predicting the fraudulent claims as legitimate and if FP are high means we are predicting the legitimate claims as fraudulent.</li>
<li>Cost of Misclassifications: Higher FN and FP will result in cost involved to further drill down if actually a claim is fraud or not by further investigation. If FN is high Cost will be reimbursed for fraud claims and if FP is high then additional cost of investigation is added to it.</li>
<li>Latency Requirement: Since the claim reimbursement process takes time means there is no such latency requirement. But still we will consider reducing the training time of model.</li>
</ol> 
</ol>

### <b>4. <u>Reference Research Papers</u></b>:
<ol type = 1>
<li><b>A survey on statistical methods for health care fraud detection</b>:  https://cpb-us-w2.wpmucdn.com/sites.gatech.edu/dist/4/216/files/2015/09/p70-Statistical-Methods-for-Health-Care-Fraud-Detection.pdf</li>
<li><b>Predicting Healthcare Fraud in Medicaid: A Multidimensional Data Model and Analysis Techniques for Fraud Detection</b>:  https://www.sciencedirect.com/science/article/pii/S2212017313002946</li>
</ol>
