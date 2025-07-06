### Create Interview - Job Description Step
**Steps:**
1. {'action': 'fill', 'target': "[name='jobDescription']", 'value': 'JavaScript developer with 2 years of experience and AWS expertise'}
2. {'action': 'click', 'target': "[type='submit']"}
**Expected Result:** Skill recommendations are displayed

### Create Interview - Skill Selection Step
**Steps:**
1. {'action': 'selectOption', 'target': "[name='skills']", 'option': 'AWS'}
2. {'action': 'selectOption', 'target': "[name='skills']", 'option': 'JavaScript'}
3. {'action': 'selectOption', 'target': "[name='difficultyLevel']", 'option': 'Moderate'}
**Expected Result:** Questions are generated based on selected skills

### Create Interview - Standard Questions Step
**Steps:**
1. {'action': 'waitForSelector', 'target': "[data-test='standard-questions']"}
2. {'action': 'check', 'target': "[data-test='preferred-answer-checkbox']"}
3. {'action': 'addCustomQuestion', 'target': "[data-test='add-custom-question-button']", 'question': 'What is your experience with AWS?'}
**Expected Result:** Custom question is added to standard questions

### Create Interview - Role-Based Questions Step
**Steps:**
1. {'action': 'waitForSelector', 'target': "[data-test='role-based-questions']"}
2. {'action': 'modifyQuestion', 'target': "[data-test='role-based-question-1']", 'question': 'How do you handle errors in JavaScript?'}
3. {'action': 'modifyIdealAnswer', 'target': "[data-test='ideal-answer-input']", 'answer': 'Using try-catch blocks'}
**Expected Result:** Role-based question is modified

### Create Interview - Create Interview Step
**Steps:**
1. {'action': 'click', 'target': "[data-test='create-interview-button']"}
**Expected Result:** Interview is created and public link is displayed

### Test candidate video interview
**Steps:**
1. Visit the responses tab
2. Click on the candidate's response to view structured answers and video recordings
3. Check if scores and resumes are displayed
**Expected Result:** The candidate's interview score, communication score, and comprehensive summary of the interview are displayed

### Test AI analyze scores
**Steps:**
1. Visit the interview screenings section
2. Check if AI analyze scores are displayed
**Expected Result:** AI analyze scores are displayed for the candidate

### Test action buttons
**Steps:**
1. Check if action buttons (select or reject) are displayed next to the candidate's profile
**Expected Result:** Action buttons (select or reject) are displayed next to the candidate's profile

### Test ré screening
**Steps:**
1. Create an interview and upload multiple résumés
2. Submit the résumés for screening
3. Check if AI screening process starts
**Expected Result:** AI screening process starts and assigns a ré score to each candidate

### Test semantic analysis and ré score
**Steps:**
1. Check if the system conducts a comprehensive semantic analysis
2. Check if ré score is assigned to each candidate based on their skills and experience
**Expected Result:** Ré score is assigned to each candidate based on their skills and experience, and AI recommends or rejects the profile

### Test interview link sending
**Steps:**
1. Select a candidate to proceed to the next round
2. Send an interview link to the candidate
3. Check if the link is valid for 24 hours
**Expected Result:** Interview link is sent to the candidate and is valid for 24 hours

### Test interview submission and review
**Steps:**
1. Check if the candidate can submit their interview at their convenience
2. Initiate the interview screening process
3. Review the summary of the interview
**Expected Result:** Candidate can submit their interview, and the summary of the interview is displayed for review

