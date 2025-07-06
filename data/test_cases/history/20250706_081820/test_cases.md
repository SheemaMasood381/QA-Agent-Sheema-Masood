### Create Interview with Job Description
**Steps:**
1. {'action': 'Enter job description', 'input': {'jobDescription': 'JavaScript developer with 2 years of experience and AWS knowledge'}}
2. {'action': 'Click on Save Job Description', 'wait_for': 'networkidle2'}
**Expected Result:** Skill recommendations are displayed

### Select Skills from AI Recommendations
**Steps:**
1. {'action': 'Select skills from AI recommendations', 'input': {'skills': ['JavaScript', 'AWS']}}
**Expected Result:** Selected skills are displayed

### Set Difficulty Level of Questions
**Steps:**
1. {'action': 'Select difficulty level of questions', 'input': {'difficulty': 'Moderate'}}
**Expected Result:** Difficulty level is set to Moderate

### View Standard and Role-Based Questions
**Steps:**
1. {'action': 'View standard and role-based questions', 'wait_for': 'networkidle2'}
**Expected Result:** Standard and role-based questions are displayed

### Customize Standard Questions
**Steps:**
1. {'action': 'Edit standard question', 'input': {'question': "What's the notice period?", 'preferredAnswer': '2 weeks'}}
**Expected Result:** Standard question is customized

### Create Interview
**Steps:**
1. {'action': 'Click on Create Interview', 'wait_for': 'networkidle2'}
**Expected Result:** Interview is created and unique public interview link is displayed

### Advanced Plan: Select AI Avatar
**Steps:**
1. {'action': 'Select AI avatar', 'input': {'avatar': 'AI Avatar 1'}}
**Expected Result:** AI avatar is selected

### View Candidate Responses
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
**Expected Result:** Fully view structured answers, video recordings, scores, and resumes for the candidate

### Verify Interview Score
**Steps:**
1. Visit the interview screenings section
2. Click on the candidate's interview
**Expected Result:** Display the candidate's interview score

### Verify Communication Score
**Steps:**
1. Visit the interview screenings section
2. Click on the candidate's interview
**Expected Result:** Display the candidate's communication score

### View AI Summary
**Steps:**
1. Visit the interview screenings section
2. Click on the candidate's interview
**Expected Result:** Display a comprehensive summary of the interview, including observations, positives, and negatives

### Reject or Select Candidate
**Steps:**
1. Visit the interview screenings section
2. Click on the candidate's interview
3. Click on the action button
**Expected Result:** Option to select or reject the candidate appears

### Resume Screening
**Steps:**
1. Create an interview
2. Upload resumes
3. Submit for AI screening
**Expected Result:** AI conducts semantic analysis and assigns a resume score

### View AI Recommendation
**Steps:**
1. View the resume screening results
2. Check the AI recommendation for the candidate
**Expected Result:** Display the AI's recommendation for the candidate, considering skills and experience alignment with the job description

### Send Interview Link
**Steps:**
1. Decide to proceed with a candidate
2. Send an interview link to the candidate
**Expected Result:** Candidate receives an interview link, valid for 24 hours

### Initiate Interview Screening
**Steps:**
1. Wait for candidate to submit their interview
2. Initiate the interview screening process
**Expected Result:** Ability to review the candidate's interview summary and scores

