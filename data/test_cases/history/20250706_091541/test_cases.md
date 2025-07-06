### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'target': "input[name='jobDescription']", 'value': 'JavaScript developer with 2 years of AWS experience'}
2. {'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** AI suggests questions based on job description

### Customize Questions
**Steps:**
1. {'action': 'click', 'target': "button[data-test='edit-question']"}
2. {'action': 'fill', 'target': "input[name='customQuestion']", 'value': 'What is your experience with AWS?'}
3. {'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** Customized question is saved

### Select AI Avatar (Advanced Plan)
**Steps:**
1. {'action': 'click', 'target': "button[data-test='select-ai-avatar']"}
2. {'action': 'select', 'target': "select[name='aiAvatar']", 'option': 'Lip Syncing Avatar'}
**Expected Result:** AI avatar is selected

### Choose Skills from AI Suggestions
**Steps:**
1. {'action': 'click', 'target': "checkbox[name='skill-aws']"}
2. {'action': 'click', 'target': "checkbox[name='skill-javascript']"}
**Expected Result:** Selected skills are saved

### Set Difficulty Level of Questions
**Steps:**
1. {'action': 'select', 'target': "select[name='question-difficulty']", 'option': 'Moderate'}
**Expected Result:** Difficulty level of questions is set to Moderate

### Create Interview
**Steps:**
1. {'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** Interview is created and public interview link is generated

### Candidate Response Tab
**Steps:**
1. Visit the public link for the job posting
2. Verify the responses tab is visible
3. Click on the responses tab
4. Verify structured answers, video recordings, scores, and resumes are displayed
**Expected Result:** The responses tab displays the candidate's responses, scores, and resumes

### Interview Screening Section
**Steps:**
1. Visit the interview screenings section
2. Verify AI analyze scores are displayed
3. Verify the candidate's skills versus scores are displayed
**Expected Result:** The interview screenings section displays AI analyze scores and candidate's skills versus scores

### Candidate Score
**Steps:**
1. Visit the interview screenings section
2. Verify the candidate's interview score is displayed
3. Verify the candidate's communication score is displayed
**Expected Result:** The candidate's interview score and communication score are displayed

### AI Interview Summary
**Steps:**
1. Visit the interview screenings section
2. Verify the AI provides a comprehensive summary of the interview
3. Verify observations, positives, and negatives are noted in the summary
**Expected Result:** The AI provides a comprehensive summary of the interview with observations, positives, and negatives

### Action Button
**Steps:**
1. Visit the interview screenings section
2. Verify an action button to select or reject the candidate is displayed
3. Click on the action button and verify the corresponding action is taken
**Expected Result:** The action button allows the user to select or reject the candidate

### Ré Screening
**Steps:**
1. Create an interview and upload resumes
2. Verify the AI commences the screening process
3. Verify the system conducts a comprehensive semantic analysis and assigns a ré score
**Expected Result:** The AI screens the resumes and assigns a ré score based on skills and experience

### Ré Score and Recommendation
**Steps:**
1. Verify the ré score is displayed for each candidate
2. Verify the AI provides a recommendation for each candidate based on the ré score and job requirements
**Expected Result:** The ré score and AI recommendation are displayed for each candidate

### Interview Invitation
**Steps:**
1. Decide to proceed with a candidate
2. Verify an interview link can be sent to the candidate
3. Verify the interview link is valid for 24 hours
**Expected Result:** The candidate receives an interview link that is valid for 24 hours

