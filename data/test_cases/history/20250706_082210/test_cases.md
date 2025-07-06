### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'target': '#job-description-input', 'value': 'Looking for a 2-year experienced JavaScript developer with AWS experience'}
2. {'action': 'click', 'target': '#save-job-description-btn'}
**Expected Result:** Job description is saved and skill recommendations are displayed

### Select Skills from AI Recommendations
**Steps:**
1. {'action': 'click', 'target': '#skill-recommendation-list'}
2. {'action': 'select', 'target': '#aws-skill-checkbox'}
3. {'action': 'select', 'target': '#javascript-skill-checkbox'}
**Expected Result:** Selected skills are displayed and skill list is updated

### Set Difficulty Level of Questions
**Steps:**
1. {'action': 'select', 'target': '#difficulty-level-select', 'value': 'Moderate'}
**Expected Result:** Difficulty level is set to Moderate

### Review and Customize Standard Questions
**Steps:**
1. {'action': 'click', 'target': '#standard-questions-list'}
2. {'action': 'check', 'target': '#notice-period-question-checkbox'}
3. {'action': 'fill', 'target': '#notice-period-question-answer-input', 'value': '30 days'}
**Expected Result:** Standard questions are displayed and preferred answer is set

### Review and Customize Role-Based Questions
**Steps:**
1. {'action': 'click', 'target': '#role-based-questions-list'}
2. {'action': 'check', 'target': '#aws-experience-question-checkbox'}
3. {'action': 'fill', 'target': '#aws-experience-question-answer-input', 'value': '2 years'}
**Expected Result:** Role-based questions are displayed and preferred answer is set

### Create Interview with AI Avatar (Advanced Plan)
**Steps:**
1. {'action': 'click', 'target': '#ai-avatar-select'}
2. {'action': 'select', 'target': '#ai-avatar-option', 'value': 'Avatar 1'}
**Expected Result:** AI avatar is selected and lip syncing alignment is enabled

### Create Interview
**Steps:**
1. {'action': 'click', 'target': '#create-interview-btn'}
**Expected Result:** Interview is created and unique public interview link is generated

### Candidate Video Interview Submission
**Steps:**
1. Navigate to the job posting page with a public link
2. Click on the 'Responses' tab
3. Verify the candidate's video interview is listed
4. Click on the candidate's video interview
5. Verify the video recording, structured answers, scores, and resume are displayed
**Expected Result:** The candidate's video interview details are displayed correctly

### Interview Screening and Scoring
**Steps:**
1. Navigate to the 'Interview Screenings' section
2. Verify the candidate's interview score is displayed
3. Verify the candidate's communication score is displayed
4. Verify the AI-generated summary of the interview is displayed, including observations, positives, and negatives
**Expected Result:** The candidate's interview scores and summary are displayed correctly

### Résumé Screening and Recommendation
**Steps:**
1. Create an interview and upload multiple résumés
2. Verify the AI commences the screening process
3. Verify the résumé score is displayed for each candidate
4. Verify the AI recommendation for each candidate is displayed
**Expected Result:** The AI provides a realistic assessment of the candidates' experience and recommends suitable profiles

### Candidate Advancement and Interview Link
**Steps:**
1. Decide to proceed with a candidate based on the AI recommendation
2. Verify the option to send an interview link to the candidate
3. Verify the interview link is valid for 24 hours
4. Verify the candidate can submit their interview at their convenience
**Expected Result:** The candidate can submit their interview successfully

### Initiating Interview Screening Process
**Steps:**
1. Verify the candidate has submitted their interview
2. Initiate the interview screening process
3. Verify the summary of the interview is displayed, including scores and AI analysis
**Expected Result:** The interview screening process is initiated successfully and the summary is displayed correctly

