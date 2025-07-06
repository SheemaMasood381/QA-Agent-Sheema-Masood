### Create Interview: Enter Job Description
**Steps:**
1. {'action': 'fill', 'target': "input[name='jobDescription']", 'value': 'JavaScript developer with AWS experience'}
**Expected Result:** AI suggests questions based on the job description

### Create Interview: Use Enhanced JD Feature
**Steps:**
1. {'action': 'click', 'target': "button[data-test-id='enhanced-jd-feature']"}
2. {'action': 'fill', 'target': "input[name='jobTitle']", 'value': '2-year experienced JavaScript developer with AWS experience'}
**Expected Result:** AI generates a complete job description

### Create Interview: Save Job Description
**Steps:**
1. {'action': 'click', 'target': "button[data-test-id='save-job-description']"}
**Expected Result:** Skill recommendations are displayed

### Create Interview: Select Skills
**Steps:**
1. {'action': 'click', 'target': "checkbox[name='skills'][value='AWS']"}
2. {'action': 'click', 'target': "checkbox[name='skills'][value='JavaScript']"}
**Expected Result:** Selected skills are displayed

### Create Interview: Set Difficulty Level
**Steps:**
1. {'action': 'select', 'target': "select[name='difficultyLevel']", 'value': 'moderate'}
**Expected Result:** Difficulty level is set to moderate

### Create Interview: Standard Questions
**Steps:**
1. {'action': 'click', 'target': "button[data-test-id='add-standard-question']"}
2. {'action': 'fill', 'target': "input[name='standardQuestion']", 'value': "What's the notice period?"}
**Expected Result:** Standard question is added

### Create Interview: Role-Based Questions
**Steps:**
1. {'action': 'click', 'target': "button[data-test-id='add-role-based-question']"}
2. {'action': 'fill', 'target': "input[name='roleBasedQuestion']", 'value': 'How do you handle deployment with AWS?'}
**Expected Result:** Role-based question is added

### Create Interview: Create Interview
**Steps:**
1. {'action': 'click', 'target': "button[data-test-id='create-interview']"}
**Expected Result:** Interview is created and unique public interview link is displayed

###  Candidate Video Interview Response
**Steps:**
1. Visit the responses tab
2. Click on a candidate's video interview response
**Expected Result:** The candidate's structured answers, video recordings, scores, and resume are displayed

### View Interview Score and Communication Score
**Steps:**
1. Visit the responses tab
2. Click on a candidate's video interview response
3. View the interview score and communication score
**Expected Result:** The interview score and communication score are displayed

### View Comprehensive Summary of Interview
**Steps:**
1. Visit the responses tab
2. Click on a candidate's video interview response
3. View the comprehensive summary of the interview
**Expected Result:** The comprehensive summary includes observations, positives, and negatives

### Select or Reject Candidate
**Steps:**
1. Visit the responses tab
2. Click on a candidate's video interview response
3. Click on the action button to select or reject the candidate
**Expected Result:** The candidate is selected or rejected successfully

### Ré Screening - Create Interview and Upload Résumés
**Steps:**
1. Create a new interview
2. Upload multiple résumés
**Expected Result:** The AI commences the screening process

### View Ré Score and AI Recommendation
**Steps:**
1. Visit the ré screening section
2. View the ré score and AI recommendation for a candidate
**Expected Result:** The ré score and AI recommendation are displayed

### Decide to Reject or Advance Candidate
**Steps:**
1. Visit the ré screening section
2. View the ré score and AI recommendation for a candidate
3. Decide to reject or advance the candidate
**Expected Result:** The candidate is rejected or advanced to the next round successfully

### Send Interview Link to Candidate
**Steps:**
1. Decide to advance a candidate
2. Send an interview link to the candidate
**Expected Result:** The interview link is sent to the candidate successfully

### Review Interview Summary
**Steps:**
1. Candidate submits their interview
2. Initiate the interview screening process
3. View the summary of the interview
**Expected Result:** The interview summary is displayed with observations, positives, and negatives

