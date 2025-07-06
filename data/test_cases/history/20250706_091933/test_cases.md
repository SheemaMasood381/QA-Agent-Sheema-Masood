### Create Interview - Job Description Input
**Steps:**
1. {'action': 'fill', 'target': "input[name='jobDescription']", 'value': 'JavaScript developer with AWS experience'}
**Expected Result:** Job description is filled and AI is suggesting questions

### Create Interview - Job Title Input
**Steps:**
1. {'action': 'fill', 'target': "input[name='jobTitle']", 'value': '2-year experienced JavaScript developer'}
**Expected Result:** AI generates a complete job description

### Create Interview - Enhanced JD Feature
**Steps:**
1. {'action': 'click', 'target': "button[aria-label='Enhanced JD Feature']"}
**Expected Result:** AI prefills and edits the job description

### Create Interview - Skill Recommendations
**Steps:**
1. {'action': 'wait', 'target': 'text=Skill Recommendations'}
2. {'action': 'check', 'target': "input[name='awsExperience']"}
**Expected Result:** AI extracts key skills from job description and user can pick from suggested skills

### Create Interview - Difficulty Level Selection
**Steps:**
1. {'action': 'selectOption', 'target': "select[name='difficultyLevel']", 'option': 'Moderate'}
**Expected Result:** Difficulty level of questions is set

### Create Interview - Company Name Input
**Steps:**
1. {'action': 'fill', 'target': "input[name='companyName']", 'value': 'Test Company'}
**Expected Result:** Company name is filled and AI analyzes job description

### Create Interview - Standard Questions
**Steps:**
1. {'action': 'check', 'target': "input[name='standardQuestion1']"}
2. {'action': 'check', 'target': "input[name='standardQuestion2']"}
**Expected Result:** Standard questions are populated and can be personalized

### Create Interview - Role-Based Questions
**Steps:**
1. {'action': 'check', 'target': "input[name='roleBasedQuestion1']"}
2. {'action': 'check', 'target': "input[name='roleBasedQuestion2']"}
**Expected Result:** Role-based questions are generated with preferred answers

### Create Interview - Create Option
**Steps:**
1. {'action': 'click', 'target': "button[aria-label='Create Interview']"}
**Expected Result:** Interview is created with a unique public interview link

### Test View Candidate Responses
**Steps:**
1. {'action': 'click', 'target': "link(text='Responses')"}
**Expected Result:** Candidate responses are displayed with structured answers, video recordings, scores, and resumes

### Test Interview Score
**Steps:**
1. {'action': 'click', 'target': "link(text='Interview Screenings')"}
2. {'action': 'getByText', 'target': 'Interview Score'}
**Expected Result:** The interview score is displayed

### Test Communication Score
**Steps:**
1. {'action': 'click', 'target': "link(text='Interview Screenings')"}
2. {'action': 'getByText', 'target': 'Communication Score'}
**Expected Result:** The communication score is displayed

### Test AI Analysis Summary
**Steps:**
1. {'action': 'click', 'target': "link(text='Interview Screenings')"}
2. {'action': 'getByText', 'target': 'Summary'}
**Expected Result:** The AI analysis summary is displayed with observations, positives, and negatives

### Test Action Button
**Steps:**
1. {'action': 'click', 'target': "button(text='Select' or text='Reject')"}
**Expected Result:** The candidate is either selected or rejected

### Test Resume Screening
**Steps:**
1. {'action': 'click', 'target': "link(text='Resume Screening')"}
2. {'action': 'uploadFile', 'target': "input[type='file']", 'file': 'resume.pdf'}
**Expected Result:** The AI commences the screening process and assigns a resume score

### Test AI Recommendation
**Steps:**
1. {'action': 'click', 'target': "link(text='Resume Screening')"}
2. {'action': 'getByText', 'target': 'Recommendation'}
**Expected Result:** The AI recommendation is displayed with a suitability score

### Test Send Interview Link
**Steps:**
1. {'action': 'click', 'target': "button(text='Send Interview Link')"}
**Expected Result:** The interview link is sent to the candidate and is valid for 24 hours

