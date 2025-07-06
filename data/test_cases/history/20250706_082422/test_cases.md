### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'target': 'Job Description input field', 'data': 'JavaScript developer with AWS experience'}
2. {'action': 'click', 'target': 'Save Job Description button'}
3. {'action': 'wait_for', 'target': 'Skill recommendations section'}
**Expected Result:** Skill recommendations section is displayed with key skills extracted from the job description

### Select Skills and Difficulty Level
**Steps:**
1. {'action': 'select', 'target': 'Skill checkbox (e.g. AWS experience)', 'data': 'true'}
2. {'action': 'select', 'target': 'Difficulty level dropdown', 'data': 'Moderate'}
**Expected Result:** Selected skills and difficulty level are saved successfully

### View and Customize Interview Questions
**Steps:**
1. {'action': 'wait_for', 'target': 'Interview questions section'}
2. {'action': 'click', 'target': "Standard question (e.g. 'What's the notice period?')"}
3. {'action': 'fill', 'target': 'Preferred answer input field', 'data': '30 days'}
**Expected Result:** Standard question with preferred answer is displayed and editable

### Create Interview with Selected Questions
**Steps:**
1. {'action': 'click', 'target': 'Create Interview button'}
**Expected Result:** Interview is created successfully with a unique public interview link

### Verify candidate's interview score and communication score
**Steps:**
1. Visit the responses tab
2. Click on a candidate's video interview
3. Verify the interview score is displayed
4. Verify the communication score is displayed
**Expected Result:** Interview score and communication score are displayed correctly

### Verify comprehensive summary of the interview
**Steps:**
1. Visit the responses tab
2. Click on a candidate's video interview
3. Verify the comprehensive summary of the interview is displayed
4. Verify the summary includes observations, positives, and negatives
**Expected Result:** Comprehensive summary of the interview is displayed correctly

### Verify action buttons to select or reject a candidate
**Steps:**
1. Visit the responses tab
2. Click on a candidate's video interview
3. Verify the 'Select' and 'Reject' action buttons are displayed
**Expected Result:** Action buttons to select or reject a candidate are displayed

### Verify ré screening functionality
**Steps:**
1. Create an interview and upload a set of résumés
2. Verify the AI commences the screening process
3. Verify the ré score is displayed for each candidate
4. Verify the system recommends profiles for the next stage based on suitability
**Expected Result:** Ré screening functionality works as expected

### Verify AI recommendations
**Steps:**
1. Upload a set of résumés for ré screening
2. Verify the AI recommends profiles for the next stage based on suitability
3. Verify the recommendation is based on skills and experience alignment with the job description
**Expected Result:** AI recommendations are accurate and based on skills and experience alignment

### Verify interview link sending functionality
**Steps:**
1. Decide to proceed with a candidate
2. Verify the option to send an interview link is available
3. Verify the interview link is sent to the candidate and can be submitted within 24 hours
**Expected Result:** Interview link sending functionality works as expected

