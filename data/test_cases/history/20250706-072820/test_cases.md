### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'target': 'job description input field', 'value': 'JavaScript Developer with 2 years of AWS experience'}
2. {'action': 'click', 'target': 'Save Job Description button'}
**Expected Result:** Job description is saved and skill recommendations are displayed

### Select Skill from Recommendations
**Steps:**
1. {'action': 'click', 'target': 'AWS skill recommendation'}
**Expected Result:** AWS skill is selected and displayed in the skill list

### Set Difficulty Level of Questions
**Steps:**
1. {'action': 'select', 'target': 'difficulty level dropdown', 'value': 'Moderate'}
**Expected Result:** Moderate difficulty level is set for the interview questions

### Generate Standard Questions
**Steps:**
1. {'action': 'click', 'target': 'Generate Questions button'}
**Expected Result:** Standard questions are generated and displayed, including 'What's the notice period?'

### Customize Standard Question
**Steps:**
1. {'action': 'check', 'target': "Preferred answer checkbox for 'What's the notice period?' question"}
**Expected Result:** Preferred answer is set for the 'What's the notice period?' question

### Generate Role-Based Questions
**Steps:**
1. {'action': 'click', 'target': 'Generate Questions button'}
**Expected Result:** Role-based questions are generated and displayed, with ideal answers

### Create Interview
**Steps:**
1. {'action': 'click', 'target': 'Create Interview button'}
**Expected Result:** Interview is created and unique public interview link is displayed

### Test Candidate Video Interview Response
**Steps:**
1. Visit the public link and navigate to the responses tab
2. Click on a candidate's response to view structured answers and video recordings
**Expected Result:** Candidate's video interview response is displayed with scores and resumes

### Test Interview Score and Communication Score
**Steps:**
1. Visit the responses tab and select a candidate's response
2. Check the interview score and communication score
**Expected Result:** Interview score and communication score are displayed correctly

### Test AI Comprehensive Summary
**Steps:**
1. Visit the responses tab and select a candidate's response
2. Check the AI comprehensive summary including observations, positives, and negatives
**Expected Result:** AI comprehensive summary is displayed correctly

### Test Action Buttons (Select/Reject Candidate)
**Steps:**
1. Visit the responses tab and select a candidate's response
2. Click on the action button to select or reject the candidate
**Expected Result:** Action buttons (select/reject) are functional and update candidate status correctly

### Test Ré Screening
**Steps:**
1. Create an interview and upload multiple résumés
2. Submit the résumés for AI screening
**Expected Result:** AI commences the screening process and assigns a ré score to each candidate

### Test Ré Score and AI Recommendation
**Steps:**
1. Visit the ré screening results
2. Check the ré score and AI recommendation for each candidate
**Expected Result:** Ré score and AI recommendation are displayed correctly, considering skills and job description alignment

### Test Send Interview Link to Candidate
**Steps:**
1. Select a candidate from the ré screening results
2. Send an interview link to the candidate
**Expected Result:** Interview link is sent successfully to the candidate, valid for 24 hours

### Test Interview Screening Process
**Steps:**
1. Wait for the candidate to submit their interview
2. Initiate the interview screening process
**Expected Result:** Interview screening process is initiated successfully, displaying the AI summary

