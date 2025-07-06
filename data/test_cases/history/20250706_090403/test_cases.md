### Create Interview - Enter Job Description
**Steps:**
1. {'step': 'Enter job description', 'input': 'JavaScript developer with AWS experience'}
2. {'step': 'Click Save'}
**Expected Result:** Skill recommendations are displayed

### Create Interview - Select Skills
**Steps:**
1. {'step': 'Select skills from AI recommendations', 'input': ['JavaScript', 'AWS']}
2. {'step': 'Add custom skill', 'input': '2 years of experience in AWS'}
**Expected Result:** Skills are saved and difficulty level options are displayed

### Create Interview - Set Difficulty Level
**Steps:**
1. {'step': 'Select difficulty level', 'input': 'Moderate'}
**Expected Result:** Difficulty level is saved

### Create Interview - Review Questions
**Steps:**
1. {'step': 'Review standard questions', 'input': ''}
2. {'step': 'Review role-based questions', 'input': ''}
3. {'step': 'Edit a question', 'input': "What's the notice period?"}
4. {'step': 'Set preferred answer', 'input': '30 days'}
**Expected Result:** Questions are updated

### Create Interview - Create Interview
**Steps:**
1. {'step': 'Click Create Interview'}
**Expected Result:** Unique public interview link is generated

### Create Interview - Advanced Plan - Select AI Avatar
**Steps:**
1. {'step': 'Select AI avatar', 'input': 'Lip syncing avatar'}
**Expected Result:** AI avatar is selected and lip syncing is enabled

### Test Candidate Video Interview
**Steps:**
1. Navigate to the responses tab
2. Click on the candidate's video interview
3. Verify the candidate's skills versus scores are displayed
**Expected Result:** The candidate's interview score and communication score are displayed

### Test Candidate Scoring Summary
**Steps:**
1. Navigate to the interview screenings section
2. Click on the AI analyze scores section
3. Verify the comprehensive summary of the interview is displayed
**Expected Result:** The summary includes observations, positives, and negatives, and an action button to select or reject the candidate

### Test Resume Screening
**Steps:**
1. Navigate to the resume screening section
2. Upload multiple resumes
3. Verify the AI commences the screening process
**Expected Result:** The AI evaluates candidates based on their skills and assigns a resume score

### Test Resume Score Recommendations
**Steps:**
1. Navigate to the resume screening section
2. Verify the AI recommends suitable candidates based on the job description
**Expected Result:** The AI recommends candidates with resumes that align with the job requirements

### Test Interview Invitation
**Steps:**
1. Navigate to the resume screening section
2. Click on the 'Send interview link' button
3. Verify the candidate receives an interview link valid for 24 hours
**Expected Result:** The candidate can submit their interview at their convenience

### Test Interview Screening Process
**Steps:**
1. Navigate to the interview screening section
2. Verify the candidate's interview is displayed
3. Click on the 'Initiate interview screening' button
**Expected Result:** The interview screening process is initiated, and the summary is displayed

