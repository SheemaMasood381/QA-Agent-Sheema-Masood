### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'selector': "[name='jobDescription']", 'value': 'Experienced JavaScript developer with AWS experience'}
2. {'action': 'click', 'selector': "[type='submit']"}
**Expected Result:** {'description': 'AI suggests questions based on the job description', 'selector': '.ai-generated-questions'}

### Edit and Save Job Description
**Steps:**
1. {'action': 'fill', 'selector': "[name='jobDescription']", 'value': 'Updated job description with 2 years of AWS experience'}
2. {'action': 'click', 'selector': "[type='submit']"}
**Expected Result:** {'description': 'Job description is saved and skill recommendations are displayed', 'selector': '.skill-recommendations'}

### Select and Customize Questions
**Steps:**
1. {'action': 'check', 'selector': "[name='standardQuestions']"}
2. {'action': 'check', 'selector': "[name='roleBasedQuestions']"}
3. {'action': 'fill', 'selector': "[name='difficultyLevel']", 'value': 'Moderate'}
**Expected Result:** {'description': 'Questions are populated and customizable', 'selector': '.question-list'}

### Create Interview
**Steps:**
1. {'action': 'click', 'selector': "[type='submit']"}
**Expected Result:** {'description': 'Interview is created with unique public interview link', 'selector': '.interview-link'}

### Verify Public Interview Link
**Steps:**
1. {'action': 'visit', 'url': 'generated-interview-link'}
**Expected Result:** {'description': 'Public interview link is accessible and functional', 'selector': '.interview-form'}

### Test Video Interview Response
**Steps:**
1. {'action': 'visit', 'target': 'responses tab'}
2. {'action': 'assert', 'target': 'structured answers and video recordings are displayed'}
3. {'action': 'assert', 'target': 'scores and resumes are displayed'}
**Expected Result:** Video interview response is displayed with scores and resumes

### Test Interview Screenings
**Steps:**
1. {'action': 'visit', 'target': 'interview screenings section'}
2. {'action': 'assert', 'target': 'AI analyzed scores are displayed'}
**Expected Result:** AI analyzed scores are displayed in interview screenings section

### Test Candidate Scoring
**Steps:**
1. {'action': 'get text', 'target': 'interview score'}
2. {'action': 'get text', 'target': 'communication score'}
**Expected Result:** Interview score and communication score are displayed

### Test Resume Screening
**Steps:**
1. {'action': 'upload resumes', 'target': 'résumés input field'}
2. {'action': 'submit', 'target': 'upload resumes button'}
3. {'action': 'assert', 'target': 'ré score is displayed'}
**Expected Result:** Resume screening process is successful and ré score is displayed

### Test AI Recommendations
**Steps:**
1. {'action': 'get text', 'target': 'AI recommendation message'}
**Expected Result:** AI recommendation message is displayed

### Test Interview Link Sending
**Steps:**
1. {'action': 'click', 'target': 'send interview link button'}
2. {'action': 'assert', 'target': 'interview link is sent successfully'}
**Expected Result:** Interview link is sent successfully to the candidate

