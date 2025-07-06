### Test Create Interview with Job Description
**Steps:**
1. {'action': 'Fill input', 'target': 'Job Description input field', 'value': 'JavaScript developer with AWS experience'}
2. {'action': 'Click', 'target': 'Save Job Description button'}
**Expected Result:** Skill recommendations are displayed

### Test Enhanced JD Feature
**Steps:**
1. {'action': 'Click', 'target': 'Enhanced JD feature button'}
2. {'action': 'Fill input', 'target': 'Job Title input field', 'value': '2-year experienced JavaScript developer with AWS experience'}
3. {'action': 'Click', 'target': 'Generate Job Description button'}
**Expected Result:** Job description is generated and displayed

### Test Adding and Editing Skills
**Steps:**
1. {'action': 'Click', 'target': 'Add Skill button'}
2. {'action': 'Fill input', 'target': 'Skill input field', 'value': 'AWS experience'}
3. {'action': 'Click', 'target': 'Save Skill button'}
**Expected Result:** Added skill is displayed in the skill list

### Test Setting Difficulty Level of Questions
**Steps:**
1. {'action': 'Click', 'target': 'Difficulty Level dropdown'}
2. {'action': 'Select', 'target': 'Moderate difficulty level'}
**Expected Result:** Moderate difficulty level is selected

### Test Customizing Standard Questions
**Steps:**
1. {'action': 'Click', 'target': 'Edit Standard Question button'}
2. {'action': 'Fill input', 'target': 'Standard Question input field', 'value': "What's the notice period?"}
3. {'action': 'Click', 'target': 'Save Standard Question button'}
**Expected Result:** Customized standard question is displayed

### Test Creating Interview
**Steps:**
1. {'action': 'Click', 'target': 'Create Interview button'}
**Expected Result:** Interview is created and unique public interview link is displayed

### Verify Candidate Responses
**Steps:**
1. Visit the responses tab
2. Verify structured answers and video recordings are displayed
3. Verify scores and resumes are displayed
**Expected Result:** Candidate responses are displayed correctly

### Verify Interview Score and Communication Score
**Steps:**
1. Visit the interview screenings section
2. Verify interview score is displayed
3. Verify communication score is displayed
**Expected Result:** Interview score and communication score are displayed correctly

### Verify AI Summary
**Steps:**
1. Verify comprehensive summary of the interview is displayed
2. Verify observations, positives, and negatives are noted
**Expected Result:** AI summary is displayed correctly

### Verify Action Buttons
**Steps:**
1. Verify select and reject buttons are displayed
2. Verify buttons are clickable
**Expected Result:** Action buttons are displayed and functional

### Verify Ré Screening
**Steps:**
1. Create an interview and upload résumés
2. Verify AI commences screening process
3. Verify ré score is assigned
**Expected Result:** Ré screening process is initiated correctly

### Verify AI Recommendations
**Steps:**
1. Verify AI recommendations are displayed
2. Verify suitability of resume is considered
**Expected Result:** AI recommendations are displayed correctly

### Verify Sending Interview Link
**Steps:**
1. Verify interview link can be sent to candidate
2. Verify link is valid for 24 hours
**Expected Result:** Interview link is sent and valid

### Verify Interview Submission and Screening
**Steps:**
1. Verify candidate can submit interview
2. Verify interview screening process can be initiated
**Expected Result:** Interview submission and screening process is successful

