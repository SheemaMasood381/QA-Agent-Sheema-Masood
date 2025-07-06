### Create Interview with Job Description
**Steps:**
1. {'step': 'Enter job description', 'input': 'JavaScript developer with AWS experience', 'element': '#job-description-input'}
2. {'step': 'Save job description', 'element': '#save-job-description-button'}
3. {'step': 'Verify skill recommendations', 'expected': 'Key skills extracted from the job description'}
**Expected Result:** Job description saved and skill recommendations displayed

### Select Skills and Set Difficulty Level
**Steps:**
1. {'step': 'Choose skills from AI suggestions', 'input': 'AWS, JavaScript', 'element': '#skills-list'}
2. {'step': 'Set difficulty level', 'input': 'Moderate', 'element': '#difficulty-level-select'}
**Expected Result:** Skills and difficulty level saved

### Review and Customize Questions
**Steps:**
1. {'step': 'Review standard questions', 'expected': 'Standard questions displayed'}
2. {'step': 'Review role-based questions', 'expected': 'Role-based questions displayed'}
3. {'step': 'Personalize question options', 'input': 'Preferred answer', 'element': '#question-options'}
**Expected Result:** Questions reviewed and customized

### Create Interview and Get Public Link
**Steps:**
1. {'step': 'Click create interview', 'element': '#create-interview-button'}
**Expected Result:** Interview created and public link displayed

### Verify Public Interview Link
**Steps:**
1. {'step': 'Verify public interview link', 'expected': 'Unique public interview link displayed'}
**Expected Result:** Public interview link is valid and functional

### Test Advanced Plan Feature (AI Avatar)
**Steps:**
1. {'step': 'Select AI avatar', 'element': '#ai-avatar-select'}
**Expected Result:** AI avatar selected and lip syncing aligned with script

### View candidate responses
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
**Expected Result:** Display structured answers, video recordings, scores, and resumes

### View interview scores
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
3. View the interview score
**Expected Result:** Display the candidate's interview score

### View communication score
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
3. View the communication score
**Expected Result:** Display the candidate's communication score

### View AI analysis summary
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
3. View the AI analysis summary
**Expected Result:** Display a comprehensive summary of the interview, including observations, positives, and negatives

### Reject or select candidate
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
3. Click the action button
4. Choose to either select or reject the candidate
**Expected Result:** Display the selected or rejected status of the candidate

### Resume screening
**Steps:**
1. Create an interview
2. Upload resumes
3. Submit for AI screening
**Expected Result:** AI commences screening process and assigns a resume score

### View AI recommendations
**Steps:**
1. Visit the resume screening results
2. View the AI recommendations
**Expected Result:** Display AI recommendations for each candidate, including suitability and resume score

### Send interview link to candidate
**Steps:**
1. Visit the resume screening results
2. Choose to proceed with a candidate
3. Send an interview link to the candidate
**Expected Result:** Candidate receives an interview link valid for 24 hours

### View candidate interview submission
**Steps:**
1. Wait for candidate to submit interview
2. Visit the responses tab
**Expected Result:** Display the candidate's submitted interview

### Initiate interview screening
**Steps:**
1. Visit the responses tab
2. Click on the candidate's submitted interview
3. Initiate interview screening
**Expected Result:** Display the interview screening results, including scores and summary

