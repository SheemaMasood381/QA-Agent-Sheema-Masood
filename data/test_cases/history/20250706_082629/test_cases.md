### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'locator': "input[name='jobDescription']", 'value': 'JavaScript Developer with AWS experience'}
2. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** AI suggests questions based on the job description

### Create Interview with Enhanced JD Feature
**Steps:**
1. {'action': 'fill', 'locator': "input[name='jobTitle']", 'value': 'JavaScript Developer with AWS experience'}
2. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** AI generates a complete job description

### Edit and Save Job Description
**Steps:**
1. {'action': 'fill', 'locator': "textarea[name='jobDescription']", 'value': 'Edited job description'}
2. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** Job description is saved and skill recommendations are displayed

### Select Skills from AI Suggestions
**Steps:**
1. {'action': 'check', 'locator': "input[name='skill-aws']"}
**Expected Result:** Selected skills are displayed

### Add Custom Skills
**Steps:**
1. {'action': 'fill', 'locator': "input[name='newSkill']", 'value': 'JavaScript'}
2. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** Custom skill is added to the list

### Set Difficulty Level of Questions
**Steps:**
1. {'action': 'select', 'locator': "select[name='difficulty']", 'value': 'Moderate'}
**Expected Result:** Difficulty level of questions is set

### View Standard Questions
**Steps:**
1. {'action': 'click', 'locator': "a[href='#standard-questions']"}
**Expected Result:** Standard questions are displayed

### View Role-Based Questions
**Steps:**
1. {'action': 'click', 'locator': "a[href='#role-based-questions']"}
**Expected Result:** Role-based questions are displayed

### Create Interview with Custom Questions
**Steps:**
1. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** Interview is created with custom questions

### View Public Interview Link
**Steps:**
1. {'action': 'expect', 'locator': "a[href*='unique-interview-link']"}
**Expected Result:** Public interview link is displayed

### Public link sharing and responses tab
**Steps:**
1. Visit the public link
2. Go to the responses tab
**Expected Result:** View structured answers, video recordings, scores, and resumes of candidates

### Interview score and communication score
**Steps:**
1. Select a candidate who has completed a video interview
2. View the candidate's skills versus scores
**Expected Result:** Display interview score and communication score for the selected candidate

### Comprehensive summary of the interview
**Steps:**
1. Select a candidate who has completed a video interview
2. View the comprehensive summary of the interview
**Expected Result:** Display observations, positives, and negatives of the interview

### Action button to select or reject candidates
**Steps:**
1. Select a candidate who has completed a video interview
2. Click the action button
**Expected Result:** Display options to select or reject the candidate

### Ré screening and AI analysis
**Steps:**
1. Create an interview and upload multiple résumés
2. View the AI analysis and ré scores
**Expected Result:** Display AI analysis and ré scores for each uploaded résumé

### Ré score and AI recommendation
**Steps:**
1. View the ré score and AI recommendation for a candidate
2. Verify the recommendation
**Expected Result:** Display AI recommendation based on the candidate's skills and experience

### Sending interview link to candidates
**Steps:**
1. Select a candidate to proceed to the next round
2. Send the interview link to the candidate
**Expected Result:** Candidate receives the interview link and can submit their interview at their convenience

### Initiating interview screening process
**Steps:**
1. Candidate submits their interview
2. Initiate the interview screening process
**Expected Result:** Display comprehensive summary of the interview, including observations, positives, and negatives

