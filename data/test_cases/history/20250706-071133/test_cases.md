### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'locator': '#job-description-input', 'value': 'JavaScript developer with AWS experience'}
2. {'action': 'click', 'locator': '#save-job-description-button'}
3. {'action': 'wait_for_selector', 'locator': '#skill-recommendations'}
**Expected Result:** Skill recommendations are displayed

### Select Skills and Difficulty Level
**Steps:**
1. {'action': 'click', 'locator': '#aws-skill-checkbox'}
2. {'action': 'select_option', 'locator': '#difficulty-level-select', 'value': 'Moderate'}
**Expected Result:** AWS skill is selected and difficulty level is set to Moderate

### Configure Standard Questions
**Steps:**
1. {'action': 'click', 'locator': '#standard-questions-tab'}
2. {'action': 'fill', 'locator': '#question-input', 'value': "What's the notice period?"}
3. {'action': 'check', 'locator': '#preferred-answer-checkbox'}
**Expected Result:** Standard question is configured with preferred answer

### Configure Role-Based Questions
**Steps:**
1. {'action': 'click', 'locator': '#role-based-questions-tab'}
2. {'action': 'fill', 'locator': '#role-based-question-input', 'value': "What's your experience with AWS?"}
3. {'action': 'check', 'locator': '#ideal-answer-checkbox'}
**Expected Result:** Role-based question is configured with ideal answer

### Create Interview
**Steps:**
1. {'action': 'click', 'locator': '#create-interview-button'}
2. {'action': 'wait_for_selector', 'locator': '#interview-link'}
**Expected Result:** Interview is created with unique public link

### Viewing candidate responses in the responses tab
**Steps:**
1. Navigate to the responses tab
2. Verify the candidate's video recording is playable
3. Verify the candidate's structured answers are displayed
4. Verify the candidate's scores and resume are displayed
**Expected Result:** All candidate responses are displayed correctly

### Viewing interview scores and summary
**Steps:**
1. Navigate to the interview screenings section
2. Verify the candidate's interview score is displayed
3. Verify the candidate's communication score is displayed
4. Verify the AI's comprehensive summary of the interview is displayed, including observations, positives, and negatives
**Expected Result:** All interview scores and summary are displayed correctly

### Rejecting or selecting a candidate
**Steps:**
1. Click the action button next to the candidate's response
2. Verify the option to select or reject the candidate is displayed
3. Click either the select or reject button
4. Verify the candidate's status is updated accordingly
**Expected Result:** Candidate status is updated correctly

### Screening resumes with AI
**Steps:**
1. Create an interview and upload multiple resumes
2. Verify the AI commences the screening process
3. Verify each resume is assigned a score based on skills and experience
4. Verify the AI recommends profiles for the next stage based on suitability
**Expected Result:** AI screens resumes correctly and recommends profiles

###  Sending interview link to candidate
**Steps:**
1. Decide to proceed with a candidate
2. Verify the option to send an interview link is displayed
3. Click the send interview link button
4. Verify the link is valid for 24 hours
**Expected Result:** Interview link is sent to candidate correctly

