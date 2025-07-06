### Create Interview - Validate Job Description Input
**Steps:**
1. {'action': 'navigate', 'target': 'https://example.com/create-interview'}
2. {'action': 'fill', 'target': 'input[name=jobDescription]', 'value': 'JavaScript developer with AWS experience'}
**Expected Result:** Job description input field is populated

### Create Interview - Verify Enhanced JD Feature
**Steps:**
1. {'action': 'click', 'target': "button[aria-label='Use Enhanced JD feature']"}
2. {'action': 'wait_for_load_state', 'target': 'networkidle2'}
**Expected Result:** Enhanced JD feature is enabled and job description is generated

### Create Interview - Validate Skill Recommendations
**Steps:**
1. {'action': 'wait_for_selector', 'target': 'div.skill-recommendations'}
2. {'action': 'get_text', 'target': 'div.skill-recommendations'}
**Expected Result:** Skill recommendations are displayed based on job description

### Create Interview - Add Custom Skill
**Steps:**
1. {'action': 'fill', 'target': 'input[name=add-skill]', 'value': 'Cloud Computing'}
2. {'action': 'click', 'target': "button[aria-label='Add Skill']"}
**Expected Result:** Custom skill is added to the skill recommendations list

### Create Interview - Validate Question Categories
**Steps:**
1. {'action': 'wait_for_selector', 'target': 'div.question-categories'}
2. {'action': 'get_text', 'target': 'div.question-categories'}
**Expected Result:** Standard and Role-based question categories are displayed

### Create Interview - Validate Standard Questions
**Steps:**
1. {'action': 'wait_for_selector', 'target': 'div.standard-questions'}
2. {'action': 'get_text', 'target': 'div.standard-questions'}
**Expected Result:** Standard questions are displayed with options to personalize

### Create Interview - Validate Role-based Questions
**Steps:**
1. {'action': 'wait_for_selector', 'target': 'div.role-based-questions'}
2. {'action': 'get_text', 'target': 'div.role-based-questions'}
**Expected Result:** Role-based questions are displayed with options to personalize

### Create Interview - Validate Create Option
**Steps:**
1. {'action': 'click', 'target': "button[aria-label='Create Interview']"}
**Expected Result:** Interview is created successfully and unique public interview link is generated

###  Candidate Video Interview Response
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
3. Verify the video recording is available
4. Verify the structured answers are available
5. Verify the scores and resume are available
**Expected Result:** The candidate's video interview response is displayed with scores, resume, and structured answers

### Candidate Interview Score and Communication Score
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
3. Verify the interview score is displayed
4. Verify the communication score is displayed
**Expected Result:** The interview score and communication score are displayed for the candidate

### AI Analysis and Summary
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
3. Verify the AI analysis summary is displayed
4. Verify the summary includes observations, positives, and negatives
**Expected Result:** The AI analysis summary is displayed with observations, positives, and negatives

### Select or Reject Candidate
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
3. Verify the action buttons 'Select' and 'Reject' are available
4. Click on the 'Select' or 'Reject' button
5. Verify the candidate's status is updated accordingly
**Expected Result:** The candidate's status is updated successfully

### Resume Screening
**Steps:**
1. Create an interview and upload multiple resumes
2. Verify the AI commences the screening process
3. Verify the resume scores are displayed
4. Verify the AI recommendations are displayed
**Expected Result:** The resume screening process is successful and AI recommendations are displayed

### Resume Score and Recommendation
**Steps:**
1. Create an interview and upload multiple resumes
2. Verify the resume scores are displayed
3. Verify the AI recommendation is displayed for each resume
4. Verify the recommendation considers the candidate's experience and job requirements
**Expected Result:** The resume score and AI recommendation are accurate and consider the candidate's experience and job requirements

### Send Interview Link to Candidate
**Steps:**
1. Decide to proceed with a candidate
2. Verify the option to send an interview link is available
3. Send the interview link to the candidate
4. Verify the interview link is valid for 24 hours
**Expected Result:** The interview link is sent to the candidate successfully and is valid for 24 hours

### Initiate Interview Screening Process
**Steps:**
1. Candidate submits their interview
2. Verify the option to initiate the interview screening process is available
3. Initiate the interview screening process
4. Verify the AI analysis summary is displayed
**Expected Result:** The interview screening process is initiated successfully and the AI analysis summary is displayed

