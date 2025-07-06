### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'target': "input[name='jobDescription']", 'value': 'Looking for a 2-year experienced JavaScript developer with AWS experience'}
2. {'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** AI suggests questions based on the job description

### Customize Questions and Establish Interview
**Steps:**
1. {'action': 'check', 'target': "checkbox[name='question1']"}
2. {'action': 'click', 'target': "button[id='editQuestion']"}
3. {'action': 'fill', 'target': "input[name='question1']", 'value': "What's the notice period?"}
4. {'action': 'click', 'target': "button[id='saveQuestion']"}
5. {'action': 'click', 'target': "button[id='createInterview']"}
**Expected Result:** Interview is created with customized questions

### Verify Public Interview Link
**Steps:**
1. {'action': 'wait_forSelector', 'target': "a[id='publicInterviewLink']"}
2. {'action': 'get_attribute', 'target': "a[id='publicInterviewLink']", 'attribute': 'href'}
**Expected Result:** Unique public interview link is generated

### Verify AI-driven Resume Screening and Video Interview
**Steps:**
1. {'action': 'fill', 'target': "input[name='candidateEmail']", 'value': 'candidate@example.com'}
2. {'action': 'click', 'target': "button[type='submit']"}
3. {'action': 'wait_forSelector', 'target': "div[id='resumeScreeningResult']"}
4. {'action': 'get_text', 'target': "div[id='videoInterviewStatus']"}
**Expected Result:** AI-driven resume screening and video interview are successfully executed

### View Candidate Responses
**Steps:**
1. Visit the responses tab
2. Verify that structured answers and video recordings are displayed
3. Verify that scores and resumes are displayed
**Expected Result:** Candidate responses are displayed with scores and resumes

### View Interview Score and Communication Score
**Steps:**
1. Visit the responses tab
2. Click on a candidate's video interview
3. Verify that interview score and communication score are displayed
**Expected Result:** Interview score and communication score are displayed for the candidate

### View AI Analyze Scores
**Steps:**
1. Visit the interview screenings section
2. Verify that AI analyze scores are displayed
**Expected Result:** AI analyze scores are displayed for the candidate

### View Comprehensive Summary of Interview
**Steps:**
1. Visit the responses tab
2. Click on a candidate's video interview
3. Verify that a comprehensive summary of the interview is displayed, including observations, positives, and negatives
**Expected Result:** Comprehensive summary of the interview is displayed with observations, positives, and negatives

### Use Action Button to Select or Reject Candidate
**Steps:**
1. Visit the responses tab
2. Click on a candidate's video interview
3. Verify that an action button is displayed to select or reject the candidate
**Expected Result:** Action button is displayed to select or reject the candidate

### Use Ré Screening to Evaluate Candidates
**Steps:**
1. Create an interview and upload a set of résumés
2. Verify that the AI commences the screening process
3. Verify that ré scores are assigned based on skills and experience
**Expected Result:** Ré screening process evaluates candidates based on skills and experience, and assigns ré scores

### View AI Recommendations for Candidates
**Steps:**
1. Visit the ré screening section
2. Verify that AI recommendations are displayed for each candidate
3. Verify that recommendations are based on suitability of the resume and skills alignment with the job description
**Expected Result:** AI recommendations are displayed for each candidate, based on suitability of the resume and skills alignment with the job description

### Send Interview Link to Candidate
**Steps:**
1. Decide to proceed with a candidate
2. Verify that an interview link is sent to the candidate, valid for 24 hours
**Expected Result:** Interview link is sent to the candidate, valid for 24 hours

### Initiate Interview Screening Process
**Steps:**
1. Candidate submits their interview
2. Verify that the interview screening process can be initiated
3. Verify that a comprehensive summary of the interview is displayed
**Expected Result:** Interview screening process is initiated, and a comprehensive summary of the interview is displayed

