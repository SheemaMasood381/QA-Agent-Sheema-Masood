### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'target': "input[name='jobDescription']", 'value': 'JavaScript developer with AWS experience'}
2. {'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** AI suggests questions based on the job description

### Use Enhanced JD Feature
**Steps:**
1. {'action': 'fill', 'target': "input[name='jobTitle']", 'value': 'JavaScript developer with AWS experience'}
2. {'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** AI generates a complete job description

### Save Job Description and View Skill Recommendations
**Steps:**
1. {'action': 'fill', 'target': "input[name='jobDescription']", 'value': 'JavaScript developer with AWS experience'}
2. {'action': 'click', 'target': "button[type='save']"}
**Expected Result:** Skill recommendations are displayed based on the job description

### Select Skills and Set Difficulty Level
**Steps:**
1. {'action': 'select', 'target': "select[name='skills']", 'value': 'AWS'}
2. {'action': 'select', 'target': "select[name='difficultyLevel']", 'value': 'Moderate'}
**Expected Result:** Selected skills and difficulty level are saved

### View Standard and Role-Based Questions
**Steps:**
1. {'action': 'wait', 'target': "section[role='questions']"}
**Expected Result:** Standard and role-based questions are displayed

### Add and Customize Questions
**Steps:**
1. {'action': 'click', 'target': "button[type='addQuestion']"}
2. {'action': 'fill', 'target': "input[name='question']", 'value': "What's your experience with AWS?"}
3. {'action': 'click', 'target': "button[type='saveQuestion']"}
**Expected Result:** Customized question is added to the list

### Create Interview
**Steps:**
1. {'action': 'click', 'target': "button[type='createInterview']"}
**Expected Result:** Interview is created with a unique public link

### View Candidate Responses
**Steps:**
1. Visit the public link
2. Navigate to the responses tab
**Expected Result:** View structured answers, video recordings, scores, and resumes of candidates

### Check Interview Score
**Steps:**
1. Select a candidate who has completed a video interview
2. View interview score
**Expected Result:** A numerical score indicating the candidate's performance in the interview

### Check Communication Score
**Steps:**
1. Select a candidate who has completed a video interview
2. View communication score
**Expected Result:** A numerical score indicating the candidate's communication skills

### View Interview Summary
**Steps:**
1. Select a candidate who has completed a video interview
2. View interview summary
**Expected Result:** A comprehensive summary of the interview, including observations, positives, and negatives

### Take Action on Candidate
**Steps:**
1. Select a candidate who has completed a video interview
2. Click the action button
**Expected Result:** Option to either select or reject the candidate

### Ré Screening
**Steps:**
1. Create an interview
2. Upload résumés
3. Submit for screening
**Expected Result:** AI commences screening process, evaluating candidates based on skills and experience

### View Ré Score
**Steps:**
1. View ré screening results
2. Check ré score
**Expected Result:** A numerical score indicating the candidate's suitability for the job description

### View AI Recommendation
**Steps:**
1. View ré screening results
2. Check AI recommendation
**Expected Result:** AI recommends or rejects the candidate for the next stage

### Send Interview Link
**Steps:**
1. Decide to proceed with a candidate
2. Send interview link to the candidate
**Expected Result:** Candidate receives interview link valid for 24 hours

### Initiate Interview Screening
**Steps:**
1. Candidate submits their interview
2. Initiate the interview screening process
**Expected Result:** Ability to review the interview summary and start the screening process

